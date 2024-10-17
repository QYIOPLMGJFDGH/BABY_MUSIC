def handle_webhook(bot_token, update):
    if 'message' in update:
        message = update['message']['text']
        # Bot-specific logic
        if message.startswith('/play'):
            song_name = message.split(' ', 1)[1]
            print(f"Playing {song_name} for bot {bot_token}")
        elif message.startswith('/pause'):
            print(f"Pausing music for bot {bot_token}")
