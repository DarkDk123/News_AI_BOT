"""
## commands.py

This file Routes all the commands gives to BOT
using `command_router` from `routers.py`.
"""

from aiogram import filters, types, F
from aiogram.utils import markdown

from .routers import command_router


@command_router.message(filters.Command("start"))
async def start(message: types.Message) -> None:
    await message.answer(f"Hy, {markdown.bold(message.from_user.first_name)}\nNice to see you")  # type: ignore


@command_router.message(filters.Command("help"))
async def help(message: types.Message) -> None:
    await message.answer("I'm willing to help you, but I can't!! 😅")


@command_router.message(F.text.casefold() == "am i admin?")
async def admin(message: types.Message) -> None:
    # Needs to change, read docs!
    if filters.IS_ADMIN:
        await message.answer("Yes, you're an Admin")
    else:
        await message.answer("No bro!")

    await message.answer(f"{filters.IS_ADMIN=}")
