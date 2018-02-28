#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')
#find_element_by_id
#driver.find_element_by_id('kw').send_keys('books')

#find_element_by_xpath
#driver.find_element_by_xpath(".//*[@id='u1']/a[8]").click()

#find_element_by_xpath
driver.find_element_by_xpath(".//*[@id='u1']/a[1]").click()
driver.maximize_window()
driver.set_window_size(2900,2900)
#driver.quit()

