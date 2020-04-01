import telebot
import health_news


bot = telebot.TeleBot('ENTER YOUR KEY')
all_users = {}


keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Следующая новость')


@bot.message_handler(commands=['start'])
def start_message(mess):
    bot.send_message(mess.chat.id, 'Привет, я рассказываю актуальные новости.Используя https://newsapi.org/'
                     , reply_markup=keyboard)
    all_users[mess.chat.id] = health_news.RussiaNews()


@bot.message_handler(content_types='text')
def send_text(mess):
    if mess.chat.id not in all_users:
        all_users[mess.chat.id] = health_news.RussiaNews()

    if mess.text.lower() == 'следующая новость':
        bot.send_message(mess.chat.id, all_users[mess.chat.id].fresh_new(), reply_markup=keyboard)
        all_users[mess.chat.id].next_new()
    else:
        bot.send_message(mess.chat.id, 'Используйте клавиатуру', reply_markup=keyboard)


bot.polling()
