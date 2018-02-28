#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")

#原位置
original=driver.find_element_by_xpath("//div[@id='dragger']")
#移动到item2
dest=driver.find_element_by_xpath("/html/body/div[3]")

ActionChains(driver).drag_and_drop(original,dest).perform()
print driver.find_element_by_xpath("//div[@class='item dragover dropped']").text









