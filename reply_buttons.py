from telebot import types

def buttons():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add("1–3", "4–6", "7–9", "10")
        return markup