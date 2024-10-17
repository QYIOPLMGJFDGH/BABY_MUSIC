from telebot import TeleBot

# Pehla bot (original bot) ka token
MAIN_BOT_TOKEN = "7638229482:AAEFl9_9Vmrl9MDDmsA6uipDH1Hc6HcjGHc"

# Original bot instance
main_bot = telebot.TeleBot(MAIN_BOT_TOKEN)

# Clone command
@main_bot.message_handler(commands=['clone'])
def clone_bot(message):
    try:
        # User se bot token extract karna
        bot_token = message.text.split()[1]
        
        # Naya bot instance create karna with user provided token
        cloned_bot = telebot.TeleBot(bot_token)
        
        # Saare handlers aur functionality clone karna
        @cloned_bot.message_handler(func=lambda msg: True)
        def handle_all_messages(msg):
            # Yaha aap original bot ki functionality clone kar sakte hain
            cloned_bot.send_message(msg.chat.id, "Yeh bot aapke original bot ka clone hai!")
        
        # Cloned bot ko start karna
        cloned_bot.polling()
        
        # Confirmation dena ki bot successfully clone ho gaya
        main_bot.send_message(message.chat.id, "Bot successfully cloned!")
    
    except Exception as e:
        main_bot.send_message(message.chat.id, f"Error: {str(e)}")

# Pehla bot ko start karna
main_bot.polling()
