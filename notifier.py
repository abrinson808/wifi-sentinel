# notifier.py — cross-platform desktop and SMS alerts

import platform
from config import (
    ENABLE_DESKTOP,
    ENABLE_SMS,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_FROM_NUMBER,
    TWILIO_TO_NUMBER
)


def send_desktop_notification(title, message):
    """Send a desktop notification — works on Mac, Windows, and Linux"""
    if not ENABLE_DESKTOP:
        return
    try:
        from plyer import notification
        notification.notify(
            title=title,
            message=message,
            app_name="WiFi Sentinel",
            timeout=10
        )
        print("🔔 Desktop notification sent!")
    except Exception as e:
        print(f"⚠️  Desktop notification failed: {e}")


def send_sms(message):
    """Send an SMS alert via Twilio"""
    if not ENABLE_SMS:
        print("📵 SMS disabled in config — skipping.")
        return
    try:
        from twilio.rest import Client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_FROM_NUMBER,
            to=TWILIO_TO_NUMBER
        )
        print("📱 SMS alert sent!")
    except Exception as e:
        print(f"⚠️  SMS failed: {e}")


def alert_unknown_device(mac, ip, hostname, vendor="Unknown"):
    """Fire all enabled alerts for an unknown device"""
    os_name = platform.system()
    title = "WiFi Sentinel Alert"
    message = (
        f"Unknown device on your network!\n"
        f"IP: {ip}\n"
        f"MAC: {mac}\n"
        f"Vendor: {vendor}\n"
        f"Hostname: {hostname}"
    )
    send_desktop_notification(title, message)
    send_sms(
        f"WiFi Sentinel: Unknown device! "
        f"IP: {ip} | MAC: {mac} | Vendor: {vendor}"
    )
    print(f"[{os_name}] Alert fired for {ip}")


if __name__ == "__main__":
    print("🧪 Testing cross-platform notification...")
    alert_unknown_device(
        mac="AA:BB:CC:DD:EE:FF",
        ip="10.0.0.99",
        hostname="Unknown",
        vendor="Test Device"
    )