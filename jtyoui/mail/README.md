# **Mail** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 邮箱模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-邮箱-black.svg)]()


#### 安装
    pip install jtyoui

### 使用QQ邮箱方法
```python
from jtyoui.mail import send_qq_mail

if __name__ == '__main__':
    flag = send_qq_mail(from_addr='你的QQ邮箱', password='你的授权码', to_addr='别人的邮箱;另一个人的邮箱',content='文字内容', subject='主题', files='文件附件')
    if flag:
        print('发送成功!')
    else:
        print('发送失败!')
```

### 使用其他邮箱、更换邮件传输协议
```python
from jtyoui.mail import send_qq_mail

if __name__ == '__main__':
    HOST=('smtp.163.com', 465) #换成网易邮箱、更换邮件传输协议
    flag = send_qq_mail(from_addr='你的网易邮箱', password='你的授权码', to_addr='别人的邮箱;另一个人的邮箱',content='文字内容', subject='主题', files='文件附件',host=HOST)
    if flag:
        print('发送成功!')
    else:
        print('发送失败!')
```
***

### 如果获得授权码
>>> [点击查看获得授权码](https://jingyan.baidu.com/article/fedf0737af2b4035ac8977ea.html)


[1]: https://blog.jtyoui.com