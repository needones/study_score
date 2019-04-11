import os

# file_name = os.path.dirname(os.path.realpath(__file__))
# file_name = os.path.dirname(os.path.realpath(file_name))
# print(file_name)
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1'
}
url = 'https://www.baidu.com/'


# url = 'http://www,dushu.com'
r = requests.get(url=url, headers=headers, verify=False)
print(r.text)
