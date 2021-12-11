import os
import time

import requests
from bs4 import BeautifulSoup


def request_data(url, params=None):
    try:
        # アクセス結果を格納
        res = requests.get(url, params=params)
        res.raise_for_status()
        time.sleep(1)
    except requests.exceptions.RequestException as e:
        print("error", e)
    return res


def parse_data(res):
    # 結果解析
    soup = BeautifulSoup(res, features="lxml")
    return soup


def get_html(url, file_name):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            response = f.read()
        print("exists")
    else:
        response = request_data(url).text
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(response)
        print("not exists")
    return response


def main():

    # urlにrequest
    TARGET_URL = "https://lister.jp/industry/group/all/"
    HTML_FILE = "group_list.html"
    response = get_html(TARGET_URL, HTML_FILE)
    soup = parse_data(response)

    # 表頭の一覧を取得
    s_select = soup.select("#industry-group-table > thead > tr > td")
    table_head = [head.string for head in s_select]
    print(table_head)

    # 団体一覧を取得
    # s_select = soup.select("#industry-group-table > tbody > tr:nth-child(i) > td")
    s_select = soup.select("#industry-group-table > tbody > tr:nth-child(1) > td")
    industryall_organization = [item.string for item in s_select]
    print(industryall_organization)

    # 企業一覧のURL取得 if
    s_select = soup.select("#industry-group-table > tbody > tr:nth-child(1) > td:nth-child(5) > a")
    print(s_select[0].get("href"))

    # ホームページのURL取得
    s_select = soup.select("#industry-group-table > tbody > tr:nth-child(1) > td:nth-child(6) > a")
    print(s_select[0].get("href"))


if __name__ == "__main__":
    main()

    # import pandas as pd

    # df = pd.DataFrame(
    #     {"名前": ["田中", "山田", "高橋"], "役割": ["営業部長", "広報部", "技術責任者"], "身長": [178, 173, 169]}
    # )
    # print(df)
    # print(df.dtypes)

    # print(df.columns)  # 列ラベルの確認(辞書型のkeyが列ラベル）
