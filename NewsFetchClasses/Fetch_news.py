from newsapi import NewsApiClient
from newsdataapi import NewsDataApiClient
import os


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
        super().__init__(apikey=os.environ.get("NEWSDATA_KEY"))  # type: ignore


# Actual Client Objects to be utilized
newsAPI = NewsAPI()


def get_sources_by_country(country_code: str) -> str:
    """
    Return `string` of comma separated `sources` for the given country!
    """
    response = newsAPI.get_sources(country=country_code)

    scr_ids = (
        [scr["id"] for scr in response["sources"] if scr["id"]]
        if (response["status"] == "ok")
        else []
    )

    return ",".join(
        scr_ids if scr_ids else ["the-times-of-india", "google-news-in", "the-hindu"]
    )
