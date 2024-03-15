from newsapi import NewsApiClient
from newsdataapi import NewsDataApiClient
from dotenv import load_dotenv
import os

# Load the API Keys from .env file
load_dotenv()


# NewsAPI wrapper Inheriting NewsApiClient
# Free tier allowing 100 req/day

class NewsAPI(NewsApiClient):

    # Initialize Client & establish connection
    def __init__(self) -> None:
        super().__init__(os.environ.get("NEWSAPI_KEY"))


# NewsData.io wrapper
# 200 Credits/day | 10 Articles/credit

class NewsDataAPI(NewsDataApiClient):
    def __init__(self) -> None:
        super().__init__(apikey=os.environ.get("NEWSDATA_KEY"))
