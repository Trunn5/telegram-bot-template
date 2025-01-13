from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

from bot import config

# https://docs.aiogram.dev/en/v3.17.0/dispatcher/finite_state_machine/storages.html
storage = MemoryStorage()

dp = Dispatcher(storage=storage)
bot = Bot(token=config.bot_token)

