# 네이버 지도에 검색해서 검색 결과 가져오기

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://map.naver.com/')

#assert 'Django' in driver.title

keyword = '시청역'

elem = driver.find_element_by_id('search-input')
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

time.sleep(2) # 5초 대기

try:
    #addr = driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl/dd[1]/text()")
    #name = driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl/dt/a/b")

    first_item = driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl")
    addr = first_item.find_element_by_class_name('addr')
    print(addr.text)
    print("====="*10)

    result = driver.find_elements_by_class_name("lsnx_det")
    for item in result:
        item_name = item.find_element_by_css_selector('dt a b')
        item_addr = item.find_element_by_class_name('addr')
        item_tel = item.find_element_by_class_name('tel')
        print(item_name.text)
        print(item_addr.text)
        print(item_tel.text)

        if ( keyword in item_name.text ):
            p = item.find_element_by_tag_name('a')
            p.click()
            break

except NoSuchElementException:
    print("No Element")


time.sleep(10) # 5초 대기
driver.quit() # 브라우저 종료
