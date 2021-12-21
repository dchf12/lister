from crawler import Crawler
from industryalldatatable import IndustryallDataTable

TARGET_URL = "https://lister.jp/industry/group/all/"  # requestするURL
HTML_FILE = "group_list.html"  # requestしたurlのhtmlを保存するhtml


def main():

    crawler = Crawler(TARGET_URL)

    # urlにrequest
    crawler.get_html(HTML_FILE)
    crawler.parse_data()

    # 表頭の一覧を取得
    selector = "#industry-group-table > thead > tr > td"
    table_head = [x.string for x in crawler.get_elements_by_css_selector(selector)]

    # 団体一覧を取得
    selector = "#industry-group-table > tbody > tr"
    industryall_groups = [
        [td.string for td in tr] for tr in crawler.get_elements_by_css_selector(selector)
    ]

    # 企業一覧のURL取得
    selector = "#industry-group-table > tbody > tr > td:nth-child(5) > a"
    corporate_urls = [
        tag_a.get("href") for tag_a in crawler.get_elements_by_css_selector(selector)
    ]

    # ホームページのURL取得
    selector = "#industry-group-table > tbody > tr > td:nth-child(6) > a"
    homepage_urls = [tag_a.get("href") for tag_a in crawler.get_elements_by_css_selector(selector)]

    i_data = IndustryallDataTable()
    i_data.modify_dataframe(table_head, industryall_groups, corporate_urls, homepage_urls)
    i_data.save_file("group_list.html")


if __name__ == "__main__":
    main()
