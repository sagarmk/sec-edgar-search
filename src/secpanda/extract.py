from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Extract:
    def __init__(self):

        self.keyword = None
        self.list_map = {}
        chrome_services = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(options=chrome_options, service=chrome_services)
        self.driver.maximize_window()

    def search_keys(self, keyword):

        self.keyword = keyword
        self.driver.get('https://www.sec.gov/edgar/search/')
        search = self.driver.find_element(By.XPATH, '//*[@id="entity-short-form"]')
        search.send_keys(self.keyword)
        self.driver.find_element(By.XPATH, '//*[@id="search"]').click()
        time.sleep(1)
        return self.driver

    def extract_links(self):
        if self.keyword not in self.list_map:
            self.list_map[self.keyword] = []
        elems = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div[2]/table/tbody/tr//td//a")
        for elem in elems:
            if elem:
                if elem.get_attribute("href").endswith('.htm'):

                    ### click the hyper link to get full url ###
                    elem.click()
                    download_link = self.driver.find_element(By.XPATH,
                                                             '/html/body/div[4]/div/div/div[3]/a').get_attribute(
                        "href")

                    if download_link:
                        if download_link.endswith('.htm'):
                            self.list_map[self.keyword].append(download_link)
                        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/button').click()
                        time.sleep(5)

    def pagination_skip(self):

        pagination = self.driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div[2]/nav/ul/li')
        # self.extract_links()
        for page in pagination:
            if page.text.isdigit():
                # print(f"Extracting pages from Page No. {page.text}")
                page.click()
                time.sleep(5)
                self.extract_links()

    def get_list(self):

        return self.list_map

    def exit_driver(self):

        self.driver.quit()
        return 'driver connection closed'