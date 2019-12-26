#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/9 11:48
# @Author: Jtyoui@qq.com

"""
SC (solar calendar)：阳历
阳历转农历
"""

import time
from jtyoui.data import holiday, week_to_chinese, chinese_mon


class Lunar:
    """阳历转农历

    返回年月日星期和节日

    >>> lun = Lunar(year=2018, month=1, day=2)
    >>> print(lun)  # 二零一九年 七月 十四 星期四 无
    >>> print(lun.y)  # 农历的年,中文字符 二零一九
    >>> print(lun.year)  # 农历的年，阿拉伯数字 2019
    >>> print(lun.m)  # 农历的月份 中文字符 七
    >>> print(lun.month)  # 农历的月份 阿拉伯字符 7
    >>> print(lun.d)  # 农历的日期 中文字符 十四
    >>> print(lun.day)  # 阳历的日期 阿拉伯数字 15 ，注意。和农历不一样
    >>> print(lun.w)  # 星期几 中文字符
    >>> print(lun.week)  # 星期几、英文字符
    >>> print(lun.h)  # 节日
    >>> print(lun)  # 二零一九年 七月 十四 星期四 无
    """

    def __init__(self, year, month, day):
        """
            1980年的数据是： 0x095b0
            二进制：0000 1001 0101 1011 0000
            1-4: 表示当年有无闰年，有的话，为闰月的月份，没有的话，为0。
            5-16：为除了闰月外的正常月份是大月还是小月，1为30天，0为29天。
            注意：从1月到12月对应的是第16位到第5位。
            17-20：表示闰月是大月还是小月，仅当存在闰月的情况下有意义。
        """
        self.date = '{0}-{1:0>2}-{2:0>2}'.format(year, month, day)
        if year > 2050 or year < 1990:
            raise ValueError('输入的范围在1990-2050年之间')
        self.year = 0
        self.month = 0
        self.day = 0
        self.week = 0
        self.leap = False
        self.chinese_week = week_to_chinese
        self.chinese_number = chinese_mon
        self.lunar_info = [
            0x04bd8, 0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950, 0x16554, 0x056a0, 0x09ad0, 0x055d2,
            0x04ae0, 0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540, 0x0d6a0, 0x0ada2, 0x095b0, 0x14977,
            0x04970, 0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54, 0x02b60, 0x09570, 0x052f2, 0x04970,
            0x06566, 0x0d4a0, 0x0ea50, 0x06e95, 0x05ad0, 0x02b60, 0x186e3, 0x092e0, 0x1c8d7, 0x0c950,
            0x0d4a0, 0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0, 0x092d0, 0x0d2b2, 0x0a950, 0x0b557,
            0x06ca0, 0x0b550, 0x15355, 0x04da0, 0x0a5d0, 0x14573, 0x052d0, 0x0a9a8, 0x0e950, 0x06aa0,
            0x0aea6, 0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260, 0x0f263, 0x0d950, 0x05b57, 0x056a0,
            0x096d0, 0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250, 0x0d558, 0x0b540, 0x0b5a0, 0x195a6,
            0x095b0, 0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50, 0x06d40, 0x0af46, 0x0ab60, 0x09570,
            0x04af5, 0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58, 0x055c0, 0x0ab60, 0x096d5, 0x092e0,
            0x0c960, 0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0, 0x0abb7, 0x025d0, 0x092d0, 0x0cab5,
            0x0a950, 0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0, 0x0a5b0, 0x15176, 0x052b0, 0x0a930,
            0x07954, 0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6, 0x0a4e0, 0x0d260, 0x0ea65, 0x0d530,
            0x05aa0, 0x076a3, 0x096d0, 0x04bd7, 0x04ad0, 0x0a4d0, 0x1d0b6, 0x0d250, 0x0d520, 0x0dd45,
            0x0b5a0, 0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0, 0x0aa50, 0x1b255, 0x06d20, 0x0ada0
        ]
        self.lunar()

    def lunar(self):
        date_time = time.strptime(self.date, '%Y-%m-%d')
        # 25538是1900-01-01到1970-01-01的天数，86400是一年的秒数
        total_day = int(time.mktime(date_time) / 86400) + 25538

        # 计算当天是农历第几天
        lunar_year, year_day = 0, 0
        while lunar_year < 2050 - 1900 and total_day > 0:
            year_day = self.year_days(lunar_year)
            total_day -= year_day
            lunar_year += 1

        if total_day < 0:
            total_day += year_day
            lunar_year -= 1

        # 农历年份
        self.year = lunar_year + 1900
        leap_month = self.leap_months(lunar_year)  # 闰哪个月, 1 - 12
        # 用当年的天数offset, 逐个减去每月（农历）的天数，求出当天是本月的第几天
        lunar_month, month_day = 1, 0
        while lunar_month < 13 and total_day > 0:
            # 闰月
            if leap_month > 0 and lunar_month == (leap_month + 1) and (not self.leap):
                lunar_month -= 1
                self.leap = True
                month_day = self.leap_days(lunar_year)
            else:
                month_day = self.month_days(lunar_year, lunar_month)
            total_day -= month_day
            # 解除闰月
            if self.leap and lunar_month == (leap_month + 1):
                self.leap = False
            lunar_month += 1

        # offset为0时，并且刚才计算的月份是闰月，要校正
        if total_day == 0 and leap_month > 0 and lunar_month == leap_month + 1:
            leap = False if self.leap else True
            if leap:
                lunar_month -= 1
        # offset小于0时，也要校正
        if total_day < 0:
            total_day += month_day
            lunar_month -= 1
        self.month = lunar_month
        self.day = total_day + 1
        self.week = time.strftime('%a', date_time)

    def year_days(self, lunar_year):
        i, sum_day = 0x8000, 348
        while i > 0x8:
            if (self.lunar_info[lunar_year] & i) != 0:
                sum_day += 1
            i >>= 1
        return sum_day + self.leap_days(lunar_year)

    def leap_months(self, lunar_year):
        return int(self.lunar_info[lunar_year] & 0xf)

    def leap_days(self, lunar_year):
        if self.leap_months(lunar_year) != 0:
            return 30 if (self.lunar_info[lunar_year] & 0x10000) != 0 else 29
        return 0

    def month_days(self, lunar_year, lunar_month):
        return 29 if (self.lunar_info[lunar_year] & (0x10000 >> lunar_month)) == 0 else 30

    def get_china_day(self, d):
        chinese_ten = ['初', '十', '廿', '卅']
        n = 9 if d % 10 == 0 else (d % 10 - 1)
        if d == 10:
            return '初十'
        elif n == 0:
            return chinese_ten[d // 10] + '一'
        else:
            return chinese_ten[d // 10] + self.chinese_number[n + 1]

    def get_holiday(self, date):
        x = holiday.get(date[5:])
        if x:
            return x
        else:
            z = holiday.get(self.chinese_number[self.month - 1] + '月' + self.get_china_day(self.day))
            return z if z else '无'

    def __str__(self):
        """返回字符串数据

        :return: 年 月 日 星期 节日(没有是无)
        """
        if self.leap:
            return self.y + '年 闰' + self.m + '月 ' + self.d + ' ' + self.w + ' 节日：' + self.h
        else:
            return self.y + '年 ' + self.m + '月 ' + self.d + ' ' + self.w + ' 节日：' + self.h

    def __getattr__(self, item):
        if item == 'y':
            y = ''
            for i in range(3, -1, -1):
                y += self.chinese_number[self.year // (10 ** i) % 10]
            return y.replace('正', '一')
        elif item == 'm':
            return self.chinese_number[self.month]
        elif item == 'd':
            return self.get_china_day(self.day)
        elif item == 'w':
            return self.chinese_week.get(self.week)
        elif item == 'h':
            return self.get_holiday(self.date)

    def to_sc(self):
        """年 月 日 """
        if self.leap:
            return str(self.year) + '年闰' + str(self.month) + '月' + str(self.day) + '日'
        else:
            return str(self.year) + '年' + str(self.month) + '月' + str(self.day) + '日'

    def __repr__(self):
        return self.__str__()


SC = Lunar

if __name__ == '__main__':
    lun = Lunar(year=2019, month=12, day=27)
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
