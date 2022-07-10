from email import message
import telebot
from telebot import types
import random
import xlrd

bot = telebot.TeleBot('5509572803:AAFYe_oXq7xN75QDSDWngEIzTZPJ_w49plY')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	stic = open('/home/kuba/Desktop/pyBot/stic/welcome.webp', 'rb')

	# клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	but1 = types.KeyboardButton("Цитата про успех")
	but2 = types.KeyboardButton("Подсознательное богатство")
	markup.add(but1, but2)

	bot.reply_to(message, "Здравствуй, {0.first_name}\nСмотрю, Вы сказочно богатый человек :)".format(message.from_user),parse_mode='html',reply_markup=markup)
	bot.send_sticker(message.chat.id,stic)
	

@bot.message_handler(func=lambda message: True)
def menu(message):
	if message.chat.type == 'private':
		if message.text == "Цитата про успех":
            
			#достаём циататы из ворда
			stic3 = open('/home/kuba/Desktop/pyBot/stic/itachi2.webp', 'rb')
			rb = xlrd.open_workbook('/home/kuba/Desktop/pyBot/citat/citata.xls', formatting_info=True)
			sheet = rb.sheet_by_index(0)
			for rownum in range(sheet.nrows):
				rand = int(random.randint(0,rownum))
				row = sheet.row_values(rand)
			bot.send_message(message.chat.id, row)
			bot.send_sticker(message.chat.id,stic3)

		elif message.text == "Подсознательное богатство":

			#достаём циататы из ворда
			stic4 = open('/home/kuba/Desktop/pyBot/stic/citata.webp', 'rb')
			rb = xlrd.open_workbook('/home/kuba/Desktop/pyBot/citat/reache.xls', formatting_info=True)
			sheet = rb.sheet_by_index(0)
			for rownum in range(sheet.nrows):
				rand = int(random.randint(0,rownum))
				row = sheet.row_values(rand)
			bot.send_message(message.chat.id, row)
			bot.send_sticker(message.chat.id,stic4)

		elif message.text.lower() == 'привет':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic = open('/home/kuba/Desktop/pyBot/stic/welcome.webp', 'rb')
			bot.send_message(message.chat.id, "Привет, {0.first_name}\n, как ты? :)".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic)
		
		elif message.text.lower() == 'пока':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic5 = open('/home/kuba/Desktop/pyBot/stic/poka.webp', 'rb')
			bot.send_message(message.chat.id, "Удачного дня Вам - {0.first_name}\n и до новой встречи ;)".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic5)

		elif message.text.lower() == 'хорошо':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic6 = open('/home/kuba/Desktop/pyBot/stic/itachi2.webp', 'rb')
			bot.send_message(message.chat.id, "Отлично, {0.first_name}\nя очень рад за Вас :)".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic6)
		
		elif message.text.lower() == 'устал':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic7 = open('/home/kuba/Desktop/pyBot/stic/itachi3.webp', 'rb')
			bot.send_message(message.chat.id, "Работа работой - {0.first_name}\n, а отдохнуть надо ;)".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic7)

		elif message.text.lower() == 'как ты':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic8 = open('/home/kuba/Desktop/pyBot/stic/itachi4.webp', 'rb')
			bot.send_message(message.chat.id, "{0.first_name}\n, думаю я лучше чем вчера :)".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic8)
		
		elif message.text.lower() == 'не получается':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic9 = open('/home/kuba/Desktop/pyBot/stic/reacher.webp', 'rb')
			bot.send_message(message.chat.id, "отдохни {0.first_name}\n, потом еще попробуешь ;)".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic9)

		elif message.text.lower() == 'спать хочу':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic5 = open('/home/kuba/Desktop/pyBot/stic/itachi1.webp', 'rb')
			bot.send_message(message.chat.id, "поспи {0.first_name}\n, не мучай себя ;)".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic5)

		elif message.text.lower() == 'спасибо':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic6 = open('/home/kuba/Desktop/pyBot/stic/itachi5.webp', 'rb')
			bot.send_message(message.chat.id, "и Вам - {0.first_name}\n, большое спасибо ;)".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic6)

		elif message.text.lower() == 'команды':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stic7 = open('/home/kuba/Desktop/pyBot/stic/citata.webp', 'rb')
			bot.send_message(message.chat.id, "/start \nпривет  \nпока  \nхорошо  \nкак ты  \nустал  \nне получается  \nспасибо  \nкоманды \nспать хочу".format(message.from_user),parse_mode='html',reply_markup=markup)
			bot.send_sticker(message.chat.id,stic7)

bot.polling(none_stop=True)