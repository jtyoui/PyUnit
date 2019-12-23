#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/10/31 13:21
# @Author: Jtyoui@qq.com
from jtyoui.data import reader_conf
import time
import configparser
import os
import datetime
import re

NOW_TIME = time.localtime(time.time())


class ParseTime:

    def __init__(self, data, current_date=None, date_format='%Y-%m-%d %H:%M:%S', **kwargs):
        """初始化数据日期

        :param data: 当前数据
        :param current_date: 当前日期
        :param date_format: 日期解析格式
        :param kwargs: 其他参数
            -  map_path: 解析日期的映射表
            -  re_path: 匹配日期的正则表
        """
        # 加载日期的映射表和匹配日期的正则表
        self.map, self.re = None, None
        self.load_config(**kwargs)

        self.data = data + '\033'
        self._decide_ten()
        # 定义当前日期
        self.localtime = current_date if current_date else time.strftime(date_format)

        self.format = date_format

        # 将当前日期标准化
        local = time.strptime(self.localtime, self.format)

        # 初始化当前的年月日基本信息
        self.now_year = local.tm_year
        self.now_mon = local.tm_mon
        self.now_day = local.tm_mday
        self.now_week = local.tm_wday + 1
        if current_date:
            self.now_hour = local.tm_hour
            self.now_minute = local.tm_min
            self.now_second = local.tm_sec
        else:
            self.now_hour = 0
            self.now_minute = 0
            self.now_second = 0

        self.reduction = True  # 启动还原时分秒

    def load_config(self, map_path=None, re_path=None):
        """自定义日期解析映射表和匹配日期的正则表

        :param map_path: 解析日期的映射表
        :param re_path: 匹配日期的正则表
        """
        path = os.path.dirname(__file__)
        self.map = configparser.ConfigParser()
        if map_path:
            self.map.read(map_path, encoding='UTF-8')
        else:
            self.map.read(path + os.sep + 'map.ini', encoding='UTF-8')
        if re_path:
            self.re = reader_conf(re_path)
        else:
            self.re = reader_conf(path + os.sep + 're.cfg')

    def change_time(self, day=0, hour=0, minute=0, week=0, second=0):
        """增加天数来修改时间"""
        add_time = datetime.timedelta(days=day, hours=hour, minutes=minute, weeks=week, seconds=second)
        if self.reduction:
            change = F'{self.now_year}-{self.now_mon}-{self.now_day} 00:00:00'  # 时分秒还原到0
            self.reduction = False
        else:
            change = self.str_time()
        add = datetime.datetime.strptime(change, self.format) + add_time
        self.now_year = add.year
        self.now_mon = add.month
        self.now_day = add.day
        self.now_hour = add.hour
        self.now_minute = add.minute
        self.now_second = add.second
        self.now_week = add.isoweekday()

    def _analysis(self, name):
        """分析数据获取年月日周时分秒中的有效信息

        :param name: 年月日时周分秒调用名字
        :return: 改变的值
        """
        re_year = '|'.join(self.re['re_' + name])
        ls = re.search(re_year, self.data)
        if ls is not None:
            message = ls.group()
            add_year = self.map['add_' + name]
            value = add_year.get(message, 0)
        else:
            value = 0
        return int(value)

    def standard_time(self):
        """标准时间化"""
        return time.strptime(self.str_time(), self.format)

    def str_time(self):
        """字符串时间"""
        return self.__str__()

    def day(self):
        """查询天数"""
        value = self._analysis('day')
        if value == 0:
            re_year = '|'.join(self.re['re_day'])
            change_day = re.search(re_year, self.data)
            if change_day:
                message = change_day.group()
                if message[:-1].isdigit():
                    self.now_day = message[:-1]
                elif '后' in message:
                    value = int(message[:message.find('天')])
                elif '前' in message:
                    value = -int(message[:message.find('天')])
        self.change_time(day=value)

    def month(self):
        """查询月份"""
        value = self._analysis('month')
        if value == 0:
            re_month = '|'.join(self.re['re_month'])
            change_month = re.search(re_month, self.data)
            if change_month:
                message = change_month.group()
                if '个月' in message:
                    point = message[:message.find('个')]
                else:
                    point = message[:message.find('月')]
                if point.isdigit():
                    point = int(point)
                    if '底' in message:
                        self.now_mon = point + 1
                        self.now_day = 1
                        self.change_time(day=-1)
                    elif '除' in message:
                        self.now_mon = point
                        self.now_day = 1
                    elif '后' in message:
                        value = point
                    elif '前' in message:
                        value = -point
                    else:
                        self.now_mon = point
        if value:
            mon = self.now_mon + value
            if mon == 0:
                self.now_year -= 1
                mon = 12
            if mon > 12:
                over_12_mon, mod_12 = divmod(mon, 12)
                self.now_year += over_12_mon
                self.now_mon = mod_12
            else:
                self.now_mon = mon

    def year(self):
        """查询年份"""
        value = self._analysis('year')
        if value == 0:
            re_year = '|'.join(self.re['re_year'])
            change_year = re.search(re_year, self.data)
            if change_year:
                message = change_year.group()
                if message[:-1].isdigit():
                    self.now_year = int(message[:-1])
        else:
            self.now_year += value

    def week(self):
        """查找第几个周"""
        value = self._analysis('week')
        self.change_time(week=value)

    def what_week(self):
        """查找当前周中的第几个星期"""
        ds = self.map['chinese_number']
        keys = r'星期(\d+|' + '|'.join(ds.keys())[4:-11] + '天|日)'
        match = re.search(keys, self.data)
        if match is not None:
            value = match.group()
            point = value[2:]
            if point.isdigit():
                w = int(point)
            elif ds.get(point, None) is not None:
                w = int(ds[point])
            elif point in '天日':
                w = 7
            else:
                w = self.now_week  # 暂未设置
            differ = w - self.now_week
            self.change_time(day=differ)

    def hour(self):
        """查找当前的小时"""
        re_hour = '(' + '|'.join(self.re['re_hour']) + ')' + r'\d+点'
        match = re.search(re_hour, self.data)
        if match is not None:
            value = match.group()
            add_hour = int(value[2:-1])
            point = value[:2]
            sc = int(self.map['add_hour'].get(point, 0))
            if add_hour < sc:
                if '凌晨' in value and add_hour == 12:
                    add_hour = sc  # 凌晨12点等于凌晨0点
                else:
                    add_hour += sc
            self.change_time(hour=add_hour)
        else:
            self.reduction = False

    def minute(self):
        """查找当前的分钟"""
        re_minute = '|'.join(self.re['re_minute'])
        match = re.search(re_minute, self.data)
        if match is not None:
            value = match.group()
            if '点半' in value:
                add_min = 30
            elif '分' in value:
                add_min = int(value[:-1])
            else:
                add_min = 0  # 其他情况
            self.change_time(minute=add_min)

    def second(self):
        """查找当前的秒钟"""
        re_second = '|'.join(self.re['re_second'])
        match = re.search(re_second, self.data)
        if match is not None:
            value = match.group()
            if '秒' in value:
                add_second = int(value[:-1])
                self.change_time(second=add_second)

    def parse(self):
        """开始解析，返回解析后的标准时间"""
        self.second()
        self.minute()
        self.hour()
        self.week()
        self.what_week()
        self.day()
        self.month()
        self.year()
        return self

    def find_times(self):
        """同StringTime.find_times中的一样"""
        return [self.parse().__str__()]

    def _decide_ten(self):
        """重新映射一些词语"""
        chinese_number = self.map['chinese_number']
        str_ = list()
        for data in self.data:
            if data == '周':
                # 如果又有周又有星期，不改变
                if '星期' in self.data:
                    str_.append(data)
                else:  # 否则将周改为星期
                    str_.append(self.map['chinese_number'].get(data, data))
            elif data != '十' and data in chinese_number:  # 十为特殊符号
                str_.append(self.map['chinese_number'][data])
            else:
                str_.append(data)
        if '十' in str_:
            # 判断十在每个位置上的不同意义
            for index, c in enumerate(str_):
                if c == '十':
                    if str_[index - 1].isdigit() and str_[index + 1].isdigit():  # 比如：二十一实际上十可以取空，变成21
                        str_[index] = ''
                    elif str_[index - 1].isdigit() and (not str_[index + 1].isdigit()):  # 比如：二十实际上十变成0，变成20
                        str_[index] = '0'
                    elif not str_[index - 1].isdigit() and str_[index + 1].isdigit():  # 比如：十三实际上十变成1，变成13
                        str_[index] = '1'
                    else:
                        str_[index] = '10'  # 其余情况十就变成10
        self.data = ''.join(str_[:-1])

    def __add__(self, other):
        """两个时间对象相加"""
        pass

    def __mul__(self, other):
        """两个时间对象相减"""
        pass

    def __str__(self):
        """字符串格式化"""
        return F'{self.now_year}-{self.now_mon}-{self.now_day} ' \
               F'{self.now_hour:0>2}:{self.now_minute:0>2}:{self.now_second:0>2}'


if __name__ == '__main__':
    today = '2019-10-31 16:00:00'
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
    print(st)  # 2007-8-21 14:30:00
