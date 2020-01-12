#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:ssc

from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com/')
driver.implicitly_wait(10)
# 单个元素定位实战
driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_name('wd').send_keys('ssc')
# driver.find_element_by_class_name('s_ipt').send_keys('ssc')
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('ssc')
# driver.find_element_by_link_text(u'新闻').click()
# driver.find_element_by_partial_link_text(u'贴').click()
# driver.find_element_by_css_selector('#kw').send_keys('ssc')
# 多个元素定位实战
# driver.find_elements_by_tag_name('input')[7].send_keys('ssc')
# tag_names = driver.find_elements_by_tag_name('input')
# for tag_name in tag_names:
#     print(tag_name)
# print(type(tag_names))
# driver.refresh()
print('测试地址为：{0}'.format(driver.current_url))
# print('页面代码如下：{0}'.format(driver.page_source))
print('百度首页的标题为：{0}'.format(driver.title))
print('测试执行的浏览器：{0}'.format(driver.name))
t.sleep(3)
driver.quit()

