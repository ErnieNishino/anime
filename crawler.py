from ssl import _create_unverified_context
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import urllib.parse


def get_douban_rating(movie_title):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    load_driver_success = False
    browser = None
    wait = None

    try:
        browser = webdriver.Chrome()
        browser.set_page_load_timeout(10)
        browser.set_script_timeout(10)
        wait = WebDriverWait(browser, 10)
        load_driver_success = True
    except Exception as ex:
        load_driver_success = False
        err_str = "加载chromedriver驱动失败，请下载chromedriver驱动并填写正确的路径。\n\n异常信息：{}".format(ex)
        return [err_str]

    if load_driver_success:
        try:
            browser.get(
                'https://movie.douban.com/subject_search?search_text=' + urllib.parse.quote(movie_title) + '&cat=1002')
            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.root')))
            dr = browser.find_elements(by=By.XPATH, value="//div[@class='item-root']")
            douban_ratings = []

            for son in dr:
                rating_element = son.find_elements(by=By.XPATH, value=".//span[@class='rating_nums']")
                if rating_element:
                    douban_ratings.append(rating_element[0].text)

            browser.quit()
            return douban_ratings

        except Exception as ex:
            browser.quit()
            err_str = "chromedriver驱动加载成功，但是出现其他未知异常：{}".format(ex)
            return [err_str]
