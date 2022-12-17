import telebot
import requests
from telebot import types

bot = telebot.TeleBot('5104380438:AAG5TWkS_gFhZ0lsQU6VjfLLsdfeKI9EAvA')
appid = 'dd52a6639077c9b9dcf40d5528083fab'
s_city = "Moscow (RU)"
city_id = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Погода")
    btn2 = types.KeyboardButton("Температура")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Я родился!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    try:
        res = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={appid}&lang=ru&units=metric")
        data = res.json()
        if ((not data) or (str(data['cod']) == '404')):
            raise Exception('Page not Found 404')
    except Exception as e:
        bot.send_message(message.chat.id, text=f"Сервер упал :(\nОшибка: {e}")
        return

    if (message.text == "Погода"):
        weather = data['list'][0]['weather'][0]['description'].title()
        bot.send_message(message.chat.id, text=weather)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Назад")
        markup.add(back)

    elif (message.text == "Температура"):
        temp = 'Температура ' + str(data['list'][0]['main']['temp']) + '°C'
        feels_temp = 'Ощущается как ' + str(data['list'][0]['main']['feels_like']) + '°C'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text=temp + "\n" + feels_temp, reply_markup=markup)
        back = types.KeyboardButton("Назад")
        markup.add(back)

    elif (message.text == "Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Погода")
        button2 = types.KeyboardButton("Температура")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню, чем могу помочь?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Не знаю такого..")


bot.polling(none_stop=True)