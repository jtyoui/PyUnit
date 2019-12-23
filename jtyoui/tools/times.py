#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/24 17:29
# @Author: Jtyoui@qq.com
from jtyoui.data import chinese_mon_number, add_time
from jtyoui.decorators import warns
import re
import datetime
import time
import itertools
import copy
import calendar


class StringTime:
    """解析时间

    >>> st = StringTime('二零零七年十月三十一号下午2点半')
    >>> print(st.find_times())

    """

    def __init__(self, sentence, date_str=None, date_format='%Y-%m-%d %H:%M:%S'):
        """传入一个字符串时间和现在时间

        :param sentence: 字符串时间
        :param date_str: 你认为的现在时间，不传默认是当前时间
        :param date_format: 时间格式
        """
        self._sentence = sentence
        self._localtime = date_str if date_str else time.strftime(date_format)
        self.format = date_format
        self.local = time.strptime(self._localtime, self.format)
        self.re_year = r'(今年)|(明年)|(后年)|(昨年)|(前年)|(去年)|(\d+年)'
        self.re_mon = r'(上个?月)|(这个?月)|(下个?月)|(\d{0,2}本?月底?)|(\d*个?月以?后)'
        self.re_day = r'(今天)|(明天)|(后天)|(昨天)|(前天)|(\d+日)|(\d+号)|(\d*天\w?[后前])'
        self.re_week = r'(上个?周)|(下个?周)|(星期日)|(星期天)|(星期\d+)|(周\d+)'
        self.re_hour = r'(早上)|(下午)|(晚上)|(\d+点)'
        self.re_min = r'(\d+分)|(\d+点半)'
        self.re_sec = r'(\d+秒)'
        self.now_year = self.local.tm_year
        self.now_mon = self.local.tm_mon
        self.now_day = self.local.tm_mday
        self.now_week = self.local.tm_wday + 1
        self.chinese_numerals = copy.deepcopy(chinese_mon_number)
        self.chinese_numerals.pop('十')
        self.add_time = add_time
        self.times = set()

    @property
    def sentence(self):
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        self._sentence = sentence

    def adds(self, x, fmt):
        add = datetime.datetime.strptime(self._localtime, self.format) + datetime.timedelta(days=x)
        self.now_year = add.year
        self.now_mon = add.month
        self.now_day = add.day
        self.now_week = add.isoweekday()
        return add.strftime(fmt)

    def find(self, name):
        """根据名字来查找年月日

        :param name: 填写年、月、日、号、来找对应的日期
        """
        if name == '年':
            flag = '%Y'
            re_ = self.re_year
        elif name == '月':
            flag = '%m'
            re_ = self.re_mon
        elif name == '日' or name == '号':
            flag = '%d'
            re_ = self.re_day
        elif name == '周':
            flag = '%d'
            re_ = self.re_week
        else:
            flag = None
            re_ = ''
        date_time, day, add = [], 0, 0
        for d in re.findall(re_, self.sentence):
            for i in d:
                if i:
                    if i in ['星期日', '星期天']:
                        day = 7 - self.now_week
                    elif '星期' in i and i[-1].isdigit():
                        week = int(i[-1])
                        day = week - self.now_week
                    elif '周' in i and len(i) < 3:  # 周三、周四等
                        if i[-1].isdigit():
                            week = int(i[-1])
                            day = week - self.now_week
                        else:
                            add = self.add_time[i]
                    else:
                        if i in self.add_time:
                            date_time.append(self.adds(self.add_time[i], flag))
                        elif re.search(r'\d{1,2}个?月以?后', i):
                            ds = int(i[0]) if i[0].isdigit() else int(i[0:2])
                            self.now_mon = self.now_mon + ds
                        elif name in i and '底' not in i:  # 判断不是xx月底
                            if i[:-1].isdigit():
                                date_time.append(i[:-1])
                        elif '月底' in i:  # 处理xx月底
                            if i[0] == '本':
                                days = calendar.monthrange(self.now_year, self.now_mon)[1]
                                date_time.append(self.now_mon)
                                self._sentence += f'{days}日'
                            elif i[0].isdigit():
                                days = calendar.monthrange(self.now_year, int(i[0]))[1]
                                date_time.append(int(i[0]))
                                self._sentence += f'{days}日'
                            else:  # 既没有xx月也没有本月之类的。暂未考虑
                                pass
                        elif add_time.get(i[1]):
                            if i[0].isdigit():
                                date_time.append(self.adds(int(i[0]), flag))
        if day != 0 or add != 0:
            if add == 0 and date_time:
                days = int(date_time[0]) + day
                date_time = [days]
            else:
                days = self.adds(day + add, flag)
            if int(days) >= self.now_day:
                date_time.append(days)
            else:
                date_time.append(days)
                return date_time, 1
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
                    elif i == '晚上':
                        flag = 12
                    else:
                        if i[:-1].isdigit():
                            if int(i[:-1]) >= 12:
                                hours.append(int(i[:-1]))
                            else:
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

    @warns('该类已经废除、废除时间2019年11月1日（19.10.28版本），请将StringTime类换成ParseTime类使用', DeprecationWarning)
    def find_times(self):
        """根据一句话来找对应的时间"""
        words = re.split(r'[,.，。、?!？！]', self.sentence)
        for sentences_ in words:
            if not sentences_:
                continue
            sentences = re.split(r'[到至-]', sentences_)
            t = re.findall('早上|下午|晚上', sentences[0])
            if t and len(t) == 1:
                sentences = [_ if re.findall('早上|下午|晚上', _) else t[0] + _ for _ in sentences]
            flag_y, flag_m, flag_d = [], [], []  # 临时变量，存放左右连词的性质
            for sentence in sentences:
                str_ = [self.chinese_numerals.get(s, s) for s in sentence] + [' ']  # 加[' ']的原因保证index+1不会出现list索引溢出
                string = ''
                if '十' in str_:
                    for index, c in enumerate(str_):  # 判断十在每个位置上的不同意义
                        if c == '十':
                            if str_[index - 1].isdigit() and str_[index + 1].isdigit():  # 比如：二十一实际上十可以取空，变成21
                                c = ''
                            elif str_[index - 1].isdigit() and (not str_[index + 1].isdigit()):  # 比如：二十实际上十变成0，变成20
                                c = '0'
                            elif not str_[index - 1].isdigit() and str_[index + 1].isdigit():  # 比如：十三实际上十变成1，变成13
                                c = '1'
                            else:
                                c = '10'  # 其余情况十就变成10
                        string += c
                else:
                    string = ''.join(str_)
                if re.search('[上下]个?周[1-6日]', string):
                    string = string.replace('周', '周星期')
                self._sentence = string
                y = self.find('年')  # 找到一句话中的年份
                m = self.find('月')  # 找到一句话中的月份
                d = self.find('号')  # 找到一句话中的天数
                d = d + self.find('日')  # 找到一句话中的天数
                w = self.find('周')  # 找到一句话中的天数
                if isinstance(w, tuple):
                    if m:
                        m[0] = int(m[0]) + w[1]
                    else:
                        m = [self.now_mon + w[1]]
                    d += d + w[0]
                else:
                    d += d + w
                h = self.find_hour()  # 找到一句话中的小时
                mi = self.find_min()  # 找到一句话中的分钟
                sec = self.find_sec()  # 找到一句话中的秒钟
                if not (y or m or d or h or mi or sec):
                    continue
                if not y:
                    y = flag_y
                if not m:
                    m = flag_m
                if not d:
                    d = flag_d
                if h and not d:
                    d = [self.now_day]
                flag_y, flag_m, flag_d = y, m, d
                for y_, m_, d_, h_, mi_, sec_ in itertools.zip_longest(y, m, d, h, mi, sec):
                    if not y_ and m_:
                        y_ = self.now_year
                    if not m_ and d_:
                        if not y_:
                            y_ = self.now_year
                        m_ = self.now_mon
                        add_y, add_m = divmod(m_, 12)
                        y_ += add_y
                        m_ = add_m
                    if not mi_:
                        mi_ = '00'
                    if not sec_:
                        sec_ = '00'
                    if not m_:
                        self.times.add(f'{y_}')
                    elif not d_:
                        self.times.add(f'{y_}-{m_:0>2}')
                    elif not h_:
                        self.times.add(f'{y_}-{m_:0>2}-{d_:0>2}')
                    else:
                        self.times.add(f'{y_}-{m_:0>2}-{d_:0>2} {h_:0>2}:{mi_:0>2}:{sec_:0>2}')
                    break
        times = sorted(self.times)
        self.times.clear()
        return times


