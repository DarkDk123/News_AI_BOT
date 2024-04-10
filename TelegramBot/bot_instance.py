"""
## bot_instance.py

This file contains the Single `BOT` instance used in the Project!
"""

# _________IMPORTS_____________
from aiogram import Bot, types
from aiogram.client.default import DefaultBotProperties


import os


# Default Bot Properties
default_bot_properties = DefaultBotProperties(
    parse_mode="Markdown", disable_notification=False
)

BOT = Bot(os.environ["TELEGRAM_BOT_TOKEN"], default=default_bot_properties)


async def menu_buttons(BOT: Bot) -> None:
    await BOT.set_my_commands(
        commands=[
            types.BotCommand(command="/start", description="🚀 Starts the bot"),
            types.BotCommand(command="/restart", description="🔁 Re-starts the bot"),
            types.BotCommand(command="/help", description="🙏 Show Help Message"),
            types.BotCommand(command="/sources", description="🗞️ Get News Sources"),
            types.BotCommand(command="/destroy", description="💥 Destroy user's Data📝"),
            types.BotCommand(command="/mydetails", description="📃 Show User details"),
            types.BotCommand(command="/register", description="👤 Invoke Registration📝"),
            types.BotCommand(command="/support", description="👍 Support Me 💁‍♂️"),
        ]
    )