from flask import Flask, jsonify
from flask_cors import CORS

led = False

app = Flask(__name__)

CORS(app)

@app.route('/api/status', methods=['GET'])
def status():
    print(f'Status: {led}')
    return jsonify({
        'status': led
    })

@app.route('/api/toggle', methods=['POST'])
def toggle():
    global led
    led = not led
    print(f'Status: {led}')
    return "Ok"

app.run(host='0.0.0.0', port=8080)
