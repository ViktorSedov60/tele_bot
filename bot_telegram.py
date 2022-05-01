

from aiogram import  Bot, types
import telebot
from aiogram.dispatcher import Dispatcher
from aiogram. utils import executor

import os

TOKEN = '5321695565:AAFlb2BdS8UfZjNknIKn4sAysymfst8lJag'
# bot = telebot.TeleBot(TOKEN)
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async  def echo_send(message : types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)



executor.start_polling(dp, skip_updates=True)
