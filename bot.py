import os
import telebot
from flask import Flask

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)
server = Flask(name)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men Render bulutli platformasida ishlayapman. Menga xabar yozing, men uni tahlil qilaman!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    analysis = f"Siz yozdingiz: {text}\nUzunligi: {len(text)} ta belgi."
    bot.reply_to(message, analysis)

@server.route("/")
def webhook():
    return "Bot is running!", 200

if name == "main":
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
