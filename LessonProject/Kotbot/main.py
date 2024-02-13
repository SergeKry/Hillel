import telebot
from telebot import types
from datetime import date

api_token = '6489865740:AAFBZXIOZR7B8MqT2ilnUzgFU0rrSooTEAc'
bot = telebot.TeleBot(api_token)

status_updated = None
status = '\U0000274c \U0000274c'

markup = types.ReplyKeyboardMarkup()
itembtn_status = types.KeyboardButton('/status')
itembtn_breakfast = types.KeyboardButton('/breakfast')
itembtn_dinner = types.KeyboardButton('/dinner')
markup.row(itembtn_status)
markup.row(itembtn_breakfast, itembtn_dinner)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "\U0001F63A Этот бот не даст тебе быть обманутым\nФилимончик покушал?", reply_markup=markup)


@bot.message_handler(commands=['status'])
def get_status(message):
	if status_updated != date.today():
		global status
		status = '\U0000274c \U0000274c'
	bot.reply_to(message, f'Статус Филимончика: {status}')


@bot.message_handler(commands=['breakfast', 'dinner'])
def get_meal(message):
	global status
	global status_updated
	if message.text == '/breakfast':
		status = '\U00002705 \U0000274c'
		status_updated = date.today()
		bot.send_message(message.from_user.id, f'{status}\nФилимончик позавтракал. Спасибо, что кормишь его \U0001F63B')
	elif message.text == '/dinner':
		status = '\U00002705 \U00002705'
		status_updated = date.today()
		bot.send_message(message.from_user.id, f'{status}\nФилимончик поужинал. Спасибо, что кормишь его \U0001F63B')


@bot.message_handler(content_types=['text'])
def get_keyboard(message):
	bot.send_message(message.from_user.id, f'{status}\n"Филимончик покушал?', reply_markup=markup)


bot.infinity_polling()