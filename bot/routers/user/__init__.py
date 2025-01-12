from aiogram import Router

router = Router()

from bot.routers.user.start import handle_start


router.message.register(handle_start, ...)
