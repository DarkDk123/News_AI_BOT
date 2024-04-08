"""
## custom_marktups.py

Custom Keyboard and other markups are declared here!
"""

from aiogram import types
from config import settings

# Register or continue as guest
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


# Destroy user data or not?
destroy_data_or_not = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="Yes",
                callback_data="destroy_yes",
            ),
            types.InlineKeyboardButton(text="No", callback_data="destroy_no"),
        ],
    ]
)

# Support markup
support = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="➡️ LinkedIn", url=settings.LINKEDIN_URL),
            types.InlineKeyboardButton(text="🚀 GitHub", url=settings.GITHUB_URL),
        ]
    ]
)

# Registration Process

registration_markups = {
    "correct_name_or_not": types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Yes", callback_data="correct_name_yes"
                ),
                types.InlineKeyboardButton(text="No", callback_data="correct_name_no"),
            ]
        ]
    ),
    "location_prompt": types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="India"), types.KeyboardButton(text="Pakistan")],
            [
                types.KeyboardButton(text="USA"),
                types.KeyboardButton(
                    text="Use Current Location", request_location=True
                ),
            ],
        ],
        one_time_keyboard=True,
    ),
    "re-register": types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Re-register", callback_data="re-register_callback"
                ),
                types.InlineKeyboardButton(
                    text="NO, Leave", callback_data="destroy_no"
                ),
            ]
        ]
    ),
}

# Independent Objects!

remove_keyboard = types.ReplyKeyboardRemove()