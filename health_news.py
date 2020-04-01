import requests
import json


class RussiaNews:

    def __init__(self):
        self.counter = 0
        self.my_data = None
        self.get_json()

    def get_json(self):
        url = ('http://newsapi.org/v2/top-headlines?'
               'country=ru&'
               'category=health&'
               'apiKey=4f520a93615b4a17bfcaa111d872b70c')
        json_data = requests.get(url)
        self.my_data = json.loads(json_data.text)

    def fresh_new(self):
        title_news = self.my_data['articles'][self.counter]['title']
        description_news = self.my_data['articles'][self.counter]['description']
        url_news = self.my_data['articles'][self.counter]['url']
        info = f'{title_news} {description_news} {url_news}'
        return info

    def next_new(self):
        self.counter += 1
        self.refresh_news()

    def is_last_new(self):
        return self.counter < len(self.my_data['articles']) - 1

    def refresh_news(self):
        if not self.is_last_new():
            self.counter = 0
            self.get_json()
