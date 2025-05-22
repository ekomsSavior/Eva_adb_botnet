import os
import json
import time
import socket

def write_state():
    bot_id = f"bot_{socket.gethostbyname(socket.gethostname())}"
    os.makedirs(f"bots/{bot_id}", exist_ok=True)
    with open(f"bots/{bot_id}/jeangrey_state.json", "w") as f:
        json.dump({
            "bot_id": bot_id,
            "ip": socket.gethostbyname(socket.gethostname()),
            "tags": ["android", "mesh", "jeangrey"],
            "last_seen": time.ctime()
        }, f, indent=4)

write_state()
