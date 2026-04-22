import os, time
from dotenv import load_dotenv
from analyzer import NetworkAnalyzer
from notifier import DiscordNotifier
from rules import SecurityRules

def main():
    load_dotenv()
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    analyzer = NetworkAnalyzer()
    notifier = DiscordNotifier(webhook_url) if webhook_url else None
    connections = analyzer.scan(SecurityRules)

    print("--- SentinelNode: Active and Monitoring ---")
    if not notifier:
        print("[WARN]: Discord Webhook not configured.")

    try:
        while True:
            found_alerts = analyzer.scan(SecurityRules)
            for addr, category, severity in found_alerts:
                ip, port = addr
                alert_msg = f"Detection: {category}\nTarget: {ip}:{port}\nSeverity: {severity}"
                print(f"[ALERT]: {category} on {ip}:{port}")
                if notifier:
                    notifier.send_alert(category, alert_msg)
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n[INFO]: SentinelNode stopped by user.")
    except Exception as e:
        print(f"[ERROR]: Unexpected system failure: {e}")

if __name__ == "__main__":
    main()