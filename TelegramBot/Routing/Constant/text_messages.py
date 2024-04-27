"""
## constant_messages.py

Most of the text message responses are declared here!
"""

from aiogram.utils import markdown as m, formatting as fm
from datetime import datetime
from config.settings import ADMIN_USER, BOT_USER


def welcome_message(username: str = "User") -> str:

    return f"""Hy, {m.hbold(username)}!!
            Welcome to the <code>TeleNews</code> Bot

    This is the only Bot you need to get
    <b>"Top News"</b> from various sources including personalized
    updates.

    {m.hblockquote("You can also provide NLP queries directly!!")}
    """


def help_message() -> str:
    commands_list = (
        "/start, /restart - Start/Restart the Bot Chat\n",
        "/help - Show this help message\n",
        "/destroy - Destroy User Data\n",
        "/sources - List of Sources for custom query inputs\n",
        "/support - Support Our Project\n",
        "/mydetails - Get User's saved details\n",
        "/register - Invoke Registration Process\n",
        "/clear - Clear Chat Completely\n"
    )
    return f"""
📃 <b>List of Commands</b>

{fm.as_numbered_list(*commands_list, fmt="{}. ").as_html()}
"""


def details_message(data: dict) -> str:
    return f"""
<b>Hey {data.get('name')}!</b>

<b><i>💝 You're interested in following topics :</i></b>
{fm.as_marked_list(*data.get('topics'), marker="  → ").as_html()}
        
<b>🏠 You're from : </b> {data.get('country')}
"""


def reg_init(username: str) -> str:
    return f"""
<b>Registration Process Started!! 🌟</b>
        
👋 Hey, {m.hbold(username)}!
    Is this correct name for you??
"""


def locations() -> str:
    return """
        <b>Please select your country!!</b>
        """


def sources(scr: list) -> str:
    result = m.hbold(
        f"📃 This are some of the Available Sources: \n\n"
        + f"{fm.as_numbered_list(*scr, fmt='{}. ').as_html()}"
    )

    return result


def support() -> str:
    return f"""
    {m.hblockquote("Please Support me At following: 💝")}
    """


def sel_countries():
    return f"""
    <b>Select a country : </b> 

    {fm.as_numbered_list(*countries, fmt="({}). ").as_html()}
    """


def no_quick():
    return "<b><i>⚠️ Quick Updates is Available for Registered Users Only! ⚠️</i></b>"


def api_rate_limited() -> str:
    return "<b>😢 Sorry, API rate limit exceeded, Try after few hours⏳</b>"


def query_template(user_query: str):
    return f"""
    You role:
        You're name is `TeleNews` Bot to search from millions of articles and you're sole purpose is to find articles relevant to user query"
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
{m.hide_link(url)} {m.hide_link(img_url if img_url.startswith("http") else "https:/" + img_url)}
{m.hblockquote("Article : " + index)}
_____________________________________

<b>{m.hcode("📰 Title ↓")}</b> {m.hblockquote("👉  " + title)}
    
<b><code>🔍 Description</code></b>
{m.hblockquote("→  " + description)}


<b>📅 Published At:</b> {date}
<b>🗣️ <code>by</code></b> {author}
_____________________________________ 
💖 {BOT_USER}
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
