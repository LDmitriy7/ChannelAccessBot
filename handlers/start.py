from aiogram import types

import commands
import keyboards as kb
import texts
from loader import dp
from models import documents


@dp.message_handler(commands=commands.START, state='*')
async def welcome(msg: types.Message):
    # text = api.get_text(documents.WelcomeText)
    # await msg.answer(text)
    await msg.answer(texts.welcome, disable_web_page_preview=True)
    await msg.answer(texts.ask_to_choose_tariff, reply_markup=kb.Tariffs([documents.tariff1]))
