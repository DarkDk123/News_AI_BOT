"""
## bot_instance.py

This file contains the Single `BOT` instance used in the Project!
"""

# _________IMPORTS_____________
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties


import os


# Default Bot Properties
default_bot_properties = DefaultBotProperties(
    parse_mode="Markdown", disable_notification=False
)

BOT = Bot(os.environ["TELEGRAM_BOT_TOKEN"], default=default_bot_properties)
