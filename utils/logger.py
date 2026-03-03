# utils/logger.py
from datetime import datetime

def log(message, logfile="bbscan.log"):
    with open(logfile, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
