# utils.py
import logging
import os
from datetime import datetime

# Set up logging
LOG_FILE = "clausecrafter_log.txt"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_event(event_type, message):
    logging.info(f"{event_type}: {message}")


def chunk_text(text, chunk_size=300):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]


def save_json_output(output, filename_prefix="output"):
    import json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)
    return filename