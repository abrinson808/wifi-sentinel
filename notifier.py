# notifier.py — handles desktop and SMS alerts

from config import (
    ENABLE_DESKTOP,
    ENABLE_SMS,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_FROM_NUMBER,
    TWILIO_TO_NUMBER
)


def send_desktop_notification(title, message):
    """Send a Mac desktop notification"""
    if not ENABLE_DESKTOP:
        return
    try:
        import pync
        pync.notify(message, title=title, sound="Funk")
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
    title = "⚠️ WiFi Sentinel Alert"
    message = (
        f"Unknown device on your network!\n"
        f"IP: {ip}\n"
        f"MAC: {mac}\n"
        f"Vendor: {vendor}\n"
        f"Hostname: {hostname}"
    )
    send_desktop_notification(title, message)
    send_sms(f"WiFi Sentinel: Unknown device detected! IP: {ip} | MAC: {mac} | Vendor: {vendor}")


if __name__ == "__main__":
    # Test the notifier directly
    print("🧪 Testing notifications...")
    alert_unknown_device(
        mac="AA:BB:CC:DD:EE:FF",
        ip="10.0.0.99",
        hostname="Unknown",
        vendor="Test Device"
    )