import os
import time

import requests
from bs4 import BeautifulSoup
import src.stopwatch as stopwatch


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


@stopwatch
def main():

    # urlにrequest
    TARGET_URL = "https://lister.jp/industry/group/all/"
    HTML_FILE = "group_list.html"
    response = get_html(TARGET_URL, HTML_FILE)
    soup = parse_data(response)

    # 表頭の一覧を取得
    s_select = soup.select("#industry-group-table > thead > tr > td")
    table_head = [s.string for s in s_select]
    print(table_head)

    # 団体一覧を取得
    industryall_organization_all = [tr for tr in soup.select("#industry-group-table > tbody > tr")]
    industryall_organization_one = [
        [td.string for td in tr] for tr in industryall_organization_all
    ]
    # print(industryall_organization_one[0][0])

    # 企業一覧のURL取得
    corporate_all = [
        tr for tr in soup.select("#industry-group-table > tbody > tr > td:nth-child(5) > a")
    ]
    corporate_one = [tag_a.get("href") for tag_a in corporate_all]
    print(len(corporate_one))

    # ホームページのURL取得
    homepage_all = [
        tr for tr in soup.select("#industry-group-table > tbody > tr > td:nth-child(6) > a")
    ]
    homepage_one = [tag_a.get("href") for tag_a in homepage_all]
    print(len(homepage_one))

    import pandas as pd

    df = pd.DataFrame(industryall_organization_one, columns=table_head)
    for i, company in enumerate(df["企業一覧"]):
        if company is None:
            continue
        else:
            df.at[i, df.columns[4]] = corporate_one.pop(0)
    for i, homepage in enumerate(df["ホームページ"]):
        if homepage is None:
            continue
        else:
            df.at[i, df.columns[5]] = homepage_one.pop(0)
    df.to_csv(
        "pandas.csv",
    )


if __name__ == "__main__":
    main()
