import os

STATE_FILE = "processed_ids.txt"


def load_processed_ids():
    if not os.path.exists(STATE_FILE):
        return set()
    with open(STATE_FILE, "r") as f:
        return set(f.read().splitlines())


def save_processed_id(msg_id):
    with open(STATE_FILE, "a") as f:
        f.write(msg_id + "\n")
