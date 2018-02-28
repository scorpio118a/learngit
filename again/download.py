#coding:utf-8

from selenium import webdriver
from time import sleep
'''
fp=webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.dir",'d:\\')
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")

driver=webdriver.Firefox(firefox_profile=fp)
driver.get("http://sahitest.com/demo/saveAs.htm")
driver.find_element_by_xpath("/html/body/a[3]").click()
sleep(3)
'''

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', r'C:\Users\penghuan\Desktop\sql')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

driver = webdriver.Firefox(firefox_profile=profile)

driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
sleep(3)
driver.quit()