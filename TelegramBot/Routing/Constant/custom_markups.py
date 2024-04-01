"""
## custom_marktups.py

Custom Keyboard and other markups are declared here!
"""

from aiogram import types


register_or_guest = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="Register for Personalized Updates", callback_data="register_callback"
            )
        ],
        [types.InlineKeyboardButton(text="Continue as a Guest", callback_data="guest_callback")],
    ]
)
