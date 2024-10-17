from flask import Flask, request
from bot_manager import BotManager

app = Flask(__name__)
bot_manager = BotManager()

@app.route('/register_bot', methods=['POST'])
def register_bot():
    data = request.get_json()
    bot_token = data.get('token')
    
    if bot_token:
        # Register the new bot and set the webhook
        result = bot_manager.add_bot(bot_token)
        if result:
            return {"status": "success", "message": "Bot registered successfully"}, 200
        return {"status": "error", "message": "Webhook setup failed"}, 400
    return {"status": "error", "message": "Invalid token"}, 400

# Webhook handler route for all registered bots
@app.route('/<bot_token>/webhook', methods=['POST'])
def bot_webhook(bot_token):
    update = request.get_json()
    bot_manager.process_update(bot_token, update)
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(debug=True)
