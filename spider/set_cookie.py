import json
import os
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.xuexi.cn')

sleep(30)
# 60s时间内登录成功，等待程序关闭即可
'''cookie有效期很短，基本上每天都要重新登录，运行这个文件'''

windows = driver.window_handles
driver.switch_to.window(windows[1])
sleep(30)
a = driver.get_cookies()
file_name = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.dirname(os.path.realpath(file_name)) + '\cookie'
os.makedirs(file_name, exist_ok=True)
dict_cookie = {}
dict_cookie['data'] = a
data = json.dumps(dict_cookie)
with open(file_name + '\cookie.json', 'w', encoding='utf-8')as f:
    f.write(data)
    print('cookie get success')
driver.quit()
