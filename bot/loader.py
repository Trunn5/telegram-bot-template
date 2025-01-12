from aiogram import Dispatcher, Bot

from bot import config


dp = Dispatcher()
bot = Bot(token=config.bot_token)

