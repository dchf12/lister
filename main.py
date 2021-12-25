from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from crawler import Crawler

# Seleniumをあらゆる環境で起動させるオプション
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument('--proxy-server="direct://"')
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--headless")  # ※ヘッドレスモードを使用する場合、コメントアウトを外す

TARGET_URL = "https://www.zenkuren.or.jp/shopsearch"  # requestするURL
HTML_FILE = "housing_manager.html"  # requestしたurlのhtmlを保存するhtml
PREF_FILE = "./todohuken/jp-prefectures.txt"


def load_file(file_path):
    with open(file_path, encoding="utf-8", mode="r") as f:
        res = f.readlines()
    for i, r in enumerate(res):
        res[i] = r.strip()
    return res


def main():

    crawler = Crawler(url=TARGET_URL)
    crawler.parse_data()

    for i in range(1, 8):
        selector = f"#japantextlink > ul.area{i} > li > a"
        ul_area = [x for x in crawler.get_elements_by_css_selector(selector)]
        href_area = [x.get("href") for x in ul_area]

        for j in range(len(href_area)):
            crawler.url = "https://www.zenkuren.or.jp/" + href_area[j]
            stores = scraping_for_selenium(crawler.url)
            filename = href_area[j].replace("shopsearch/result_list?pref=", "")
            with open(f"csv/{filename}.csv", "w", encoding="utf-8") as f:
                f.writelines(stores)


def scraping_for_selenium(url):
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.implicitly_wait(5)
    try:
        driver.get(f"{url}")
        stores = []
        for i in range(1, 500):
            selector = f"#contents > div.shopsearchresultblock > div.shoplist > ul:nth-child({i}) \
            > li.table > table > tbody "
            items = driver.find_element(By.CSS_SELECTOR, selector).text
            stores.append(items)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        return stores


if __name__ == "__main__":
    main()
