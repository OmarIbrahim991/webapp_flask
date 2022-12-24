from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def main():
    return "<h1>Flask Web App</h1>"

@socketio.on("initialize")
def start():
    socketio.emit("start", ["A", "B", "C"])
    return ""
