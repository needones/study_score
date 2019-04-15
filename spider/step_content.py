import json
import os
import random
from datetime import datetime
from time import sleep

from selenium import webdriver

# driver = webdriver.Chrome()
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

ops = webdriver.ChromeOptions()
ops.add_argument('--headless')  # 无头
ops.add_argument('--disable-gpu')  # 禁用GPU
ops.add_argument('--disable-infobars')  # 关闭浏览器上方自动测试提示
driver = webdriver.Chrome(chrome_options=ops)

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
# 学习理论（阅读文章12分，预计20分钟）
# driver.find_element_by_xpath('//div[@class="father-nav"]/ul[3]/li[1]/a').click()
driver.find_element_by_xpath('//div[@class="menu-list"]/div[1]/a[3]').click()
sleep(1)
windows = driver.window_handles
driver.switch_to.window(windows[1])
sleep(2)
# 7篇
# list_content = []
for i in list(range(7)):
    sleep(2)
    # while True:
    #
    #     kk = random.randint(7, 20)
    #     if kk not in list_content:
    #         list_content.append(kk)
    #         break

    # 当时间在17点之前，新内容没有上架，点击昨日的后半部分的新文章
    time1 = int(datetime.now().strftime('%H'))
    if time1 < 16:
        kk = i + 7
    else:
        kk = i
    driver.find_elements_by_xpath('//div[@class="_3wnLIRcEni99IWb4rSpguK"]/div/div[1]')[kk].click()
    sleep(3)
    windows = driver.window_handles
    driver.switch_to.window(windows[2])
    key = random.randint(0, 1)
    for j in list(range(9)):
        sleep(random.randint(5, 6))
        if key == 1:
            num = random.randint(200, 350)
            driver.execute_script("var q=document.documentElement.scrollTop={}".format((j + 3) * num))

            sleep(random.randint(9, 13))
        else:
            if j == 1:
                sleep(random.randint(10, 13))
            else:
                ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
                sleep(random.randint(9, 13))
        print('---第{}篇---{}0%---'.format((i + 1), (j + 1)))
    # 滑动到底部
    driver.execute_script("var q=document.documentElement.scrollTop=100000")
    sleep(2)
    ActionChains(driver).key_down(Keys.PAGE_UP).perform()
    sleep(5)
    driver.close()
    sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    print('===============第%d篇结束===============' % (i + 1))
driver.close()
sleep(2)
# 换回首页
windows = driver.window_handles
driver.switch_to.window(windows[0])

# 写入最新的cookie
dict_cookie = {}
a = driver.get_cookies()
dict_cookie['data'] = a
data = json.dumps(dict_cookie)
with open(file_name, 'w', encoding='utf-8')as f:
    f.write(data)
print('---------恭喜你---12分到手--------')

sleep(2)
ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
sleep(5)
driver.quit()
