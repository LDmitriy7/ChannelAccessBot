from aiogram import types

import api
import commands
from loader import dp
from models import documents


@dp.message_handler(commands=commands.START, state='*')
async def welcome(msg: types.Message):
    text = api.get_text(documents.WelcomeText)
    await msg.answer(text)
