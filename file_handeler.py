import json
import os

DATA_FILE = "data/bank_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump(load_data(), f,indent=4)