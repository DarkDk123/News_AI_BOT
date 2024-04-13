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


def _get_country(id_:int):
    return list(countries.keys())[id_] #type: ignore

## Countries data dictionary
countries = {
    "United Arab Emirates": "ae",
    "Argentina": "ar",
    "Austria": "at",
    "Australia": "au",
    "Belgium": "be",
    "Bulgaria": "bg",
    "Brazil": "br",
    "Canada": "ca",
    "Switzerland": "ch",
    "China": "cn",
    "Colombia": "co",
    "Cuba": "cu",
    "Czech Republic": "cz",
    "Germany": "de",
    "Egypt": "eg",
    "France": "fr",
    "United Kingdom": "gb",
    "Greece": "gr",
    "Hong Kong": "hk",
    "Hungary": "hu",
    "Indonesia": "id",
    "Ireland": "ie",
    "Israel": "il",
    "India": "in",
    "Italy": "it",
    "Japan": "jp",
    "South Korea": "kr",
    "Lithuania": "lt",
    "Latvia": "lv",
    "Morocco": "ma",
    "Mexico": "mx",
    "Malaysia": "my",
    "Nigeria": "ng",
    "Netherlands": "nl",
    "Norway": "no",
    "New Zealand": "nz",
    "Philippines": "ph",
    "Poland": "pl",
    "Portugal": "pt",
    "Romania": "ro",
    "Serbia": "rs",
    "Russia": "ru",
    "Saudi Arabia": "sa",
    "Sweden": "se",
    "Singapore": "sg",
    "Slovenia": "si",
    "Slovakia": "sk",
    "Thailand": "th",
    "Turkey": "tr",
    "Taiwan": "tw",
    "Ukraine": "ua",
    "United States": "us",
    "Venezuela": "ve",
    "South Africa": "za",
}
