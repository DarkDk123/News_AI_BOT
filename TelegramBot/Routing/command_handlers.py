"""
## commands.py

This file Routes all the commands gives to BOT
using `command_router` from `routers.py`.
"""

from multiprocessing.connection import answer_challenge
from aiogram import filters, types, F
from .Constant import text_messages as msg

from .routers import command_router


# Start/Restart the Conversation
@command_router.message(filters.Command("start", "restart", ignore_case=True))
async def start(message: types.Message) -> None:
    await message.answer(
        msg.welcome_message(username=message.from_user.first_name),  # type: ignore
    )


# Help command : shows list of commands
@command_router.message(filters.Command("help", ignore_case=True))
async def help_(message: types.Message) -> None:
    await message.answer(msg.help_message())


# Destroys User Data if registered.
@command_router.message(filters.Command("destroy", ignore_case=True))
async def destroy(message: types.Message) -> None:
    await message.answer(
        """
        Do you really want to destroy your Data??
        You will need to re-register!
        """
    )


# Get list of available News Sources.
@command_router.message(filters.Command("sources", ignore_case=True))
async def news_sources(message: types.Message) -> None:
    await message.answer("This will show available news sources for custom inputs.")


# Options to support this project.
@command_router.message(filters.Command("support", ignore_case=True))
async def support(message: types.Message) -> None:
    await message.answer("This will show Project links to like and support")


# Get the User's saved details.
@command_router.message(filters.Command("mydetails", ignore_case=True))
async def mydetails(message: types.Message) -> None:
    await message.answer("If user is registered, it will show it's details.")


# Invoke Registration Process | Or Register the User
@command_router.message(filters.Command("register", ignore_case=True))
async def register(message: types.Message) -> None:
    await message.answer("This registers/re-registers the user.")
