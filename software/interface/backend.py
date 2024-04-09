from flask import Flask, render_template, Response, jsonify
from influxdb_client import InfluxDBClient
import os
import requests
from dotenv import load_dotenv
import json
import time

GRAB_TRHESHOLD = 30000

app = Flask(__name__)
app.start_time = time.time()


# Get the directory path of the current Python file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the .env file in the parent directory
dotenv_path = os.path.join(current_dir, '..', '.env')

# Load environment variables from .env file
load_dotenv(dotenv_path)

# Connect to InfluxDB
client = InfluxDBClient(url=os.getenv("INFLUX_URL"), token=os.getenv("INFLUX_TOKEN"), org=os.getenv("INFLUX_ORG"))
query_api = client.query_api()

# Function to stream data
def stream_data():
    """
    Stream data from a specified InfluxDB bucket in real-time.
    
    Returns:
        str: Server-sent events (SSE) containing the streamed data.
    """
    all_query = 'from(bucket: "{}") |> range(start: -1h)'.format(os.getenv("INFLUX_BUCKET"))
    
    
    az_query = f'''
    from(bucket: "{os.getenv("INFLUX_BUCKET")}")
    |> range(start: -1h)
    |> filter(fn: (r) => r["_measurement"] == "az")
    |> sort(columns: ["_time"], desc: true)
    |> limit(n:2)
    '''

    grab_query = f'''
    from(bucket: "{os.getenv("INFLUX_BUCKET")}")
    |> range(start: -1h)  
    |> filter(fn: (r) => r["_measurement"] == "force_value")
    |> last()
    '''
    mean_z_query = f'''
    from(bucket: "{os.getenv("INFLUX_BUCKET")}")
    |> range(start: -10s)
    |> filter(fn: (r) => r["_measurement"] == "az")
    |> mean(column: "_value")
    '''

    while True:
        
        data = []

        az_tables = query_api.query(az_query)
        grab_data = query_api.query(grab_query)
        mean_z = query_api.query(mean_z_query)

        time = az_tables[0].records[0].get_time()-az_tables[0].records[1].get_time()        

        instant_height = compute_height(mean_z[0].records[0].get_value(), abs(az_tables[0].records[0].get_value()-az_tables[0].records[1].get_value()), time.total_seconds()) 

        data.append({
                        "_time": az_tables[0].records[0].get_time().strftime('%Y-%m-%dT%H:%M:%SZ'),  # Convert datetime to string
                        "_value": -instant_height,
                        "_field": "Hauteur",
                        "_measurement": "Hauteur (cm)",
                        "_conformity": ""  # Add a conformity field to indicate data validation status
        })

        for table in grab_data:
            for record in table.records:
                if(record.get_value() > GRAB_TRHESHOLD):   
                    data.append({
                        "_time": record.get_time().strftime('%Y-%m-%dT%H:%M:%SZ'),  # Convert datetime to string
                        "_value": record.get_value(),
                        "_field": record.get_field(),
                        "_measurement": "Préhension",
                        "_conformity": "En main"  # Add a conformity field to indicate data validation status
                    })
                else:
                    data.append({
                        "_time": record.get_time().strftime('%Y-%m-%dT%H:%M:%SZ'),  # Convert datetime to string
                        "_value": record.get_value(),
                        "_field": record.get_field(),
                        "_measurement": "Préhension",
                        "_conformity": "Laché"  # Add a conformity field to indicate data validation status
                    })

        all_data  = query_api.query(all_query)

        for table in all_data:
            for record in table.records:
                # do not append if sensor name is npm_test
                if (record.get_measurement() != "npm_test" and record.get_measurement() != "force_value"):
                    # implement data validation here
                    data.append({
                        "_time": record.get_time().strftime('%Y-%m-%dT%H:%M:%SZ'),  # Convert datetime to string
                        "_value": record.get_value(),
                        "_field": record.get_field(),
                        "_measurement": record.get_measurement(),
                        "_conformity": ""  # Add a conformity field to indicate data validation status
                    })

        yield "data: {}\n\n".format(json.dumps(data))
        #time.sleep(0.1)  # Adjust the sleep time as needed


