from aiogram import Router

from bot.filters.admin import IsAdminFilter


router = Router()

router.message.filter(IsAdminFilter())
router.callback_query.filter(IsAdminFilter())
