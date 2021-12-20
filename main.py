from Crawler import Crawler

TARGET_URL = "https://lister.jp/industry/group/all/"  # requestするURL
HTML_FILE = "group_list.html"  # requestしたurlのhtmlを保存するhtml


def main():

    crawler = Crawler(TARGET_URL)

    # urlにrequest
    crawler.get_html(HTML_FILE)
    crawler.parse_data()

    # 表頭の一覧を取得
    selector = "#industry-group-table > thead > tr > td"
    table_head = crawler.get_elements_by_css_selector(selector)
    print(table_head)

    # 団体一覧を取得
    industryall_organization_all = [
        tr for tr in crawler.soup.select("#industry-group-table > tbody > tr")
    ]
    industryall_organization_one = [
        [td.string for td in tr] for tr in industryall_organization_all
    ]
    # print(industryall_organization_one[0][0])

    # 企業一覧のURL取得
    corporate_all = [
        tr
        for tr in crawler.soup.select("#industry-group-table > tbody > tr > td:nth-child(5) > a")
    ]
    corporate_one = [tag_a.get("href") for tag_a in corporate_all]
    print(len(corporate_one))

    # ホームページのURL取得
    homepage_all = [
        tr
        for tr in crawler.soup.select("#industry-group-table > tbody > tr > td:nth-child(6) > a")
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
