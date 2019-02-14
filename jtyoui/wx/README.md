# **WX** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 这是一个用Python写微信自动聊天机器
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-微信-black.svg)]()


#### 安装
    pip install jtyoui

#### 使用方法
```python
from jtyoui.wx import *
if __name__ == '__main__':
    auto_start(wx_name='Jtyoui')  # 输入自己的微信名,这个是自己取的名字
```

#### 更加自定义的定义
```python
from jtyoui.wx.AutoChat import *
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    oneself(wx_name='Jtyoui')  # 输入自己的微信名
    itchat.run()
```

#### 爬取电影机器人
```python
from jtyoui.wx import movie_start
if __name__ == '__main__':
        movie_start() #打开微信输入电影名字
```

***
[1]: https://blog.jtyoui.com