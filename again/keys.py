#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

#寻找编辑框的id
edit1=driver.find_element_by_id('kw')

#输入apple，验证apple；然后输入orange，然后验证orange
edit1.send_keys("apple")
print driver.title

edit1.send_keys(Keys.BACKSPACE)
edit1.send_keys(Keys.TAB)
sleep(2)
edit1.send_keys("orange")
print driver.title

