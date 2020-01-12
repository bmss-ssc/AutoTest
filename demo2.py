from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://mail.sina.com.cn/")
driver.implicitly_wait(10)
# 获取当前句柄
now_handle = driver.current_window_handle
t.sleep(2)
# 点击注册链接
driver.find_element_by_link_text('注册').click()
t.sleep(2)
# 获取所有窗口句柄
handles = driver.window_handles
# 对所有窗口句柄循环处理
for handle in handles:
    # 判断 handle 不是当前窗口句柄
    if handle != now_handle:
        driver.switch_to.window(handle)
        t.sleep(2)
        driver.find_element_by_name('email').send_keys('ssc')
        t.sleep(2)
        driver.close()
driver.switch_to.window(now_handle)
t.sleep(2)
driver.find_element_by_id('freename').send_keys('ssc')
t.sleep(3)
driver.quit()
