#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/"+"/")
sleep(2)
driver.get_screenshot_as_file(r"C:\Users\penghuan\Desktop\bug\1.jpg")
sleep(2)
driver.find_element_by_id("kw").send_keys("apple")
sleep(2)
driver.find_element_by_name("wd").clear()
sleep(2)
driver.find_element_by_xpath("//input[@id='kw']").send_keys("pear")
sleep(2)
driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.BACK_SPACE)
sleep(2)
driver.find_element_by_xpath("//input[@id='kw']").send_keys("a")
sleep(2)
driver.find_element_by_xpath(".//*[@id='su']").click()
sleep(2)
driver.get_screenshot_as_file(r"C:\Users\penghuan\Desktop\bug\1.jpg")
print driver.title
#driver.quit()




#=========================================================================================================
#定位元素需要练习
#再看需要看4.9,4.10,4.11,4.12,4.14，4.15,4.16,

#1、熟练掌握xpath\CSS 定位的使用，这样在遇到各种难以定位的属性时才不会变得束手无策。
#2、学习掌握JavaScript 语言，掌握JavaScript 好处前面已经有过阐述，可以让我们的自动化测试工作更加游刃有余。
#3、自动化测试归根结底是与前端打交道，多多熟悉前端技术，如http 请求，HTML 语言，cookie、session机制等。