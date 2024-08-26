import json
import os

CONFIG_FILE = 'config/timer_config.json'

def save_config(window_geometry, time, interval):
    config = {
        'geometry': window_geometry,
        'time': time,
        'interval': interval
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return None
