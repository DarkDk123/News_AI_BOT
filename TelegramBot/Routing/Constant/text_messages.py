"""
## constant_messages.py

Most of the text message responses are declared here!
"""

from aiogram.utils import markdown as m


def welcome_message(username: str = "User") -> str:

    return f"""Hy, {m.bold(username)}!!
            Welcome to the TeleNews Bot

    This is the only Bot you need to get
    {m.bold("Top News")} from various sources including personalized
    updates.
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
    country_list_str = "\n".join(f"{i}. {item}" for i, item in enumerate(countries, start=1))
    return f"""
    _Select a country :_ 
    
    {country_list_str}
    """

def article_to_str(article: dict) -> str:
    return f"""
## 📰 **Title**: {article.get('title', "NA")}
📅 **Published At**: {article.get('publishedAt')}
👤 **Author**: {article.get('author')}
🔍 **Description**: {article.get('description')}
🔗 **[Read More]({article.get('url', article.get('source', {}).get('name'))})**

"""

def _get_country(id_:int):
    return list(countries.keys())[id_-1]

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
