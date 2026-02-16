from flask import Flask, jsonify
from flask_cors import CORS
from database import init_db

app = Flask(__name__)
CORS(app)  # Allows frontend to call your API

# Initialize database when app starts
init_db()

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "message": "API is running"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

