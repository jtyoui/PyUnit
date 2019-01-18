# **plunar** [![tyoui](https://github.com/zhangwei0530/logo/blob/master/logo/photolog.png?raw=true)](http://www.jtyoui.com)

[![](https://github.com/zhangwei0530/logo/blob/master/logo/logo.png?raw=true)](http://www.jtyoui.com)

## 这是一个阳历转化农历的程序
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)](https://www.jtyoui.com/)
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)](http://www.jtyoui.com)
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-jtyoui.plunar-black.svg)]()

#### 介绍
Python版阳历转农历

#### 安装
    pip install jtyoui

## 使用
```python
    from jtyoui.plunar import Lunar
    
    if __name__ == '__main__':
        lun = Lunar(year=2018, month=1, day=2)
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

## 编程语言
[点击查看Python3版本](https://gitee.com/tyoui/plunar)

[点击查看Java8版本](https://gitee.com/tyoui/lunar)