import subprocess
import time

def start_ngrok(port=5555):
    print(f"[*] Starting ngrok tunnel on port {port}...")
    subprocess.Popen(["./ngrok", "tcp", str(port)])
    time.sleep(5)
    print("[+] Ngrok tunnel started.")

if __name__ == "__main__":
    start_ngrok()
