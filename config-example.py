# config.example.py — copy this to config.py and fill in your values

NETWORK_RANGE = "192.168.1.0/24"
SCAN_INTERVAL = 15

TWILIO_ACCOUNT_SID = "your_account_sid_here"
TWILIO_AUTH_TOKEN = "your_auth_token_here"
TWILIO_FROM_NUMBER = "+1XXXXXXXXXX"
TWILIO_TO_NUMBER = "+1XXXXXXXXXX"

ENABLE_SMS = False
ENABLE_DESKTOP = True

LOG_FILE = "scan_log.txt"
WHITELIST_FILE = "whitelist.json"