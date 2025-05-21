import os  # Add this import
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import time

# Determine the absolute path to the directory containing chat_server.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=APP_ROOT, static_url_path="")  # Modified this line
CORS(app)  # Enable CORS for all routes


@app.post('/api/chat')
def chat():
    data = request.get_json(force=True)
    message = data.get('message', '')
    history = data.get('history', [])
    # Dummy processing to simulate latency / API call
    time.sleep(1)
    reply = f"You said: {message}"
    return jsonify({'reply': reply, 'history': history + [message, reply]})


if __name__ == '__main__':
    app.run(debug=True)
