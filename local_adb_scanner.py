#!/usr/bin/env python3

import socket
import ipaddress
import subprocess
import threading
import time

PORT = 5555
TIMEOUT = 0.5
LIVE_ADB_TARGETS = set()  # Use a set to avoid duplicates

def scan_ip(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((str(ip), PORT))
        if str(ip) not in LIVE_ADB_TARGETS:
            print(f"[✓] New ADB Target: {ip}:{PORT}")
            LIVE_ADB_TARGETS.add(str(ip))
            subprocess.run(["adb", "connect", f"{ip}:{PORT}"])
    except:
        pass
    s.close()

def local_scan():
    print("\n[*] Scanning local subnet for open ADB ports...")
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    net = ipaddress.IPv4Network(local_ip + '/24', strict=False)

    threads = []
    for ip in net.hosts():
        t = threading.Thread(target=scan_ip, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] ADB Devices Connected:")
    for ip in LIVE_ADB_TARGETS:
        print(f"    └─ {ip}:{PORT}")

if __name__ == "__main__":
    while True:
        local_scan()
        print(" Sleeping 5 minutes before next scan...\n")
        time.sleep(300)  # 5 minutes
