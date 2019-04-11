import json
import os
import random
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.xuexi.cn')
sleep(2)
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
file_name = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.dirname(os.path.realpath(file_name)) + '\cookie\cookie.json'
driver.delete_all_cookies()
cookie = json.load(open(file_name, encoding='utf-8'))
data = cookie['data']
# print(data)
for i in data:
    driver.add_cookie(i)

sleep(1)
driver.refresh()
sleep(3)

'''
独立文章模块
'''
# 学习理论（阅读文章12分，预计15分钟）
driver.find_element_by_xpath('//div[@class="father-nav"]/ul[3]/li[1]/a').click()
sleep(1)
windows = driver.window_handles
driver.switch_to.window(windows[1])
sleep(2)
# 6篇
for i in list(range(6)):
    sleep(2)
    driver.find_elements_by_xpath('//div[@class="_3wnLIRcEni99IWb4rSpguK"]/div/div[1]')[i].click()
    sleep(3)
    windows = driver.window_handles
    driver.switch_to.window(windows[2])
    for j in list(range(6)):
        sleep(10)
        num = random.randint(200, 350)
        driver.execute_script("var q=document.documentElement.scrollTop={}".format((j + 1) * num))
        print('第%d次滑动' % (j + 1))
        sleep(20)
    driver.close()
    sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    print('---------------第%d篇刷完-----------------' % (i + 1))
driver.close()
sleep(2)
# 换回首页
windows = driver.window_handles
driver.switch_to.window(windows[0])

#
dict_cookie = {}
a = driver.get_cookies()
dict_cookie['data'] = a
data = json.dumps(dict_cookie)
with open(file_name, 'w', encoding='utf-8')as f:
    f.write(data)

driver.quit()
