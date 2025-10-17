import os
from datetime import timezone, datetime
from dotenv import load_dotenv
import requests
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

    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        fact_data = response.json()
        cat_fact = fact_data.get("fact", "Cats are cool but fact not found.")
    except requests.exceptions.RequestException:
        cat_fact = "Unable to fetch cat at the moment"

    data = {
        "status": "success",
        "user": user,
        "timestamp": timestamp,
        "fact": "Temporary placeholder - real cat fact coming next step"
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)