#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/mouseover.htm")

#两个元素位置

write1=driver.find_element_by_xpath("//input[@value='Write on hover']")
blank1=driver.find_element_by_xpath("//input[@value='Blank on hover']")
result=driver.find_element_by_xpath("//input[@name='t1']")
#鼠标移动到write on hover button上，检查下方editbox的内容
ActionChains(driver).move_to_element(write1).perform()
print result.get_attribute("value")
sleep(2)
#鼠标移动到blank on hover button上，检查下方editbox的内容
ActionChains(driver).move_to_element(blank1).perform()
print result.get_attribute("value")
print "over"










