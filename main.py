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
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    h = logging.FileHandler(filename="group_list.log", encoding="utf-8", mode="w")
    logger.addHandler(h)

    # ホームページのURLを格納する
    TARGET_URL = "https://lister.jp"
    industryall_organization = []

    response = request_data(TARGET_URL + "/industry/group/")
    soup = BeautifulSoup(response.text, features="lxml")
    logger.info(soup)
    # logger.debug(soup.select("#industry-group-lists > ul > li:nth-child(1) > ul > li > a"))


if __name__ == "__main__":
    main()
