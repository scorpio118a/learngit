#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
driver=webdriver.Firefox()
time.sleep(2)
driver.get("http://sahitest.com/demo/clicks.htm")
time.sleep(2)
'''
#driver.maximize_window()
#单独点击复选框或者右键点击，可用
driver.find_element_by_xpath("//input[@value='Click me']").click()
right_click_me=driver.find_element_by_xpath("//input[@value='right click me']")
ActionChains(driver).context_click(right_click_me).perform()
print driver.find_element_by_xpath("//textarea[@name='t2']").get_attribute("value")

#清数据
driver.find_element_by_xpath("//input[@value='Clear']").click()
print driver.find_element_by_xpath("//textarea[@name='t2']").get_attribute("value")
print "over"

#点击click me
driver.find_element_by_xpath("//input[@value='click me']").click()
print driver.find_element_by_xpath("//textarea[@name='t2']").get_attribute("value")

'''
#双击有问题
time.sleep(2)
double_click_me=driver.find_element_by_xpath("//input[@value='dbl click me']")
ActionChains(driver).double_click(double_click_me).perform()
print driver.find_element_by_xpath("//textarea[@name='t2']").get_attribute("value")
print "over"



























