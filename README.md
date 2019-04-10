## 1.配置selenium的谷歌浏览器
    到http://npm.taobao.org/mirrors/chromedriver/ 下载对应自己谷歌浏览器版本的chromedriver
    我使用的谷歌浏览器版本号和chromedriver已上传，仅供参考
#### 下载好的chromedriver.exe复制到谷歌浏览器的根目录
    并把所在的目录加入到环境变量中，win7需要重启才能生效
#### 再复制一份到Python的根目录

## 2.环境安装
    在项目目录下，pip install -r requirments.txt 即可

## 3.运行spider目录下的set_cookie.py文件

    手动点击登陆，60s内完成扫码登陆，等待程序关闭，cookie获取成功

## 4.再运行study.py即可
