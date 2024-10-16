import requests
import time

# Aapke bot ka token
mera_bot_token = "Aapke_Original_Bot_Token"
bot_api_url = f"https://api.telegram.org/bot{mera_bot_token}/"

def bot_info_lete_hain(token):
    """Forwarded token ka istemal karke bot ka info prapt karna."""
    response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
    return response.json()

def clone_commands(forwarded_token):
    """Naye bot me commands set karna."""
    commands = [
        {"command": "start", "description": "Bot ko shuru karo"},
        {"command": "help", "description": "Madad pao"},
    ]
    response = requests.post(f"https://api.telegram.org/bot{forwarded_token}/setMyCommands", json={"commands": commands})
    if response.json().get("ok"):
        print("Commands successfully naye bot me set ho gayi.")
    else:
        print("Commands set karne me dikkat hui.")

def bot_clone_karo(forwarded_token):
    """Aapke bot ke commands ko naye bot me clone karna."""
    bot_info = bot_info_lete_hain(forwarded_token)
    if bot_info.get("ok"):
        bot_ka_naam = bot_info["result"]["first_name"]
        print(f"Naye bot me cloning ki ja rahi hai: {bot_ka_naam}")
        clone_commands(forwarded_token)
    else:
        print("Galat bot token hai")

def handle_updates(update):
    """Aaye hue messages ko handle karna."""
    message = update.get('message')
    if message and 'text' in message:
        forwarded_token = message['text']
        if forwarded_token.startswith("123456789:"):  # Ye condition check karta hai agar forwarded message ek token hai
            print(f"Token receive hua: {forwarded_token}")
            bot_clone_karo(forwarded_token)
        else:
            print("Invalid token format")

def get_updates(offset=None):
    """Telegram se nayi updates le kar unhe handle karna."""
    url = bot_api_url + "getUpdates"
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

def main():
    """Bot ko continuously updates check karne ke liye."""
    offset = None
    while True:
        updates = get_updates(offset)
        if updates.get("ok") and updates.get("result"):
            for update in updates["result"]:
                offset = update["update_id"] + 1
                handle_updates(update)
        time.sleep(1)

if __name__ == "__main__":
    main()
