from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Get the directory path of the current Python file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the .env file in the parent directory
dotenv_path = os.path.join(current_dir, '..', '.env')

# Load environment variables from .env file
load_dotenv(dotenv_path)

IP = os.getenv("BROKER_IP")
PORT = os.getenv("BROKER_PORT")

@app.route('/metrics', methods=['POST'])
def metrics():
    # Extract JSON data from the request
    data = request.get_json()

    #post data to http://localhost:8888/metrics
    requests.post(f'http://{os.getenv("INTERNAL_INPUT_API_IP")}:{os.getenv("INTERNAL_INPUT_API_PORT")}/metrics', json=data)

    return jsonify(data), 200

#please change host IP to your own IP
if __name__ == '__main__':
    app.run(host=IP, port=PORT)
    print("Receiver is running on http://{}:{}".format(IP, PORT))
