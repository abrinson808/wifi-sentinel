# WiFi Sentinel 🛡️

A Python-based home network monitor that scans your WiFi for unknown devices
and sends instant alerts via Mac desktop notification.

Built as a personal security tool after going through the process of securing
my home network. Wanted something handmade that would alert me more frequently then
the ISP's own app currently does. This is an especially great usecase for those that have
an at home Desktop or stationary Laptop setup or Server setups.

---

## Features

- 🔍 Scans your entire home network using nmap
- 📋 Maintains a whitelist of trusted devices
- 🔔 Instant Mac desktop notifications when unknown devices are detected
- 📝 Logs all scan activity with timestamps
- ⏰ Runs automatically in the background on a configurable schedule
- 🖥️ Works across multiple Macs on the same network

---

## Tech Stack

- Python 3.14
- [python-nmap](https://pypi.org/project/python-nmap/) — network scanning
- [pync](https://pypi.org/project/pync/) — macOS desktop notifications
- [schedule](https://pypi.org/project/schedule/) — job scheduling
- [Twilio](https://www.twilio.com/) — SMS alerts (optional)

---

## Setup

### 1. Prerequisites

Install Homebrew and nmap:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install nmap
```

### 2. Clone the repo

```bash
git clone https://github.com/yourusername/wifi-sentinel.git
cd wifi-sentinel
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install python-nmap twilio pync schedule
```

### 5. Configure

```bash
cp config.example.py config.py
```

Edit `config.py` with your network range and optional Twilio credentials.

### 6. Run

```bash
# Manual scan
sudo venv/bin/python scanner.py

# Run on a schedule (every 15 min by default)
sudo venv/bin/python scheduler.py
```

---

## First Run

On first run, WiFi Sentinel will automatically scan your network and build
a whitelist of all currently connected devices. Any new device that appears
on subsequent scans will trigger an alert.

---

## Project Structure