if __name__ == '__main__':
    print('-----------------默认是当日期------------------')
    st = StringTime('二零零七年十月三十一号下午2点半')
    print(st.find_times())  # ['2007-10-31 14:30:00']
    st.sentence = '下周星期一下午15点半开会'
    print(st.find_times())  # ['2019-07-08 15:30:00']

    print('-----------------切换日期------------------')
    st = StringTime('下周星期一下午2点半开会', '2019-4-17 00:00:00')
    print(st.find_times())  # ['2019-04-22 14:30:00']

    print('----------------多个时间-------------------')
    st = StringTime('今天下午3点开会到4点整到12楼大会议室开会。')
    print(st.find_times())  # ['2019-07-02 15:00:00', '2019-07-02 16:00:00']

    print('----------------没有时间-------------------')
    st = StringTime('我要是不传时间呢？')
    print(st.find_times())  # []

    print('---------------只有天数--------------------')
    st = StringTime('今天去北京，明天去哪里？')
    print(st.find_times())  # ['2019-07-02', '2019-07-03']

    print('---------------跳断日期--------------------')
    st = StringTime('下周星期一下午2点半到4点开会')
    print(st.find_times())  # ['2019-07-08 14:30:00', '2019-07-08 16:00:00']

    print('---------------非常间断日期--------------------')
    st = StringTime('明天下午2点半一直到下周星期五下午4点开会')
    print(st.find_times())  # ['2019-07-03 14:30:00', '2019-07-12 16:00:00']

    print('---------------没有日期或者天数--------------------')
    st = StringTime('下午2点半开会')
    print(st.find_times())  # ['2019-07-03 14:30:00']

    print('---------------*几个月以后--------------------')
    st = StringTime('请王鹏宇下个月1号下午3点上交财务报表')
    print(st.find_times())  # ['2019-08-01 15:00:00']

    print('--------------几天之后--------------')
    st = StringTime('三天之后下午3点开会')
    print(st.find_times())  # ['2019-07-08 15:00:00']

    print('--------------几月底--------------')
    st = StringTime('明年的2月底之前必须交报告,本月底吃饭')
    print(st.find_times())  # ['2019-07-31', '2020-02-28']

    print('--------晚上-----------')
    st = StringTime('晚上11点20分')
    print(st.find_times())

    print('--------下个周几-----------')
    st = StringTime('下个周2')
    print(st.find_times())

    print('--------几个月以后的日期--------')
    st = StringTime('5个月后的明天')
    print(st.find_times())
