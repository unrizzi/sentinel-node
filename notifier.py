import requests

class DiscordNotifier:
    def __init__(self,webhook_url):
        self.webhook_url = webhook_url
    
    def send_alert(self, title, message):

        payload = {
            "embeds": [
                {
                    "title": title,
                    "description": message
                }
            ]
        }

        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"[ERROR]: Failed to send Discord alert: {e}")
            return False