from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time



def extract_links():
    elems = driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[2]/table/tbody/tr//td//a")
    for elem in elems:

        if elem.get_attribute("href").endswith('.htm'):
    
            elem.click()
            download_link = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/a').get_attribute("href")
            print(download_link)
            if download_link.endswith('.htm'):
                folly.append(download_link)

            driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()
            time.sleep(1)

if __name__ == "__main__":

    folly = []
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r'/usr/bin/geckodriver')
    driver.get('https://www.sec.gov/edgar/search/')
    search = driver.find_element_by_xpath('//*[@id="entity-short-form"]')
    search.send_keys("employment agreement")
    driver.find_element_by_xpath('//*[@id="search"]').click()

    time.sleep(5)
    # driver.find_element_by_xpath('//*[@id="date-range-select"]/option[text()='Last year']').click()

    extract_links(driver)
    pagination = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/nav/ul/li')
    for pages in pagination:
        try:
            if int(pages.text)< 11:
                pages.click()
                time.sleep(1)
                extract_links(driver)
        except:
            pass
    driver.quit()

print(folly)

