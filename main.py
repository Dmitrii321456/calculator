import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

number1 = 0
@bot.message_handler(commands=['start', 'help'])
def start(message):
    markls = []
    bot.reply_to(message, 'Добрый день, это калькулятор введите число:')
    markup = types.InlineKeyboardMarkup(row_width=4, )
    btn1 = types.InlineKeyboardButton('+', callback_data='+')
    btn2 = types.InlineKeyboardButton('-', callback_data='-')
    btn3 = types.InlineKeyboardButton('/', callback_data='/')
    btn4 = types.InlineKeyboardButton('*', callback_data='*')
    for n in range(0, 10):
        markls.append(types.InlineKeyboardButton(f'{str(n)}', callback_data=f'{n}'))

    markls.append(btn1)
    markls.append(btn2)
    markls.append(btn3)
    markls.append(btn4)
    markup.add(markls[0], row_width=4)
    markup.add(markls[1], markls[2], markls[3], row_width=4)
    markup.add(markls[4], markls[5], markls[6], row_width=4)
    markup.add(markls[7], markls[8], markls[9], row_width=4)
    markup.add(markls[10], markls[11], markls[12], markls[13], row_width=4)
    bot.send_message(message.chat.id, text="Давай решим твою задачку!!!", reply_markup=markup)



if __name__ == "__main__":
    bot.infinity_polling()
