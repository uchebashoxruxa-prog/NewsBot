from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove
import os
from dotenv import load_dotenv
from base import all_news, get_user, save_user_data
from reply import contact_btn, menu_btn


load_dotenv()
token = os.getenv('TOKEN')

bot = TeleBot(token)


@bot.message_handler(commands=['start', 'help', 'about'])
def commands(message: Message):
    chat_id = message.chat.id
    username = message.from_user.full_name
    if message.text == '/start':
        user = get_user(chat_id)
        if user:
            bot.send_message(chat_id, f'Hi😊 {username}. You can search news by category and find '
                                      f'the newest news. If you are ready, just click the category '
                                      f'which you want to see', reply_markup=menu_btn())
        else:
            bot.send_message(chat_id, f'Hi😊 {username}. This is news Bot. Register sharing with your contact '
                                      f'to use this bot', reply_markup=contact_btn())
    elif message.text == '/help':
        bot.send_message(chat_id, 'For support contact with developer: @shoksruks')
    elif message.text == '/about':
        bot.send_message(chat_id, 'In this bot you can get newest news or just search news by category')


@bot.message_handler(regexp='Politics')
def reaction_politics(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    blocks = all_news('politics')[::-1]
    for block in blocks:
        bot.send_message(chat_id, block)


@bot.message_handler(regexp='Society')
def reaction_society(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    blocks = all_news('society')[::-1]
    for block in blocks:
        bot.send_message(chat_id, block)


@bot.message_handler(regexp='Business')
def reaction_business(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    blocks = all_news('business')[::-1]
    for block in blocks:
        bot.send_message(chat_id, block)


@bot.message_handler(regexp='Technology')
def reaction_technology(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    blocks = all_news('tech')[::-1]
    for block in blocks:
        bot.send_message(chat_id, block)


@bot.message_handler(regexp='Culture')
def reaction_culture(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    blocks = all_news('culture')[::-1]
    for block in blocks:
        bot.send_message(chat_id, block)


@bot.message_handler(regexp='Sport')
def reaction_sport(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    blocks = all_news('sport-en')[::-1]
    for block in blocks:
        bot.send_message(chat_id, block)


@bot.message_handler(regexp='Tourism')
def reaction_tourism(message: Message):
    chat_id = message.chat.id
    msg_id = message.message_id
    bot.delete_message(chat_id, msg_id)
    blocks = all_news('tourism')[::-1]
    for block in blocks:
        bot.send_message(chat_id, block)


@bot.message_handler(regexp='Exit')
def exit_menu(message: Message):
    bot.send_message(message.chat.id, "You exited the menu ✅", reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['contact'])
def get_contact_user(message: Message):
    chat_id = message.chat.id
    username = message.from_user.username
    phone = message.contact.phone_number
    user = get_user(chat_id)
    if not user:
        save_user_data(chat_id, username, phone)
        bot.send_message(chat_id, 'Registration was successfully', reply_markup=ReplyKeyboardRemove())

    bot.send_message(chat_id, f'Hi😊 {username}. You can search news by category and find '
                              f'the newest news. If you are ready, just click the category '
                              f'which you want to see', reply_markup=menu_btn())


bot.infinity_polling()
