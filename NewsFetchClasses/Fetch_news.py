from newsapi import NewsApiClient
import os


# NewsAPI wrapper Inheriting NewsApiClient
# Free tier allowing 100 req/day

class NewsAPI(NewsApiClient):

    # Initialize Client & establish connection
    def __init__(self) -> None:
        super().__init__(os.environ.get("NEWSAPI_KEY"))


