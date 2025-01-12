from aiogram import Router, types

from bot.loader import bot
from bot.config import admin_list

router = Router()

@router.errors()
async def handle_error(exception: types.ErrorEvent):
    for admin in admin_list:
        await bot.send_message(admin, "Error:\n" + str(exception))
