import asyncio

from bot.loader import dp, bot
from bot.routers import user_router, admin_router, error_router


dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(error_router)


async def main():
    print('Bot is running...')

    # setup default commands menu 
    from bot.keyboards.default_menu import menu
    await bot.set_my_commands(menu)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
