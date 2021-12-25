import time

import requests
from bs4 import BeautifulSoup


class Crawler:
    """指定URLのHTMLを取得し、解析を行う"""

    def __init__(self, url, params=None):
        self.url = url
        self.params = params

    def request_data(self):
        try:
            # アクセス結果を格納
            res = requests.get(self.url, params=self.params)
            res.raise_for_status()
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print("error", e)
        return res

    def parse_data(self):
        # 結果解析
        self.html_data = self.request_data().text
        self.soup = BeautifulSoup(self.html_data, features="lxml")

    def get_elements_by_css_selector(self, selector):
        s_select = self.soup.select(selector)
        table = [s for s in s_select]
        return table
