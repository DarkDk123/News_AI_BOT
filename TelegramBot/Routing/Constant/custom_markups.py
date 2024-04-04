"""
## custom_marktups.py

Custom Keyboard and other markups are declared here!
"""

from aiogram import types


register_or_guest = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="Register for Personalized Updates",
                callback_data="register_callback",
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Continue as a Guest", callback_data="guest_callback"
            )
        ],
    ]
)


destroy_data_or_not = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="Yes",
                callback_data="destroy_yes",
            ),
            types.InlineKeyboardButton(
                text="No", callback_data="destroy_no"
            ),
        ],
    ]
)
