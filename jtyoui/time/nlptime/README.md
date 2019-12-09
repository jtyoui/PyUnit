# **NLPTime** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 处理NLP时间模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()


### 安装
    pip install jtyoui
    pip install regex==2.5.65
    pip install arrow==0.13.1


### 使用
```python
from jtyoui.time.nlptime import NlpTime

if __name__ == '__main__':
    nt = NlpTime()
    np = nt.parse('今天晚上8点到明天上午10点之间')
    print(np)  # ['2019-12-09 20:00:00', '2019-12-10 10:00:00']
    np = nt.parse('今年儿童节晚上九点一刻')
    print(np)  # ['2019-06-01 21:15:00']
    np = nt.parse('今天中午十二点')
    print(np)  # ['2019-12-09 12:00:00']
    np = nt.parse('明年春节')
    print(np)  # ['2020-01-25 00:00:00']
    np = nt.parse('下下下个星期五早上7点半')
    print(np)  # ['2020-01-3 07:30:00']
```

***
[1]: https://blog.jtyoui.com