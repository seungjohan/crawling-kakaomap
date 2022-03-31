import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('lang=ko_KR')
chromedriver_path = "chromedriver"
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options= options)



# logic #
search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')
search_area.send_keys('강남구 스타벅스')
driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys()


from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
cafe_list = soup.select('.placelist > .PlaceItem')


driver.quit()