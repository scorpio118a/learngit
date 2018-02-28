#coding:utf-8
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
cookies=driver.get_cookies()
print "\b"
for cookie in cookies:
    print "%s---%s"%(cookie["name"],cookie["value"])
