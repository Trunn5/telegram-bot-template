from aiogram import types
from aiogram.filters import BaseFilter

from bot import config


class IsAdminFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in config.admin_list
    
