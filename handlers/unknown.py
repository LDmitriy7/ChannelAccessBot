from aiogram import types

import texts
from loader import dp


@dp.message_handler()
async def unknown(msg: types.Message):
    await msg.answer(texts.unknown)
