from aiogram import Bot, Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6663947089:AAF1hJBzGNczybEdEscOmpaI_6EmEgey6rc')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Відкрити веб сторінку', web_app=WebAppInfo(url='https://www.mcdonalds.com/ua/uk-ua.html')))
    await message.answer('Вітаю', reply_markup=markup)

executor.start_polling(dp)
