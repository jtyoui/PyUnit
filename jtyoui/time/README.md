# **Time** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 这是一个解析口语化时间模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/口语化时间-Time-black.svg)]()


#### 安装
    pip install jtyoui

### 建议使用NLPTime
[NLP时间处理](https://github.com/jtyoui/Jtyoui/tree/master/jtyoui/time/nlptime)  

### 使用
```python
from jtyoui.time import ParseTime

if __name__ == '__main__':
    today = '2019-10-31 16:00:00' #当前时间
    pt = ParseTime('上上个周星期天下午2点25分钟30秒', today).parse()
    print(pt)  # 2019-10-20 14:25:30

    print('-----------------切换日期------------------')
    st = ParseTime('下周星期一下午2点半开会', today).parse()
    print(st)  # 2019-11-4 14:30:00

    print('----------------多个时间-------------------')
    st = ParseTime('今天下午3点', today).parse()
    print(st)  # 2019-10-31 15:00:00

    print('----------------没有时间-------------------')
    st = ParseTime('我要是不传时间呢？', today).parse()
    print(st)  # 2019-10-31 16:00:00

    print('---------------只有天数--------------------')
    st = ParseTime('明天去哪里？', today).parse()
    print(st)  # 2019-11-1 16:00:00

    print('---------------没有日期或者天数--------------------')
    st = ParseTime('下午2点半开会', today).parse()
    print(st)  # 2019-10-31 14:30:00

    print('---------------*几个月以后--------------------')
    st = ParseTime('下个月1号下午3点', today).parse()
    print(st)  # 2019-11-1 15:00:00

    print('--------------几天之后--------------')
    st = ParseTime('三天之前下午3点', today).parse()
    print(st)  # 2019-10-28 15:00:00

    print('--------------几月底--------------')
    st = ParseTime('明年的2月底之前必须交报告', today).parse()
    print(st)  # 2020-2-28 16:00:00

    print('--------晚上-----------')
    st = ParseTime('3月除', today).parse()
    print(st)  # 2019-3-1 16:00:00

    print('--------下个周几-----------')
    st = ParseTime('下个周2', today).parse()
    print(st)  # 2019-11-5 16:00:00

    print('--------几个月以后的日期--------')
    st = ParseTime('5个月后的明天', today).parse()
    print(st)  # 2020-4-1 16:00:00

    print('------------凌晨或者半夜------------------')
    st = ParseTime('昨天凌晨3点', today).parse()
    print(st)  # 2019-10-31 03:00:00

    print('-------------只说时间-----------------------')
    st = ParseTime('二零零七年八月二十一号下午2点半', today).parse()
    print(st)
```

### 配置文件
    map.ini 是口语化时间的映射表
    re.cfg  是口语化时间的匹配表,支持正则表达式

### 映射表
```ini
[chinese_mon]
零 = 0
正 = 1
一 = 1
二 = 2
两 = 2
三 = 3
四 = 4
五 = 5
六 = 6
七 = 7
八 = 8
九 = 9
十 = 10
冬 = 11
腊 = 12
周 = 星期


[add_year]
去年 = -1
前年 = -2
昨年 = -1
今年 = 0
明年 = 1
后年 = 2

[add_day]
前天 = -2
昨天 = -1
今天 = 0
明天 = 1
后天 = 2

[add_month]
上个月 = -1
这个月 = 0
下个月 = 1
上月 = -1
这月 = 0
下月 = 1

[add_week]
下周 = 1
上周 = -1
下下个周 = 2
下个周 = 1
上个周 = -1
上上个周 = -2
这周 = 0
这个周 = 0
下个星期 = 1
上个星期 = -1
下下个星期 = 2
上上个星期 = -2
这星期 = 0
下星期 = 1
上星期 = -1
下下星期 = 2
上上星期 = -2

[add_hour]
早上 = 0
下午 = 12
晚上 = 12
半夜 = 24
凌晨 = 24
```

### 匹配表
```ini
[re_year]
今年
明年
后年
昨年
前年
去年
\d+年

[re_month]
上个?月
这个?月
下个?月
\d+个?月以?(后|前)
\d{0,2}个?月(底|除)?


[re_day]
今天
明天
后天
昨天
前天
\d+日
\d+号
\d+天\w?(后|前)

[re_week]
上+个?周
下+个?周
(下|上)+个?星期
周\d+

[re_hour]
早上
下午
晚上
半夜
凌晨

[re_minute]
\d+分
\d+点半

[re_second]
\d+秒
```

***
[1]: https://blog.jtyoui.com