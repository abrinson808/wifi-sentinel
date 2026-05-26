# WiFi Sentinel 🛡️

A cross-platform Python network monitor that scans your WiFi for unknown
devices and sends instant desktop alerts. Works on macOS, Windows, and Linux.

Built as a personal security tool after going through the process of securing
my home network and realizing I had no way of knowing when new devices connected.

---

## Features

- 🔍 Scans your entire home network using nmap
- 📋 Maintains a whitelist of trusted devices
- 🔔 Cross-platform desktop notifications (macOS, Windows, Linux)
- 🏭 Automatic MAC vendor lookup to identify device manufacturers
- 📝 Logs all scan activity with timestamps
- ⏰ Runs automatically in the background on a configurable schedule
- 🛠️ Setup wizard that works on any OS

---

## Supported Platforms

| Platform | Notifications | Scanning | Tested |
| -------- | ------------- | -------- | ------ |
| macOS    | ✅            | ✅       | ✅     |
| Windows  | ✅            | ✅       | ✅     |
| Linux    | ✅            | ✅       | ⏳     |

---

## Tech Stack

- Python 3.8+
- [python-nmap](https://pypi.org/project/python-nmap/) — network scanning
- [plyer](https://pypi.org/project/plyer/) — cross-platform desktop notifications
- [schedule](https://pypi.org/project/schedule/) — job scheduling
- [certifi](https://pypi.org/project/certifi/) — SSL certificate handling
- [macvendors.com](https://macvendors.com/) — MAC address vendor lookup

---

## Quick Start

### 1. Prerequisites

**macOS:**

```bash
brew install nmap
```

**Windows:**
Download nmap from https://nmap.org/download.html
Make sure to check "Add to PATH" during installation.

**Linux:**

```bash
sudo apt install nmap
```

### 2. Clone the repo

```bash
git clone https://github.com/abrinson808/wifi-sentinel.git
cd wifi-sentinel
```

### 3. Create a virtual environment

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Run the setup wizard

```bash
python setup.py
```

This will install all dependencies and create your config file automatically.

### 5. Configure

Open `config.py` and set your network range:

**macOS:**

```bash
ipconfig getifaddr en0
```

**Windows:**

```bash
ipconfig
```

**Linux:**

```bash
ip addr
```

### 6. Run

**macOS/Linux:**

```bash
# Manual scan
sudo venv/bin/python scanner.py

# Run on a schedule
sudo venv/bin/python scheduler.py
```

**Windows (run as Administrator):**

```bash
# Manual scan
venv\Scripts\python scanner.py

# Run on a schedule
venv\Scripts\python scheduler.py
```

---

## First Run

On first run, WiFi Sentinel will automatically scan your network and build
a whitelist of all currently connected devices. Any new device that appears
on subsequent scans will trigger an alert including the device's IP address,
MAC address, and manufacturer name.

### Adding new devices to your whitelist

If a trusted device triggers an alert, you can add it to your whitelist
by running:

**macOS/Linux:**

```bash
sudo venv/bin/python -c "
import json
with open('whitelist.json', 'r') as f:
    wl = json.load(f)
wl['XX:XX:XX:XX:XX:XX'] = {'ip': '10.0.0.X', 'hostname': 'Unknown', 'last_seen': 'now'}
with open('whitelist.json', 'w') as f:
    json.dump(wl, f, indent=4)
print('Device added!')
"
```

**Windows (Command Prompt as Administrator):**

```bash
python -c "import json; wl=json.load(open('whitelist.json')); wl['XX:XX:XX:XX:XX:XX']={'ip':'10.0.0.X','hostname':'Unknown','last_seen':'now'}; json.dump(wl,open('whitelist.json','w'),indent=4); print('Device added!')"
```

Replace `XX:XX:XX:XX:XX:XX` with the device's MAC address and `10.0.0.X`
with its IP address from the alert.

---

## Project Structure

wifi-sentinel/  
├── scanner.py # core scanning logic + vendor lookup
├── notifier.py # cross-platform desktop alerts
├── scheduler.py # automatic scheduling
├── setup.py # first-run setup wizard
├── whitelist.json # trusted devices (gitignored)
├── scan_log.txt # scan history (gitignored)
├── config.py # your settings (gitignored)
├── config.example.py # safe template for config
└── README.md

---

## Roadmap

- [x] Cross-platform support (macOS, Windows, Linux)
- [x] MAC vendor lookup
- [ ] Web dashboard to view scan history
- [ ] Auto-launch on startup
- [ ] Email alerts via Gmail SMTP

---

## Author

Built by [@abrinson808](https://github.com/abrinson808)
