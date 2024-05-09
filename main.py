import telebot

from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('7031635922:AAEwZ1BM3S9A2j4Ja8Z3C2t8K6ED3lh4654')

# Обработчик команды '/start', который запускает меню
@bot.message_handler(commands=['start'])
def menu(message):
    # Создание клавиатуры
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # Добавление кнопок
    markup.row('/start', '/help')
    markup.row('/settings', '/profile')
    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, "Выберите команду из меню:", reply_markup=markup)

# Обработчик команды '/help'
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Это раздел помощи. Здесь вы можете получить информацию о боте.")

# Обработчик команды '/settings'
@bot.message_handler(commands=['settings'])
def settings(message):
    bot.send_message(message.chat.id, "Это настройки вашего профиля.")

# Обработчик команды '/profile'
@bot.message_handler(commands=['profile'])
def profile(message):
    bot.send_message(message.chat.id, "Это ваш профиль.")

# Запуск бота
bot.polling()