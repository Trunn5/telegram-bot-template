from aiogram import Router
from aiogram import filters

router = Router()

from bot.routers.user.start import handle_start


router.message.register(handle_start, filters.Command("start"))




