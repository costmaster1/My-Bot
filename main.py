import telebot
from config import tk_bot

bot = telebot.TeleBot(tk_bot)

# Реакция на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой первый бот c реализацией на Jenkins !!!.../2")

# Реакция на любое текстовое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Бот запущен...")
bot.infinity_polling()
