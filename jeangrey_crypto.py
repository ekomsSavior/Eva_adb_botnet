from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64

SECRET_KEY = b'Sixteen byte key'  # Must be 16, 24, or 32 bytes

def pad(s):
    pad_len = AES.block_size - len(s) % AES.block_size
    return s + chr(pad_len) * pad_len

def unpad(s):
    return s[:-ord(s[-1])]

def encrypt(message):
    message = pad(message)
    iv = get_random_bytes(16)
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(iv + encrypted).decode()

def decrypt(ciphertext_b64):
    raw = base64.b64decode(ciphertext_b64)
    iv = raw[:16]
    encrypted = raw[16:]
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted).decode()
    return unpad(decrypted)
