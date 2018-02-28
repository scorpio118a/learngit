#coding:utf-8

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://sahitest.com/demo/php/fileUpload.htm")

driver.find_element_by_id("file").send_keys(r"C:\Users\penghuan\Desktop\sql\t_venue.sql")
driver.find_element_by_xpath("/html/body/form[1]/input[3]").click()