import telebot

# Замени 'ВАШ_ТОКЕН' на токен от @BotFather
bot = telebot.TeleBot('8770724203:AAEEi1hHEM9KW89LvNnaxaJBUie8c1_dFdQ')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Пришли мне пример, например: 2 + 2")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # eval вычисляет строку как математическое выражение
        # Ограничим символы для безопасности
        allowed_chars = "0123456789+-*/. "
        if all(char in allowed_chars for char in message.text):
            result = eval(message.text)
            bot.reply_to(message, f"Результат: {result}")
        else:
            bot.reply_to(message, "Я принимаю только цифры и знаки + - * /")
    except Exception:
        bot.reply_to(message, "Ошибка в примере!")

bot.polling(none_stop=True)
