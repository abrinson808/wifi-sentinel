# scanner.py — scans the network and detects unknown devices

import nmap
import json
import os
from datetime import datetime
from config import NETWORK_RANGE, LOG_FILE, WHITELIST_FILE
from notifier import alert_unknown_device


def load_whitelist():
    if not os.path.exists(WHITELIST_FILE):
        return {}
    with open(WHITELIST_FILE, "r") as f:
        content = f.read().strip()
        if not content:
            return {}
        return json.loads(content)


def save_whitelist(whitelist):
    with open(WHITELIST_FILE, "w") as f:
        json.dump(whitelist, f, indent=4)


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")


def scan_network():
    print(f"\n🔍 Scanning {NETWORK_RANGE} ...")
    nm = nmap.PortScanner()
    nm.scan(hosts=NETWORK_RANGE, arguments="-sn")

    devices = {}
    for host in nm.all_hosts():
        mac = nm[host]["addresses"].get("mac", "UNKNOWN")
        hostname = nm[host].hostname() or "Unknown"
        devices[mac] = {
            "ip": host,
            "hostname": hostname,
            "last_seen": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    return devices


def check_for_intruders(devices, whitelist):
    unknown = {}
    for mac, info in devices.items():
        if mac not in whitelist and mac != "UNKNOWN":
            unknown[mac] = info
    return unknown


def build_whitelist_from_scan():
    print("\n🛠  First run detected — building your whitelist...\n")
    devices = scan_network()

    if not devices:
        print("⚠️  No devices found. Check your NETWORK_RANGE in config.py")
        return

    print(f"Found {len(devices)} device(s) on your network:\n")
    for mac, info in devices.items():
        print(f"  IP: {info['ip']:<16} MAC: {mac:<20} Hostname: {info['hostname']}")

    print("\nAdding all current devices to your whitelist as trusted...")
    save_whitelist(devices)
    log_event(f"Whitelist created with {len(devices)} trusted devices.")
    print("✅ Whitelist saved to whitelist.json\n")


def run_scan():
    whitelist = load_whitelist()

    if not whitelist:
        build_whitelist_from_scan()
        return

    devices = scan_network()
    unknown = check_for_intruders(devices, whitelist)

    if unknown:
        for mac, info in unknown.items():
            message = f"⚠️  UNKNOWN DEVICE — IP: {info['ip']} | MAC: {mac} | Hostname: {info['hostname']}"
            log_event(message)
            alert_unknown_device(
                mac=mac,
                ip=info['ip'],
                hostname=info['hostname']
            )
        return unknown
    else:
        log_event(f"Scan complete. {len(devices)} device(s) found. All trusted.")
        print("✅ All devices recognized. Network looks clean!\n")
        return {}


if __name__ == "__main__":
    # Temporary test — simulates an unknown device alert
    print("🧪 Testing unknown device alert...")
    alert_unknown_device(
        mac="AA:BB:CC:DD:EE:FF",
        ip="10.0.0.99",
        hostname="Unknown",
        vendor="Test Device"
    )