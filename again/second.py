#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://www.youdao.com/")

driver.set_window_size(500,500)

WebDriverWait(driver,10)

driver.set_window_size(1000,1000)

driver.find_element_by_xpath("//input[@id='translateContent']").send_keys("apple")
driver.find_element_by_xpath(".//*[@id='form']/button").click()

#看到74页