from aiogram import types

async def handle_start(m: types.Message):
    await m.answer("hello")