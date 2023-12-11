import requests
from telebot import types

class BotMessage:
    def __init__(self, chat_id, text, reply_markup, parse_mode=None):
        self.chat_id = chat_id
        self.text = text
        self.reply_markup = reply_markup
        self.parse_mode = parse_mode



def send_hello(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Get external ip")
    markup.add(btn1)

    return BotMessage(chat_id=chat_id,
                      text="👋 Hello. I am a bot that gives out the external ip of the home network",
                      reply_markup=markup)



def get_external_ip(chat_id):
    try:
        response = requests.get('https://api.ipify.org')
        external_ip = response.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        return BotMessage(chat_id, f"Your external IP address is: {external_ip}",reply_markup=markup)
    except requests.RequestException as e:
        return BotMessage(chat_id, "Error getting external IP", e)


