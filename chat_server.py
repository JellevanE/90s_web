from flask import Flask, request, jsonify
import time

app = Flask(__name__, static_folder=".", static_url_path="")


@app.get("/")
def root():
    """Serve the homepage."""
    return app.send_static_file("index.html")

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
