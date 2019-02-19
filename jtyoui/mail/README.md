# **Mail** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 邮箱模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-邮箱-black.svg)]()


#### 安装
    pip install jtyoui

### 使用方法
```python
from jtyoui.mail import send_qq_mail

if __name__ == '__main__':
    flag = send_qq_mail(from_addr='ptyoui@jtyoui.com', password='密码', to_addr='jtyoui@jtyoui.com',content='测试邮箱', subject='政治文件', files='政治.txt')
    if flag:
        print('发送成功!')
    else:
        print('发送失败!')
```

### 更换邮件传输协议
```python
from jtyoui.mail import *
HOST=('smtp.qq.com', 465)
flag = send_qq_mail(from_addr='ptyoui@jtyoui.com', password='密码', to_addr='jtyoui@jtyoui.com',content='测试邮箱', subject='政治文件', files='政治.txt')
if flag:
    print('发送成功!')
else:
    print('发送失败!')
```
***
[1]: https://blog.jtyoui.com