#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:ssc

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time as t
# 下拉框实战
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com/')
# 实现鼠标悬浮到百度首页
element = driver.find_element_by_css_selector('a.pf:nth-child(8)')
t.sleep(3)
ActionChains(driver).move_to_element(element).perform()
t.sleep(3)
# 点击设置中的搜索设置按钮
driver.find_element_by_css_selector('.setpref').click()
t.sleep(2)
nr = driver.find_element_by_name('NR')
# 实例化 Select 类
select = Select(nr)
select.select_by_index(2)
print('下拉框选择的最新条数是：',nr.get_attribute('value'))
t.sleep(3)
driver.quit()