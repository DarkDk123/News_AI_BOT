"""
## constant_messages.py

Most of the text message responses are declared here!
"""

from aiogram.utils import markdown as m
from datetime import datetime
from config.settings import ADMIN_USER


def welcome_message(username: str = "User") -> str:

    return f"""Hy, {m.bold(username)}!!
            Welcome to the TeleNews Bot

    This is the only Bot you need to get
    {m.bold("Top News")} from various sources including personalized
    updates.

    >>>> ***You can also provide NLP queries directly!!***
    """


def help_message() -> str:
    return f"""
            📃 *List of Commands*
    
    1. /start, /restart - Start/Restart the Bot Chat

    2. /help - Show this help message

    3. /destroy - Destroy User Data

    4. /sources - List of Sources for custom query inputs

    5. /support - Support Our Project

    6. /mydetails - Get User's saved details

    7. /register - Invoke Registration Process.
    """


def details_message(data: dict) -> str:
    return f"""
        *Hey {data.get('name')}!*

        ### You're interested topics are:
                {data.get('topics')}
        
        ### You're from : 
                {data.get('country')}
        """


def reg_init(username: str) -> str:
    return f"""
        ##Registration Process Started!! 🌟
        
        👋 Hey, {username}!
        Is this correct name for you??
        """


def locations() -> str:
    return """
        *Please select your country!!*
        """


def sources(scr: list) -> str:
    result = "This are some of the Available Sources: \n"
    for i, s in enumerate(scr, 1):
        result += f"{i}. {s} \n"

    return result


def support() -> str:
    return """
    Please Support me At following: 💝
    """


def sel_countries():
    country_list_str = "\n".join(
        f"{i}. {item}" for i, item in enumerate(countries, start=1)
    )
    return f"""
    _Select a country :_ 
    
    {country_list_str}
    """


def no_quick():
    return "***⚠️ _Quick Updates_ is Available for Registered Users Only! ⚠️***"


def api_rate_limited() -> str:
    return "😢 Sorry, API rate limit exceeded, Try after few hours⏳"


def query_template(user_query: str):
    return f"""
    You role:
        You're name is `TeleBot` to search from millions of articles and you're sole purpose is to find articles relevant to user query"
        Remember you can just search for articles based on user query.
        You're developed in India by {ADMIN_USER} (your developer), so you are Indian!

    User Query: "{user_query}"

    Based on the above, TeleBot, Answer.
    """


def article_to_str(article: dict, index: str) -> str:
    title = article.get("title", "NA")
    description = article.get("description", "NA")
    url = article.get("url", article.get("source", {}).get("name"))
    img_url = article.get("urlToImage", "")
    date = _format_time_str(article.get("publishedAt"))
    author = article.get("author") if article.get("author") else "Someone!"

    return f"""
*{index}*
––––––––––––––––––––––
**`📰 Title: `** {title}
    
🔍 **`Description`**
→ {description}


📅  **Published At**: {date}
🗣️ **`by`** {author}

––––––––––––––––––––[-]({url})[-]({img_url if img_url.startswith("http") else "https:/" + img_url})
"""


def _get_country(id_: int):
    return list(countries.keys())[id_ - 1]


def _format_time_str(date_string) -> str:
    try:
        date_obj = datetime.strptime(date_string[:-1], "%Y-%m-%dT%H:%M:%S")
        return date_obj.strftime("%d %b, %Y")
    except:
        return "sometime!"


## Countries data dictionary
countries = {
    "Argentina": "ar",
    "Australia": "au",
    "Brazil": "br",
    "Canada": "ca",
    "Germany": "de",
    "France": "fr",
    "United Kingdom": "gb",
    "Ireland": "ie",
    "India": "in",
    "Italy": "it",
    "Netherlands": "nl",
    "Norway": "no",
    "Russia": "ru",
    "Saudi Arabia": "sa",
    "Sweden": "se",
    "United States": "us",
    "South Africa": "za",
}


## Languages allowed
languages = [
    "ar",
    "de",
    "en",
    "es",
    "fr",
    "he",
    "it",
    "nl",
    "no",
    "pt",
    "ru",
    "sv",
    "ud",
    "zh",
]
emoji_indexes = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]
