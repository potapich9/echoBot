import telebot

bot = telebot.TeleBot("381499912:AAH73wXx4ZJQ75RL_ZgNFf2RVbs4NEWhGv8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()