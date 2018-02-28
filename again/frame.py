#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
urltest='file:///C:/Users/penghuan/Desktop/html&js/frame.html'
driver.get(urltest)

driver.switch_to_frame('if')
driver.implicitly_wait(3)
driver.find_element_by_class_name("s_ipt").send_keys("apple")
driver.implicitly_wait(3)
