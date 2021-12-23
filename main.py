from crawler import crawler
from datatable import DataTable

AREA = "tokyo"
TARGET_URL = f"https://www.homes.co.jp/realtor/{AREA}/list/"  # requestするURL

HTML_FILE = "housing_manager.html"  # requestしたurlのhtmlを保存するhtml


def main():

    params = {"page": "1"}
    crawler = Crawler(url=TARGET_URL, params=params)

    # urlにrequest
    crawler.get_html(HTML_FILE)
    crawler.parse_data()
    print(crawler.soup)

    selector = "#searchResult > div.wrap-realtorList > div:nth-child(1) > div.heading > h3 > a"
    href = [x for x in crawler.get_elements_by_css_selector(selector)]
    print(href)

    # i_data = DataTable()
    # i_data.modify_dataframe()
    # i_data.save_file("housing_manager.csv")


if __name__ == "__main__":
    main()
