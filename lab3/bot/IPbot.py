import telebot


from api.bot_api import send_hello,get_external_ip


bot = telebot.TeleBot ('6707286926:AAGsDlw0HPgECJoUwA6a3wfXogkOQNvBv2Q')



@bot.message_handler(commands=['start'])
def start(message):
    print(f'new user{message}')
    chat_id = message.chat.id
    bot_message = send_hello(chat_id)

    bot.send_message(chat_id=bot_message.chat_id, text=bot_message.text, reply_markup=bot_message.reply_markup)

@bot.message_handler(func=lambda message: message.text == "Get external ip")
def get_ip(message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    user_name = message.from_user.first_name
    print(f'received request from user {user_id} {user_name} {user_fullname}')
    chat_id = message.chat.id
    bot_message = get_external_ip(chat_id)

    bot.send_message(chat_id=bot_message.chat_id, text=bot_message.text, reply_markup=bot_message.reply_markup)

print('bot is starting')
bot.polling(none_stop=True, interval=1)
