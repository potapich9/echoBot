import telebot

bot = telebot.TeleBot("381499912:AAH73wXx4ZJQ75RL_ZgNFf2RVbs4NEWhGv8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi, how are you doing?")

@bot.message_handler(content_types=["sticker"])
def send_welcome1(message):
	chat_id = message.chat.id
	bot.send_sticker(chat_id, message.sticker.file_id)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.polling()