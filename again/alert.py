#coding:utf-8

from selenium import webdriver
from time import sleep
'''
#Alert confirmation
driver=webdriver.Firefox()
driver.get("http://sahitest.com/demo/alertTest.htm")
driver.find_element_by_name("b1").click()
driver.switch_to_alert().accept()
print driver.find_element_by_name("t1").get_attribute("value")
driver.find_element_by_name("b2").click()
sleep(5)
print driver.switch_to_alert().text
driver.switch_to_alert().accept()
driver.quit()

#confrim Test
driver=webdriver.Firefox()
driver.get("http://sahitest.com/demo/confirmTest.htm")
driver.find_element_by_name("b1").click()
print driver.switch_to_alert().text
driver.switch_to_alert().dismiss()
print driver.find_element_by_name("t1").get_attribute("value")
driver.find_element_by_name("b1").click()
print driver.switch_to_alert().text
driver.switch_to_alert().accept()
print driver.find_element_by_name("t1").get_attribute("value")
driver.quit()
'''
#prompt confirmation
driver=webdriver.Firefox()
driver.get("http://sahitest.com/demo/promptTest.htm")
driver.implicitly_wait(5)
driver.find_element_by_name("b1").click()
'''
driver.switch_to.alert.send_keys("aa")
driver.switch_to.alert.accept()
print driver.find_element_by_name("t1").get_attribute("value")
'''
a1 = driver.switch_to.alert  # 通过switch_to.alert切换到alert
sleep(1)
print a1.text  # text属性输出alert的文本
a1.send_keys('send some words to alert!')  # 往prompt型alert中传入字符串
sleep(1)
a1.accept()
print driver.find_element_by_name('t1').get_attribute('value')
driver.quit()


















