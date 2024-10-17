import requests
import json

class BotManager:
    def __init__(self):
        self.bots = {}
        self.load_bots()

    def load_bots(self):
        try:
            with open('data/bots.json', 'r') as f:
                self.bots = json.load(f)
        except FileNotFoundError:
            self.bots = {}

    def save_bots(self):
        with open('data/bots.json', 'w') as f:
            json.dump(self.bots, f)

    def add_bot(self, token):
        if token not in self.bots:
            # Set the webhook for the new bot
            webhook_url = f"https://sonalitedttttt-372eb29afe86.herokuapp.com/7252944407:AAHwmQeuRTFmFqHcXSmHLWKiuMF4bWfPLWk/webhook"
            response = self.set_webhook(token, webhook_url)
            if response['ok']:
                self.bots[token] = {'webhook_url': webhook_url}
                self.save_bots()  # Save the new bot token
                return True
        return False

    def set_webhook(self, bot_token, webhook_url):
        url = f"https://api.telegram.org/bot7252944407:AAHwmQeuRTFmFqHcXSmHLWKiuMF4bWfPLWk/setWebhook"
        data = {"url": webhook_url}
        return requests.post(url, data=data).json()

    def process_update(self, bot_token, update):
        if 'message' in update:
            message = update['message']['text']
            print(f"Bot {bot_token} received message: {message}")
            # Handle commands like /play, /pause here
            if message.startswith('/play'):
                song_name = message.split(' ', 1)[1]
                print(f"Playing {song_name} on bot {bot_token}")
