from googletrans import Translator
from button import *
from aiogram.types import Message, CallbackQuery
# pip install googletrans==3.1.0a0

import logging

from aiogram import Bot, Dispatcher, executor, types

tr = Translator()

API_TOKEN = 'Bu Yerga Token yoziladi'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply("Hi!\nMen tarjimon Botman!\nSo'zni Yuboring: ")

@dp.message_handler()
async def echo(message: types.Message):
  global word
  word = message.text
  await message.answer("Tilni tanlang...👇", reply_markup=til)

@dp.callback_query_handler(text="en")
async def english(call: CallbackQuery):
  display=tr.translate(word,dest="en")
  await call.message.answer(display.text)


@dp.callback_query_handler(text="ru")
async def russian(call: CallbackQuery):
  display=tr.translate(word,dest="ru")
  await call.message.answer(display.text)

@dp.callback_query_handler(text="tr")
async def turkish(call: CallbackQuery):
  display=tr.translate(word,dest="tr")
  await call.message.answer(display.text)

@dp.callback_query_handler(text="fr")
async def french(call: CallbackQuery):
  display=tr.translate(word,dest="fr")
  await call.message.answer(display.text)

@dp.callback_query_handler(text="uz")
async def uzbek(call: CallbackQuery):
  display=tr.translate(word,dest="uz")
  await call.message.answer(display.text)

@dp.callback_query_handler(text="de")
async def german(call: CallbackQuery):
  display=tr.translate(word,dest="de")
  await call.message.answer(display.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)