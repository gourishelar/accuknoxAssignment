import subprocess
import logging
from datetime import datetime


SOURCE_DIR = "/path/to/source"  # Directory to be backed up
REMOTE_SERVER = "user@remote.server.com"  # Remote server
REMOTE_DIR = "/path/to/remote/backup"  # Remote backup directory
LOG_FILE = "/var/log/backup.log"


logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def log_backup_status(message):
    logging.info(f"{datetime.now()}: {message}")

def perform_backup():
    try:
        
        result = subprocess.run(
            ["rsync", "-avz", SOURCE_DIR, f"{REMOTE_SERVER}:{REMOTE_DIR}"],
            check=True,
            capture_output=True,
            text=True
        )
        log_backup_status(f"Backup successful: {result.stdout}")
    except subprocess.CalledProcessError as e:
        log_backup_status(f"Backup failed: {e.stderr}")

def main():
    perform_backup()

if __name__ == "__main__":
    main()
