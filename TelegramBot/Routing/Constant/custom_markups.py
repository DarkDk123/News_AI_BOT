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
                text="Continue as a Guest", callback_data="menu_callback"
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

registration_markups: dict = {
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
    "location_prompt": types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="India", callback_data="r_country:India"
                ),
                types.InlineKeyboardButton(
                    text="Japan", callback_data="r_country:Japan"
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text="United States", callback_data="r_country:United States"
                ),
                types.InlineKeyboardButton(
                    text="custom", callback_data="r_country_man"
                ),
            ],
        ],
        one_time_keyboard=True,
        input_field_placeholder="You can also Enter here!",
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


# Main Menu Markups
menu_markups: dict = {
    "main_menu": types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Quick Updates", callback_data="quick_updates"
                ),
                types.InlineKeyboardButton(
                    text="Select Topics", callback_data="sel_topics_callback"
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text="Get TOP Headlines", callback_data="show_results_head"
                ),
                types.InlineKeyboardButton(
                    text="Custom Prompt", callback_data="NLP_callback"
                ),
            ],
        ]
    ),
    "sel_topics": types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="AI", callback_data="topic:AI"),
                types.InlineKeyboardButton(text="ML", callback_data="topic:ML"),
            ],
            [
                types.InlineKeyboardButton(text="Tech", callback_data="topic:Tech"),
                types.InlineKeyboardButton(
                    text="Politics", callback_data="topic:Politics"
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text="Custom", callback_data="sel_custom_news_topics"
                )
            ],
            [
                types.InlineKeyboardButton(text="◀️Back", callback_data="menu_callback"),
                types.InlineKeyboardButton(
                    text="Home 🏠", callback_data="menu_callback"
                ),
            ],
        ]
    ),
    "sel_country": types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="India", callback_data="country:India"),
                types.InlineKeyboardButton(text="Japan", callback_data="country:Japan"),
            ],
            [
                types.InlineKeyboardButton(
                    text="United States", callback_data="country:United States"
                ),
                types.InlineKeyboardButton(
                    text="Custom", callback_data="sel_country_man"
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text="◀️Back", callback_data="sel_topics_callback"
                ),
                types.InlineKeyboardButton(
                    text="Home 🏠", callback_data="menu_callback"
                ),
            ],
        ]
    ),
}


# Independent Objects!
def get_response_markup(url: str) -> types.InlineKeyboardMarkup:
    article_buttons = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="🔗 Read More", url=url),
                types.InlineKeyboardButton(
                    text="🚮 Delete", callback_data="delete_article"
                ),
            ]
        ]
    )

    return article_buttons


remove_keyboard = types.ReplyKeyboardRemove()
