import pprint
from newsapi import NewsApiClient
import os


class NewsAPI:

    # Initialize Client & establish connection
    def __init__(self) -> None:
        self.client = NewsApiClient(os.environ.get("NEWSAPI_KEY"))

    
    def get_all_news(self):
        return self.client.get_everything()
    
    def get_sources(self):
        return self.client.get_sources()
    
    def get_headlines(self):
        return self.client.get_top_headlines()
    


# pprint.pprint(NewsAPI().get_headlines())



