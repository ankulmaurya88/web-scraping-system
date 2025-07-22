# Store parsed data
import json

def store(data):
    with open('data.json', 'a') as f:
        f.write(json.dumps(data) + "\n")
