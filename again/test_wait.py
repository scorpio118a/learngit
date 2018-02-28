#coding:utf-8


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#显式等待
driver=webdriver.Firefox()
driver.get("https://www.sogou.com/")
element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="query"]')),message="you are right")
element.send_keys("apple")









'''
#隐式等待
driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("apple")
'''