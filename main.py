import telebot
from secrets import secrets
from telebot import types
import random # для выбора случайного комплимента
from compliments import compliments # коллекция комплиментов

token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)

# хендлер и функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("Старт")
    action_button = types.KeyboardButton("Комплимент")
    markup.add(start_button, action_button)
    bot.send_message(message.chat.id, text="Привет, {0.first_name} \nВоспользуйся кнопками".format(message.from_user), reply_markup=markup)

# хендлер для обработки нажатий кнопок
@bot.message_handler(content_types=['text'])
def buttons(message):
    if (message.text == "Старт"):
        bot.send_message(message.chat.id, text="Я могу поддержать тебя и поднять настроение. Просто попроси об этом")
    elif (message.text == "Комплимент"):
        bot.send_message(message.chat.id, text=f"{random.choice(compliments)}")
    else:
        bot.send_message(message.chat.id, text="Я могу отвечать только на нажатие кнопок")

# бесконечное выполнение кода
bot.polling(none_stop=True, interval=0)
