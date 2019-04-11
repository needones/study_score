''''''
import json
import os
import random
from time import sleep

from selenium import webdriver

# driver = webdriver.Chrome()
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

ops = webdriver.ChromeOptions()
# ops.add_argument('--headless')
ops.add_argument('--disable-gpu')
ops.add_argument('--disable-infobars')
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

# 学习理论（阅读文章12分，预计15分钟）
driver.find_element_by_xpath('//div[@class="father-nav"]/ul[3]/li[1]/a').click()
sleep(1)
windows = driver.window_handles
driver.switch_to.window(windows[1])
sleep(2)
for i in list(range(5)):
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

# 学习电视台（观看视频12分，预计40分钟）
driver.find_element_by_xpath('//div[@class="father-nav"]/ul[2]/li[2]/a').click()
sleep(5)
windows = driver.window_handles
driver.switch_to.window(windows[1])
driver.execute_script("var q=document.documentElement.scrollTop=1000")
sleep(2)

# 视频区
# driver.find_element_by_xpath('//div[@id="Chwgg53wi10o00"]/div/div[1]').click()
try:
    driver.find_element_by_xpath('//*[@id="5586"]/div/div/div/div/div/section/div/div/div[1]/div[1]').click()
except:
    driver.find_element_by_xpath('//div[@id="Chwgg53wi10o00"]/div/div[1]').click()
sleep(1)
windows = driver.window_handles
driver.switch_to.window(windows[2])
sleep(2)
list_vedio = []
for i in list(range(7)):
    print('第%d次视频' % (i + 1))
    if i < 2:
        pass
    elif i < 4:
        try:
            driver.find_element_by_xpath('//div[@class="_1KFAyh5wHi8boHp83TMkv-"]/div/div[3]').click()
            sleep(2)
        except:
            try:
                ActionChains(driver).key_down(Keys.PAGE_UP)
                sleep(2)
                driver.find_element_by_xpath('//div[@class="_1KFAyh5wHi8boHp83TMkv-"]/div/div[3]').click()
                sleep(2)
            except:
                try:
                    driver.find_element_by_xpath('//div[@class="radio_2p2eqv4lwtk00"]/div[2]').click()
                    sleep(5)
                except:
                    pass
    else:
        try:
            driver.find_element_by_xpath('//div[@class="_1KFAyh5wHi8boHp83TMkv-"]/div/div[4]').click()
            sleep(2)
        except:
            try:
                ActionChains(driver).key_down(Keys.PAGE_UP)
                sleep(2)
                driver.find_element_by_xpath('//div[@class="_1KFAyh5wHi8boHp83TMkv-"]/div/div[4]').click()
                sleep(2)
            except:
                try:
                    driver.find_element_by_xpath('//div[@class="radio_2p2eqv4lwtk00"]/div[3]').click()
                    sleep(5)
                except:
                    pass
    # 随机更改视频
    while True:
        k = random.randint(0, 16)

        if k not in list_vedio:
            list_vedio.append(k)
            break
    try:
        driver.find_elements_by_xpath(
            '//div[@class="Iuu474S1L6y5p7yalKQbW grid-gr"]//div[@class="_252R0WxMJIuJyNty2pZiaL thePic"]')[k].click()
    except:
        try:
            driver.find_elements_by_xpath('//div[@class="_252R0WxMJIuJyNty2pZiaL thePic"]')[k].click()
        except:
            try:
                driver.find_elements_by_xpath('//div[@id="Cd5zymfz1fzs0"]/div/div/div[1]')[k].click()
            except:
                print('第%d次视频获取失败！' % (i + 1))
    sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[3])
    sleep(2)
    driver.execute_script("var q=document.documentElement.scrollTop=400")
    sleep(4)
    # 视频睡眠
    time_s = random.randint(200, 240)
    # driver.execute_script("var q=document.documentElement.scrollTop=1500")
    sleep(time_s)
    driver.close()
    sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[2])
    sleep(2)

dict_cookie = {}
a = driver.get_cookies()
dict_cookie['data'] = a
data = json.dumps(dict_cookie)
with open(file_name, 'w', encoding='utf-8')as f:
    f.write(data)

driver.quit()
