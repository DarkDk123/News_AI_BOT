"""
## custom_marktups.py

Custom Keyboard and other markups are declared here!
"""

from aiogram import types

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


# Registration Process | Correct name or not

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
        resize_keyboard=True,
        input_field_placeholder="Select One of following Countries",
    ),
}
