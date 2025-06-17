import requests
import json
import re
import random


class NewsFeed:
    def __init__(self):
        self.__API_KEY = "NEVER PUSH KEYS TO GITHUB"
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=de&apiKey={self.__API_KEY}")
        self.__data = json.loads(response.text)
        self.__desired = ["DER SPIEGEL", "NDR.de", "ZDFheute", "WELT"]

    def get_news(self):
        news = []
        for article in self.__data["articles"]:
            title = article["title"]
            rx = re.search("(?s:.*)-", title)
            headline = title[rx.span()[0]:rx.span()[1] - 2]
            author = title[rx.span()[1] + 1:]
            if author in self.__desired:
                news.append((headline, author))
        random.shuffle(news)

        return news


if __name__ == "__main__":
    for i in NewsFeed().get_news():
        print(i)
