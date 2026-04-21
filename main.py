import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Твой токен от @BotFather
API_TOKEN = '8770724203:AAEEi1hHEM9KW89LvNnaxaJBUie8c1_dFdQ'

# Настройка логов (чтобы видеть ошибки)
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я быстрый калькулятор. Просто пришли мне пример (например, 2 + 2 * 5).")

@dp.message_handler()
async def calculate(message: types.Message):
    try:
        # eval — простой способ, но в реальных проектах его нужно ограничивать
        # Здесь мы разрешаем только цифры и знаки операций для безопасности
        allowed_chars = "0123456789+-*/(). "
        if all(char in allowed_chars for char in message.text):
            result = eval(message.text)
            await message.answer(f"Результат: **{result}**", parse_mode="Markdown")
        else:
            await message.answer("Ошибка: используй только числа и знаки + - * /")
    except Exception as e:
        await message.answer(f"Не удалось посчитать. Проверь пример!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)