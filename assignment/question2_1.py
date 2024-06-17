import psutil
import logging
from datetime import datetime
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
LOG_FILE = "/var/log/system_health.log"


logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def log_alert(message):
    logging.info(f"{datetime.now()}: {message}")

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

def check_memory():
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        log_alert(f"High Memory usage detected: {memory_info.percent}%")

def check_disk():
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        log_alert(f"Low Disk space available: {disk_info.percent}% used")

def check_processes():
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]
    for proc in processes:
        if proc['cpu_percent'] > CPU_THRESHOLD:
            log_alert(f"Process {proc['name']} (PID {proc['pid']}) is using {proc['cpu_percent']}% CPU")
        if proc['memory_percent'] > MEMORY_THRESHOLD:
            log_alert(f"Process {proc['name']} (PID {proc['pid']}) is using {proc['memory_percent']}% Memory")

def main():
    check_cpu()
    check_memory()
    check_disk()
    check_processes()

if __name__ == "__main__":
    main()
