# **Data** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 这是一个数据集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-数据-black.svg)]()


#### 安装
    pip install jtyoui

### 使用
```python
from jtyoui.data import *
if __name__ == '__main__':
    download_gitee('logo', 'logo.png', 'D:\\')  # 将照片logo.png下载到D盘
    pillow = fetch_gitee('logo', 'logo.png')  # 返回PIL.image类型数据
```

### 省份名字
```python
from jtyoui.data import province
if __name__ == '__main__':
        print(province.GuiZhou) #获取贵州省下面的市名字
        print(province.Province) # 获取全国省名字

```

### 获取常见的值

1.  [常见的照片格式](https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/constant.py)
2.  [常见的文字编码格式](https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/constant.py)
3.  [数学符号](https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/constant.py)
4.  [将英文的星期转为中文](https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/constant.py)
5.  [将中文的星期转为英文](https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/constant.py)
6.  [将英文的月份转为中文](https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/constant.py)
7.  [将中文的月份转为英文](https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/constant.py)
8.  [翻译http转态码的含义](https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/constant.py)


### 获得火车站信息
```python
import jtyoui
if __name__ == '__main__':
    print(jtyoui.Train_Station['安顺'])  # 查看安顺火车站是哪个省
    desc = jtyoui.find_train_desc('安顺火车站')  # 查看安顺火车站的摘要
    print(desc)
    info = jtyoui.find_train_info('安顺站')  # 查询安顺火车站的基本信息
    print(info)
    di = desc_info = jtyoui.find_train_desc_info('宋')
    print(di)

```

### 获得时区
```python
if __name__ == '__main__':
    import datetime
    import pytz
    import jtyoui
    print(datetime.datetime.now(tz=pytz.timezone(jtyoui.TZ.Asia_BeiJing))) #设置北京时区
```

### 获取天气预报
```python
if __name__ == '__main__':
    import pprint
    import jtyoui
    w = jtyoui.WeatherForecast()
    w.set_city('九龙')
    pprint.pprint(w.get_today_weather())  # 获得当天 天气预报
    pprint.pprint(w.get_7day_weather())  # 获得7天天气预报
    pprint.pprint(w.get_15day_weather())  # 获得15天天气预报

```



***
[1]: https://blog.jtyoui.com