from aiogram import types

import commands
import keyboards as kb
import models.models
import texts
from loader import dp
from models import models


@dp.message_handler(commands=commands.START, state='*')
async def welcome(msg: types.Message):
    await msg.answer(texts.welcome, disable_web_page_preview=True)

    reply_markup = kb.Tariffs(models.tariffs)
    await msg.answer(texts.ask_to_choose_tariff, reply_markup=reply_markup)
