# **plunar** [![tyoui](https://github.com/zhangwei0530/logo/blob/master/logo/photolog.png?raw=true)](http://www.jtyoui.com)

[![](https://github.com/zhangwei0530/logo/blob/master/logo/logo.png?raw=true)](http://www.jtyoui.com)

## 这是一个阳历转化农历的程序
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)](https://www.jtyoui.com/)
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)](http://www.tyoui.cn)
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()


#### 介绍
Python版阳历转农历

#### 使用说明

1. git clone https://gitee.com/tyoui/plunar.git
2. from lunar import Lunar
3. print(Lunar('2019-08-15'))



#### 代码使用
    from lunar import Lunar
    if __name__ == '__main__':
        lunar = Lunar('2019-08-15')
        print(lunar.y)  # 农历的年,中文字符 二零一九
        print(lunar.year)  # 农历的年，阿拉伯数字 2019
        print(lunar.m)  # 农历的月份 中文字符 七
        print(lunar.month)  # 农历的月份 阿拉伯字符 7
        print(lunar.d)  # 农历的日期 中文字符 十四
        print(lunar.day)  # 阳历的日期 阿拉伯数字 15 ，注意。和农历不一样
        print(lunar.w)  # 星期几 中文字符
        print(lunar.week)  # 星期几、英文字符
        print(lunar.h)  # 节日
        print(lunar)  # 二零一九年 七月 十四 星期四 无


## 编程语言
[点击查看Python3版本](https://gitee.com/tyoui/plunar)

[点击查看Java8版本](https://gitee.com/tyoui/lunar)