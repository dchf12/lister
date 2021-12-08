import time

import requests
from bs4 import BeautifulSoup
import logging


def request_data(url, params=None):
    try:
        # アクセス結果を格納
        res = requests.get(url, params=params)
        res.raise_for_status()
        time.sleep(1)
    except requests.exceptions.RequestException as e:
        print("error", e)
    return res


def parse_data(url, params):
    # 結果解析
    res = request_data(url, params)
    soup = BeautifulSoup(res.text, features="lxml")
    return soup


def main():
    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.DEBUG)
    # h = logging.FileHandler(filename="group_list.log", encoding="utf-8", mode="w")
    # logger.addHandler(h)

    # ホームページのURLを格納する
    TARGET_URL = "https://lister.jp/industry/group/all/"
    industryall_organization = []
    table_head = ["大分類", "中分類", "小分類", "業界団体名", "企業一覧", "ホームページ"]

    response = request_data(TARGET_URL)
    soup = BeautifulSoup(response.text, features="lxml")
    # logger.debug(soup)
    print(soup.select("#industry-group-table > thead > tr > td:nth-child(1)"))


"""
import pandas as pd
df = pd.DataFrame({
    '名前' :['田中', '山田', '高橋'],
    '役割' : ['営業部長', '広報部', '技術責任者'],
    '身長' : [178, 173, 169]
    })
print(df)
print(df.dtypes)

print(df.columns) # 列ラベルの確認(辞書型のkeyが列ラベル）
"""

if __name__ == "__main__":
    main()
