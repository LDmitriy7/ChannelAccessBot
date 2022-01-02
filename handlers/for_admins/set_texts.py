from aiogram import types

import commands
import config
from loader import dp
from models import documents


@dp.message_handler(commands=commands.SET_WELCOME_TEXT, user_id=config.Users.admins_ids)
async def set_welcome_text(msg: types.Message):
    documents.WelcomeText(value=msg.get_args()).save()
    await msg.answer('done')
