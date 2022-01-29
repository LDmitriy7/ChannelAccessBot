import logging

import mongoengine as me
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage

import config
from api import Wallet

me.connect(
    db=config.Database.name,
    username=config.Database.username,
    password=config.Database.password,
    host=config.Database.host,
    port=config.Database.port,
    authentication_source=config.Database.auth_source,
)

storage = MongoStorage(
    db_name=config.Database.name,
    username=config.Database.username,
    password=config.Database.password,
    host=config.Database.host,
    port=config.Database.port,
)

bot = Bot(config.Bot.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(filename=config.Log.file, level=config.Log.level)

wallet = Wallet(config.Wallet.pubkey)
