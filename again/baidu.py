#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

filepath=r"E:\test_selenium\again\info.txt"
urlink="http://www.baidu.com"

fl=open(filepath,'r')
items=fl.readlines()

def searchit(user_info):
    driver=webdriver.Firefox()
    driver.get(urlink)
    driver.find_element_by_id("kw").send_keys(user_info)
    sleep(5)
    driver.find_element_by_id("su").click()
    sleep(5)
    driver.quit()

for item in items:
    searchit(item)




