import os, time, logging
from dotenv import load_dotenv
from analyzer import NetworkAnalyzer
from notifier import DiscordNotifier
from rules import SecurityRules

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("sentinel.log"),
        logging.StreamHandler()
    ]
)

def main():
    load_dotenv()
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    analyzer = NetworkAnalyzer()
    notifier = DiscordNotifier(webhook_url) if webhook_url else None
    logging.info("SentinelNode is active and monitoring...")
    if not notifier:
        logging.warning("Discord Webhook not configured.")

    try:
        while True:
            found_alerts = analyzer.scan(SecurityRules)
            for addr, category, severity in found_alerts:
                ip, port = addr
                logging.warning(f"SUSPICIOUS ACTIVITY: {category} detected on {ip}:{port} [Severity: {severity}]")
                if notifier:
                    alert_msg = f"Detection: {category}\nTarget: {ip}:{port}\nSeverity: {severity}"
                    notifier.send_alert(category, alert_msg)
            time.sleep(30)
    except KeyboardInterrupt:
        logging.info("SentinelNode stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected system failure: {e}")

if __name__ == "__main__":
    main()