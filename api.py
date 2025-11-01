"""
api.py
Always shows latest iot_command from MongoDB on any route.
"""

from flask import Flask
from pymongo import MongoClient
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.WARNING)

# MongoDB setup
MONGO_URI = "mongodb+srv://iosachinruhela_db_user:madamji@edith.gjjdqq3.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "edith"
COLLECTION_NAME = "iot_commands"

client = MongoClient(MONGO_URI)
collection = client[DB_NAME][COLLECTION_NAME]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_latest_command(path):
    try:
        cmd = collection.find().sort("timestamp", -1).limit(1)[0]
        return cmd["iot_command"]
    except:
        return "No command found"

if __name__ == "__main__":
    print("API Running: http://192.168.x.x:5000/")
    app.run(host="0.0.0.0", port=5000, debug=False)
