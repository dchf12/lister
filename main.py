from crawler import Crawler
from datatable import DataTable

TARGET_URL = ""  # requestするURL
PREF_FILE = "./todohuken/jp-prefectures.txt"


def load_file(file_path):
    with open(file_path, encoding="utf-8", mode="r") as f:
        res = f.readlines()
    for i, r in enumerate(res):
        res[i] = r.strip()
    return res


def main():

    params = {"page": "1"}
    crawler = Crawler(url=TARGET_URL, params=params)

    # urlにrequest
    crawler.parse_data()
    print(crawler.soup)

    selector = "#searchResult > div.wrap-realtorList > div:nth-child(1) > div.heading > h3 > a"
    href = [x for x in crawler.get_elements_by_css_selector(selector)]
    print(href)


if __name__ == "__main__":
    main()
