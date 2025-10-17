import os
from datetime import timezone, datetime
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def get_profile():
    user = {
        "email": os.getenv("EMAIL"),
        "name": os.getenv("NAME"),
        "stack": os.getenv("STACK"),
    }

    timestamp = datetime.now(timezone.utc).isoformat()

    data = {
        "status": "success",
        "user": user,
        "timestamp": timestamp,
        "fact": "Temporary placeholder - real cat fact coming next step"
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)