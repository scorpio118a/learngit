#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Firefox()
url1="file:///C:/Users/penghuan/Desktop/html&js/checkbox.html"
driver.get(url1)

elements=driver.find_elements_by_xpath('//input[@type="checkbox"]')
for i in elements:
    if i.get_attribute("type")=="checkbox":
        i.click()
        time.sleep(2)

print len(elements)
print "\t"
elements.pop().click()


