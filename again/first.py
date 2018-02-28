#coding=utf-8

from selenium import webdriver
'''
#打开浏览器
driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
example1:
#找到输入框，输入关键字：苹果
driver.find_element_by_class_name("s_ipt").send_keys("apple")

#点击“百度一下”，检查搜索结果
driver.find_element_by_id("su").click()

#验证是否正确
print driver.title()

#看到64页了
driver.find_element_by_link_text("新闻").click()

#使用自己定义的xpath的绝对路径
#一种比较好的方式是这样的    By.xpath("//input[contains(@id,'那么美')]")
driver.find_element_by_xpath("//input[@id='kw']").send_keys("apple")
driver.find_element_by_id("su").click()
#还有一种绝对路径的方法，太难了
'''

































