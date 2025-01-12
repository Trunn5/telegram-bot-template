import asyncio

from bot.loader import dp, bot
from bot.routers import user_router, admin_router


dp.include_router(user_router)
dp.include_router(admin_router)


async def main():
    print('Bot is running...')
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
