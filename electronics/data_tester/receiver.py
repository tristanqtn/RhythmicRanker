from flask import Flask, request, jsonify

app = Flask(__name__)


IP = "0.0.0.0"
PORT = 9999

@app.route('/metrics', methods=['POST'])
def metrics():
    # Extract JSON data from the request
    data = request.get_json()
        
    # Display the received data
    print(data)
    return jsonify(data), 200

#please change host IP to your own IP
if __name__ == '__main__':
    app.run(host=IP, port=PORT)
    print("Receiver is running on http://{}:{}".format(IP, PORT))
