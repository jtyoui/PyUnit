#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/12/9 10:19
# @Author: Jtyoui@qq.com
from jtyoui.data import replace, chinese_mon_number
from jtyoui.time.nlptime.dateRe import DATE_RE, Solar_Holiday, Lunar_Holiday
from jtyoui.time.nlptime.timeunit import TimeUnit, TimePoint
import re
import time


class NlpTime:
    def __init__(self):
        self.pattern = re.compile(DATE_RE)
        self.timeBase = None
        self.solar_holiday = Solar_Holiday
        self.lunar_holiday = Lunar_Holiday
        self.isTimeSpan = False

    def parse(self, target, time_base=None) -> list:
        self.timeBase = replace(r'\W+', '-', time_base) if time_base else time.strftime('%Y-%m-%d-%H-%M-%S')
        times = []
        input_query = self._filter(target)
        time_token = self._ex(input_query)
        for res in time_token:
            times.append(res.time.format("YYYY-MM-DD HH:mm:ss"))
        return times

    @staticmethod
    def _filter(word) -> str:
        """对一些不规范的表达做转换"""
        for k, v in chinese_mon_number.items():
            if k == '十':
                continue
            word = word.replace(k, v)
        pattern = re.compile("(?:周|星期)[末天日]")
        match = pattern.finditer(word)
        for m in match:
            word = word.replace(m.group(), '7')

        pattern = re.compile("[0-9]?十[0-9]?")
        match = pattern.finditer(word)
        for m in match:
            group = m.group()
            s = group.split("十")
            ten, end = int(s[0]) if s[0] else 0, int(s[1]) if s[1] else 0
            if ten == 0:
                ten = 1
            num = ten * 10 + end
            word = word.replace(m.group(), str(num))

        input_query = re.sub('\\s+', '', word)
        match = re.search("[0-9]月[0-9]", input_query)
        if match is not None:
            index = input_query.find('月')
            match = re.search("[日号]", input_query[index:])
            if match is None:
                match = re.search("[0-9]月[0-9]+", input_query)
                if match is not None:
                    end = match.span()[1]
                    input_query = input_query[:end] + '号' + input_query[end:]
        match = re.search("月", input_query)
        if match is None:
            input_query = input_query.replace('个', '')
        replaces = {'中旬': '15号', '傍晚': '午后', '大年': '', '五一': '劳动节', '白天': '早上', '：': ':'}
        for k, v in replaces.items():
            input_query = input_query.replace(k, v)
        return input_query

    def _ex(self, word):
        temp, start, end = [], -1, -1
        match = self.pattern.finditer(word)
        for m in match:
            start = m.start()
            if start == end:
                temp[-1] += m.group()
            else:
                temp.append(m.group())
            end = m.end()
        res = []
        context_tp = TimePoint()
        for t in temp:
            res.append(TimeUnit(t, self, context_tp))
            context_tp = res[-1].tp
        return res


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
