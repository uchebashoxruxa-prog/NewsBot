from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menu_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='🏛️ Politics')
    btn2 = KeyboardButton(text='🏘️ Society')
    btn3 = KeyboardButton(text='💼 Business')
    btn4 = KeyboardButton(text='🤖 Technology')
    btn5 = KeyboardButton(text='🏺 Culture')
    btn6 = KeyboardButton(text='🏃‍♂️ Sport')
    btn7 = KeyboardButton(text='✈️ Tourism')
    btn8 = KeyboardButton(text='❌ Exit')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    return markup


def contact_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Share contact 📱📞', request_contact=True)
    markup.add(btn)

    return markup
