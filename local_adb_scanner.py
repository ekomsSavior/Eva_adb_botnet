#!/usr/bin/env python3

import socket
import ipaddress
import subprocess
import threading

PORT = 5555
TIMEOUT = 1
LIVE_ADB_TARGETS = []

def scan_ip(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((str(ip), PORT))
        print(f"[✓] Found ADB: {ip}:{PORT}")
        LIVE_ADB_TARGETS.append(str(ip))
        subprocess.run(["adb", "connect", f"{ip}:{PORT}"])
    except:
        pass
    s.close()

def local_scan():
    print("[*] Scanning local subnet for open ADB ports...\n")
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

    print("\n[+] Active ADB Targets Found:")
    for ip in LIVE_ADB_TARGETS:
        print(f"    └─ {ip}:{PORT}")

if __name__ == "__main__":
    local_scan()
