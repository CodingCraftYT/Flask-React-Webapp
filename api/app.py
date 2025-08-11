from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api")
def index():
    return jsonify({"message": "Welcome to Coding Craft YT Channel!"})
