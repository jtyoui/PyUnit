# **PLunar** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]


## 这是一个阳历转化农历的程序
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-jtyoui.plunar-black.svg)]()

#### 介绍
Python版阳历转农历

#### 安装
    pip install jtyoui
    
## 阳历和农历相互转换
```python
from jtyoui.plunar import LunarSolarDateConverter,SolarDate,LunarDate

if __name__ == '__main__':
    converter = LunarSolarDateConverter() #阳历和农历相互转换
    lunar = converter.solar_to_lunar(SolarDate(2019, 12, 6)) #阳历转农历
    print(lunar.get_time()) #{'isleap': False, 'lunarDay': 11, 'lunarMonth': 11, 'lunarYear': 2019}
    solar = converter.lunar_to_solar(LunarDate(2019, 11, 10)) #农历转阳历
    print(solar) #{'solarDay': 5, 'solarMonth': 12, 'solarYear': 2019}
```

## 阳历转农历
```python
from jtyoui.plunar import SC
    
if __name__ == '__main__':
    lun = SC(year=2018, month=1, day=2) #阳历转农历
    print(lun.y)  # 农历的年,中文字符 二零一九
    print(lun.year)  # 农历的年，阿拉伯数字 2019
    print(lun.m)  # 农历的月份 中文字符 七
    print(lun.month)  # 农历的月份 阿拉伯字符 7
    print(lun.d)  # 农历的日期 中文字符 十四
    print(lun.day)  # 阳历的日期 阿拉伯数字 15 ，注意。和农历不一样
    print(lun.w)  # 星期几 中文字符
    print(lun.week)  # 星期几、英文字符
    print(lun.h)  # 节日
    print(lun)  # 二零一九年 七月 十四 星期四 无
```

## 农历转阳历
```python
from jtyoui.plunar import CTC
if __name__ == '__main__':
    c = CTC(ctc_year=2017, ctc_mon=-6, ctc_day=8)  # 农历的日期2017年闰6月初八
    print(c.find_sc())  # 阳历：2017年7月30日
    print(c.get_year())  # 2017
    print(c.get_month())  # 7
    print(c.get_day())  # 30

```


## 批量使用日历
```python
from jtyoui.plunar import BatchCalendar

if __name__ == '__main__':
    BatchCalendar.download_date('temp') #下载数据
    print('-----------------------------')
    # 农历
    print(BatchCalendar.ctc_to_sc('1984年闰十月初三'))  # 农历转阳历 1984年11月25日
    print(BatchCalendar.ctc_to_td('1984年闰十月初三'))  # 农历转天干地支 甲子年乙亥月癸亥日
    print('-----------------------------')
    # 阳历
    print(BatchCalendar.sc_to_ctc('1984年11月25日'))  # 阳历转农历 1984年闰十月初三
    print(BatchCalendar.sc_to_td('1984年11月25日'))  # 阳历转天干地支 甲子年乙亥月癸亥日
    print('-----------------------------')
    # 天干地支
    print(BatchCalendar.td_to_ctc('甲子年乙亥月癸亥日'))  # 天干地支转农历:['1984年闰十月初三', '2044年九月廿一']
    print(BatchCalendar.td_to_sc('甲子年乙亥月癸亥日'))  # 天干地支转阳历:['1984年11月25日', '2044年11月10日']
```



## 编程语言
[点击查看Python3版本](https://gitee.com/tyoui/plunar)

[点击查看Java8版本](https://gitee.com/tyoui/lunar)

[1]: https://blog.jtyoui.com