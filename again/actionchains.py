#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
driver=webdriver.Firefox()
time.sleep(2)
driver.get("http://sahitest.com/demo/clicks.htm")
time.sleep(2)
driver.maximize_window()
#测试双击
double_click_btn=driver.find_element_by_xpath('//input[@value="dbl click me"]')
ActionDoubleClick=ActionChains(driver).double_click(double_click_btn)
ActionDoubleClick.perform()
#验证点击后的文字
print driver.find_element_by_xpath("html/body/form/textarea").get_attribute("value")

