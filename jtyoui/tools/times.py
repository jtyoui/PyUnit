#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/24 17:29
# @Author: Jtyoui@qq.com
import re
import datetime
import time
import itertools


class StringTime:
    def __init__(self, sentence):
        self.sentence = sentence
        self.local = time.localtime()
        self.re_year = r'(今年)|(明年)|(后年)|(昨年)|(前年)|(去年)|(\d*年)'
        self.re_mon = r'(上个月)|(这个月)|(下个月)|(上月)|(这月)|(下月)|(\d*月)'
        self.re_day = r'(今天)|(明天)|(后天)|(昨天)|(前天)|(\d*日)|(\d*号)'
        self.re_hour = r'(早上)|(下午)|(\d*点)'
        self.re_min = r'(\d*分)|(\d*点半)'
        self.re_sec = r'(\d*秒)'
        self.now_year = self.local.tm_year
        self.now_mon = self.local.tm_mon
        self.now_day = self.local.tm_mday

    chinese_numerals = {
        '零': '0',
        '一': '1',
        '二': '2',
        '三': '3',
        '四': '4',
        '五': '5',
        '六': '6',
        '七': '7',
        '八': '8',
        '九': '9',
        '两': '2',
    }

    @staticmethod
    def adds(x, fmt):
        add = datetime.datetime.now() + datetime.timedelta(days=x)
        return add.strftime(fmt)

    add_time = {
        '前天': -2,
        '昨天': -1,
        '今天': 0,
        '明天': 1,
        '后天': 2,
        '去年': -1 * 365,
        '前年': -2 * 365,
        '昨年': -1 * 365,
        '今年': 0,
        '明年': 1 * 365,
        '后年': 2 * 365,
        '上个月': -1 * 31,
        '这个月': 0,
        '下个月': 1 * 31,
        '上月': -1 * 31,
        '这月': 0,
        '下月': 1 * 31,
    }

    def find(self, name):
        """根据名字来查找年月日号
        ：:param name:填写：年、月、日、号、来找对应的日期
        """
        if name == '年':
            flag = '%Y'
            re_ = self.re_year
        elif name == '月':
            flag = '%M'
            re_ = self.re_mon
        elif name == '日' or name == '号':
            flag = '%d'
            re_ = self.re_day
        else:
            flag = None
            re_ = ''
        date_time = []
        for d in re.findall(re_, self.sentence):
            for i in d:
                if i:
                    if i in self.add_time:
                        date_time.append(self.adds(self.add_time[i], flag))
                    elif name in i:
                        if i[:-1].isdigit():
                            date_time.append(i[:-1])
        return date_time if date_time else []

    def find_hour(self):
        """找对应的小时"""
        hours = []
        flag = 0
        for d in re.findall(self.re_hour, self.sentence):
            for i in d:
                if i:
                    if i == '早上':
                        flag = 0
                    elif i == '下午':
                        flag = 12
                    else:
                        if i[:-1].isdigit():
                            hours.append(int(i[:-1]) + flag)
                        else:
                            hours.append(0)
        return hours if hours else []

    def find_min(self):
        """找对应的分钟"""
        minute = []
        for d in re.findall(self.re_min, self.sentence):
            for i in d:
                if i:
                    if i[:-1].isdigit():
                        minute.append(int(i[:-1]))
                    elif '半' in i:
                        minute.append(30)
        return minute if minute else []

    def find_sec(self):
        """找对应的秒钟"""
        second = []
        for d in re.findall(self.re_sec, self.sentence):
            if d:
                if d[:-1].isdigit():
                    second.append(d[:-1])
        return second if second else []

    def fine_times(self):
        """ 根据一句话来找对应的时间
        >>> st = StringTime('二零零七年十月三十一号下午2点半')
        >>> print(st.fine_times())
        """
        str_ = [self.chinese_numerals.get(s, s) for s in self.sentence]
        string = ''
        for index, c in enumerate(str_):
            if c == '十':
                if str_[index - 1].isdigit() and str_[index + 1].isdigit():
                    c = ''
                elif str_[index - 1].isdigit() and (not str_[index + 1].isdigit()):
                    c = '0'
                elif not str_[index - 1].isdigit() and str_[index + 1].isdigit():
                    c = '1'
                else:
                    c = '10'
            string += c
        self.sentence = string
        y = self.find('年')
        m = self.find('月')
        d = self.find('号')
        d = d + self.find('日')
        h = self.find_hour()
        mi = self.find_min()
        sec = self.find_sec()
        for y_, m_, d_, h_, mi_, sec_ in itertools.zip_longest(y, m, d, h, mi, sec):
            if not y_ and not m_ and not d_:
                return ''
            if not y_ and m_:
                y_ = self.now_year
            if not m_ and d_:
                if not y_:
                    y_ = self.now_year
                m_ = self.now_mon
            if not mi_:
                mi_ = '00'
            if not sec_:
                sec_ = '00'
            if not m_:
                return f'{y_}'
            elif not d_:
                return f'{y_}-{m_:0>2}'
            elif not h_:
                return f'{y_}-{m_:0>2}-{d_:0>2}'
            else:
                return f'{y_}-{m_:0>2}-{d_:0>2} {h_:0>2}:{mi_:0>2}:{sec_:0>2}'


if __name__ == '__main__':
    st = StringTime('二零零七年十月三十一号下午2点半')
    print(st.fine_times())
