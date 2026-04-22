import os
from dotenv import load_dotenv
from analyzer import NetworkAnalyzer

def main():
    load_dotenv()
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("[WARN]: DISCORD_WEBHOOK_URL not found in environment.")
    else:
        print("[OK]: Configuration loaded successfully.")
    print("SentinelNode is starting...")

    analyzer = NetworkAnalyzer()
    connections = analyzer.get_current_connections()

    print(f"Found {len(connections)} active connections.")
    for ip, port in connections:
        print(f"Target: {ip}:{port}")

if __name__ == "__main__":
    main()