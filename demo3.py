#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:ssc

from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.hao123.com/')
so = driver.find_element_by_name('word')
print('输入框提示信息：{0}'.format(so.get_attribute('placeholder')))
so.send_keys('ssc')
print('填入关键字为：{0}'.format(so.get_attribute('value')))
RenMinWang = driver.find_element_by_link_text('人民网')
print('关于人民网是否可见：{0}'.format(RenMinWang.is_displayed()))
print('关于人民网是否可见：{0}'.format(RenMinWang.is_enabled()))
# t.sleep(2)
# so.clear()
t.sleep(2)
driver.quit()