def compute_height(v_z0, a_z, time):
    """
    Computes the height of an object given initial velocity in the z direction,
    acceleration in the z direction, and the time elapsed.

    Parameters:
    - v_z0: Initial velocity in the z direction (m/s)
    - a_z: Acceleration in the z direction (m/s^2). Note: Include gravity here if not included in initial acceleration.
    - time: Time since the start (seconds)

    Returns:
    - Height of the object at the given time.
    """
    g = 9.81  # Acceleration due to gravity (m/s^2), positive downwards
    height = v_z0 * time **2 + 0.5 * (a_z - g) * time ** 2  # Assuming upwards is positive, subtract gravity from acceleration
    return height


# API endpoint to stream data
@app.route('/api/stream')
def stream():
    """
    Stream endpoint that streams data from a specified InfluxDB bucket in real-time. 
    
    Tags: backend, streaming

    Returns:
        Response: Server-sent events (SSE) containing the streamed data.
    """
    return Response(stream_data(), mimetype='text/event-stream')

# Function to check InfluxDB health
def check_influxdb_health():
    """
    Check the health status of the connected InfluxDB database. This function uses the `ready` method of the InfluxDB client to check the health of the InfluxDB database. If the `ready` method returns a non-empty response, the function returns True, indicating that InfluxDB is healthy. If the `ready` method raises an exception or returns an empty response, the function returns False, indicating that InfluxDB is not healthy.

    Tags: InfluxDB, health check, monitoring
    
    Returns:
        bool: True if InfluxDB is healthy, False otherwise.
    """
    try:
        ping_response = client.ready()
        if ping_response:
            return True
    except Exception as e:
        print("Error checking InfluxDB health:", str(e))
    return False

# API endpoint to check InfluxDB health
@app.route('/api/health/influx')
def influx_health():
    """
    Check the health status of the connected InfluxDB database. 

    Tags: InfluxDB, health check, monitoring

    Returns:
        Response: JSON response containing the health status.
    """
    health_check = {
        "uptime": time.time() - app.start_time,
        "status": "OK",
        "timestamp": int(time.time())
    }
    if check_influxdb_health():
        return jsonify(health_check), 200
    else:
        health_check["status"] = "ERROR"
        return jsonify(health_check), 503

# API endpoint to check backend health
@app.route('/api/health/backend')
def backend_health():
    """
    Check the health status of the backend server hosting the API.
    
    Tags: health check, backend, monitoring

    Returns:
        Response: JSON response containing the health status.
    """
    health_check = {
        "uptime": time.time() - app.start_time,
        "status": "OK",
        "timestamp": int(time.time())
    }
    return jsonify(health_check), 200

# API endpoint to check InfluxDB health
@app.route('/api/health/api')
def api_health():
    """
    Check the health status of the data inout API endpoint. This forwards the health check request to the data input API and returns the response.

    Tags: API, health check, monitoring

    Returns:
        Response: JSON response containing the health status.
    """
     # Load IP and port from environment variables
    ip = os.getenv('INTERNAL_INPUT_API_IP')
    port = os.getenv('INTERNAL_INPUT_API_PORT')

    # Construct the target URL
    target_url = f'http://{ip}:{port}/health/influx'

    try:
        # Forward the request to the target URL
        response = requests.get(target_url)
        response.raise_for_status()

        # Return the response from the target URL
        return response.json(), response.status_code

    except requests.exceptions.RequestException as e:
        print(f"Error forwarding request: {e}")
        return jsonify({"status": "ERROR"}), 500


@app.route('/')
def index():
    data = stream_data()
    return render_template('./index.html', data=data)

@app.route('/api/docs')
def docs():
    return render_template('./docs.html')

if __name__ == '__main__':
    app.run(debug=True)
