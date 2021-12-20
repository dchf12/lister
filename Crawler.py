import os
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
        self.soup = BeautifulSoup(self.html_data, features="lxml")

    def get_html(self, html_file):
        if os.path.exists(html_file):
            with open(html_file, "r", encoding="utf-8") as f:
                self.html_data = f.read()
        else:
            self.html_data = self.request_data(self.url).text
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(self.html_data)

    def get_elements_by_css_selector(self, selector):
        s_select = self.soup.select(selector)
        table = [s for s in s_select]
        return table
