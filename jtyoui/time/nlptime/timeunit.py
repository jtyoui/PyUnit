#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/12/9 13:30
# @Author: Jtyoui@qq.com
from jtyoui.plunar import LunarSolarDateConverter, LunarDate
import regex as re  # pip install regex==2.5.65
import arrow  # pip install arrow==0.13.1
import copy
import jtyoui


class TimePoint:
    def __init__(self):
        """六个字段分别是：年-月-日-时-分-秒，"""
        self.unit = [-1, -1, -1, -1, -1, -1]


class RangeTimeEnum:
    """一天大概范围时间"""
    day_break = 3  # 黎明
    early_morning = 8  # 早
    morning = 10  # 上午
    noon = 12  # 中午、午间
    afternoon = 15  # 下午、午后
    night = 18  # 晚上、傍晚
    lateNight = 20  # 晚、晚间
    midNight = 23  # 深夜

    @classmethod
    def name(cls, names):
        """根据名字获取数据"""
        if hasattr(RangeTimeEnum, names):
            return getattr(RangeTimeEnum, names)
        return 0


class TimeUnit:
    def __init__(self, exp_time, normalizer, context):
        """时间语句分析"""
        self._no_year = False
        self.exp_time = exp_time
        self.normalizer = normalizer
        self.tp = TimePoint()
        self.tp_origin = context
        self.isFirstTimeSolveContext = True
        self.isAllDayTime = True
        self.time = None
        self.time_normalization()

    def time_normalization(self):
        """时间解析"""
        self.norm_set_year()
        self.norm_set_month()
        self.norm_set_day()
        self.norm_set_month_fuzzy_day()
        self.norm_set_base_related()
        self.norm_set_solar_holiday()
        self.norm_set_cur_related()
        self.norm_set_hour()
        self.norm_set_minute()
        self.norm_set_second()
        self.norm_set_special()
        self.norm_set_span_related()
        self.norm_set_lunar_holiday()
        self.modify_time_base()
        self.tp_origin.unit = copy.deepcopy(self.tp.unit)

        # 判断是时间点还是时间区间
        flag = True
        for i in range(0, 4):
            if self.tp.unit[i] != -1:
                flag = False
        if flag:
            self.normalizer.isTimeSpan = True

        if self.normalizer.isTimeSpan:
            days = 0
            if self.tp.unit[0] > 0:
                days += 365 * self.tp.unit[0]
            if self.tp.unit[1] > 0:
                days += 30 * self.tp.unit[1]
            if self.tp.unit[2] > 0:
                days += self.tp.unit[2]
            unit = self.tp.unit
            for i in range(3, 6):
                if self.tp.unit[i] < 0:
                    unit[i] = 0
            seconds = unit[3] * 3600 + unit[4] * 60 + unit[5]
            if seconds == 0 and days == 0:
                self.normalizer.invalidSpan = True
            self.normalizer.timeSpan = self.gen_span(days, seconds)
            return

        time_grid = self.normalizer.timeBase.split('-')
        unit_pointer = 5
        while unit_pointer >= 0 and self.tp.unit[unit_pointer] < 0:
            unit_pointer -= 1
        for i in range(unit_pointer):
            if self.tp.unit[i] < 0:
                self.tp.unit[i] = int(time_grid[i])
        self.time = self.gen_time(self.tp.unit)

    @staticmethod
    def gen_span(days, seconds):
        day = int(seconds / (3600 * 24))
        h = int((seconds % (3600 * 24)) / 3600)
        m = int(((seconds % (3600 * 24)) % 3600) / 60)
        s = int(((seconds % (3600 * 24)) % 3600) % 60)
        return str(days + day) + ' days, ' + "%d:%02d:%02d" % (h, m, s)

    @staticmethod
    def gen_time(unit):
        """得到时间"""
        time = arrow.get('1970-01-01 00:00:00')
        if unit[0] > 0:
            time = time.replace(year=int(unit[0]))
        if unit[1] > 0:
            time = time.replace(month=unit[1])
        if unit[2] > 0:
            time = time.replace(day=unit[2])
        if unit[3] > 0:
            time = time.replace(hour=unit[3])
        if unit[4] > 0:
            time = time.replace(minute=unit[4])
        if unit[5] > 0:
            time = time.replace(second=unit[5])
        return time

    def norm_set_year(self):
        """该方法识别时间表达式单元的年字段"""
        # 一位数表示的年份
        rule = "(?<![0-9])[0-9]{1}(?=年)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.normalizer.isTimeSpan = True
            year = int(match.group())
            self.tp.unit[0] = year

        # 两位数表示的年份
        rule = "[0-9]{2}(?=年)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            year = int(match.group())
            self.tp.unit[0] = year

        # 三位数表示的年份
        rule = "(?<![0-9])[0-9]{3}(?=年)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.normalizer.isTimeSpan = True
            year = int(match.group())
            self.tp.unit[0] = year

        # 四位数表示的年份
        rule = "[0-9]{4}(?=年)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            year = int(match.group())
            self.tp.unit[0] = year

    def norm_set_month(self):
        """该方法识别时间表达式单元的月字段 """
        rule = "((10)|(11)|(12)|([1-9]))(?=月)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.tp.unit[1] = int(match.group())
            # 处理倾向于未来时间的情况
            self.prefer_future(1)

    def norm_set_month_fuzzy_day(self):
        """兼容模糊写法:该方法识别时间表达式单元的月、日字段"""
        rule = "((10)|(11)|(12)|([1-9]))(月|\\.|\\-)([0-3][0-9]|[1-9])"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            match_str = match.group()
            p = re.compile("(月|\\.|\\-)")
            m = p.search(match_str)
            if match is not None:
                start = m.start()
                month = match_str[0: start]
                day = match_str[start + 1:]
                self.tp.unit[1] = int(month)
                self.tp.unit[2] = int(day)
                # 处理倾向于未来时间的情况
                self.prefer_future(1)
            self._check_time(self.tp.unit)

    def norm_set_day(self):
        """该方法识别时间表达式单元的日字段 """
        rule = "((?<!\\d))([0-3][0-9]|[1-9])(?=(日|号))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.tp.unit[2] = int(match.group())
            # 处理倾向于未来时间的情况
            self.prefer_future(2)
            self._check_time(self.tp.unit)

    def daytime(self, rule, name):
        """预测一天是在什么时候

        预测情况包括：
            day_break = 3  # 黎明
            early_morning = 8  # 早
            morning = 10  # 上午
            noon = 12  # 中午、午间
            afternoon = 15  # 下午、午后
            night = 18  # 晚上、傍晚
            lateNight = 20  # 晚、晚间
            midNight = 23  # 深夜

        :param rule: 预测情况的正则
        :param name: 预测的名字
        """
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            if self.tp.unit[3] == -1:  # 增加对没有明确时间点，只写了凌晨这种情况的处理
                self.tp.unit[3] = RangeTimeEnum.name(name)
            elif 12 <= self.tp.unit[3] <= 23:
                self.tp.unit[3] -= 12
            elif self.tp.unit[3] == 0:
                self.tp.unit[3] = 12
            # 处理倾向于未来时间的情况
            self.prefer_future(3)
            self.isAllDayTime = False

    def norm_set_hour(self):
        """该方法识别时间表达式单元的时字段"""
        rule = "(?<!(周|星期))([0-2]?[0-9])(?=(点|时))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.tp.unit[3] = int(match.group())
            # 处理倾向于未来时间的情况
            self.prefer_future(3)
            self.isAllDayTime = False

        # 1.中午/午间0-10点视为12-22点
        # 2.下午/午后0-11点视为12-23点
        # 3.晚上/傍晚/晚间/晚1-11点视为13-23点，12点视为0点
        # 4.0-11点pm/PM视为12-23点
        rule = "凌晨"
        self.daytime(rule, 'day_break')
        rule = "早上|早晨|早间|晨间|今早|明早|早|清晨"
        self.daytime(rule, 'early_morning')
        rule = "上午"
        self.daytime(rule, 'morning')
        rule = "(中午)|(午间)|白天"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            if 0 <= self.tp.unit[3] <= 10:
                self.tp.unit[3] += 12
            if self.tp.unit[3] == -1:  # 增加对没有明确时间点，只写了中午/午间这种情况的处理
                self.tp.unit[3] = RangeTimeEnum.noon
            # 处理倾向于未来时间的情况
            self.prefer_future(3)
            self.isAllDayTime = False

        rule = "(下午)|(午后)|(pm)|(PM)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            if 0 <= self.tp.unit[3] <= 11:
                self.tp.unit[3] += 12
            if self.tp.unit[3] == -1:
                self.tp.unit[3] = RangeTimeEnum.afternoon
            # 处理倾向于未来时间的情况
            self.prefer_future(3)
            self.isAllDayTime = False

        rule = "晚上|夜间|夜里|今晚|明晚|晚|夜里"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            if 0 <= self.tp.unit[3] <= 11:
                self.tp.unit[3] += 12
            elif self.tp.unit[3] == 12:
                self.tp.unit[3] = 0
            elif self.tp.unit[3] == -1:
                self.tp.unit[3] = RangeTimeEnum.lateNight
            # 处理倾向于未来时间的情况
            self.prefer_future(3)
            self.isAllDayTime = False

    def norm_set_minute(self):
        """该方法识别时间表达式单元的分字段 """
        rule = "([0-9]+(?=分(?!钟)))|((?<=((?<!小)[点时]))[0-5]?[0-9](?!刻))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            if match.group() != '':
                self.tp.unit[4] = int(match.group())
                # 处理倾向于未来时间的情况
                self.isAllDayTime = False
        # 加对一刻，半，3刻的正确识别（1刻为15分，半为30分，3刻为45分）
        rule = "(?<=[点时])[1一]刻(?!钟)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.tp.unit[4] = 15
            self.isAllDayTime = False

        rule = "(?<=[点时])半"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.tp.unit[4] = 30
            self.prefer_future(4)
            self.isAllDayTime = False

        rule = "(?<=[点时])[3三]刻(?!钟)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.tp.unit[4] = 45
            self.isAllDayTime = False

    def norm_set_second(self):
        """添加了省略秒说法的时间：如17点15分32"""
        rule = "([0-9]+(?=秒))|((?<=分)[0-5]?[0-9])"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.tp.unit[5] = int(match.group())
            self.isAllDayTime = False

    def norm_set_special(self):
        """该方法识别特殊形式的时间表达式单元的各个字段"""
        rule = "(晚上|夜间|夜里|今晚|明晚|晚|夜里|下午|午后)(?<!(周|星期))([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            rule = '([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]'
            pattern = re.compile(rule)
            match = pattern.search(self.exp_time)
            tmp_target = match.group()
            tmp_parser = tmp_target.split(":")
            if 0 <= int(tmp_parser[0]) <= 11:
                self.tp.unit[3] = int(tmp_parser[0]) + 12
            else:
                self.tp.unit[3] = int(tmp_parser[0])
            self.tp.unit[4] = int(tmp_parser[1])
            self.tp.unit[5] = int(tmp_parser[2])
            self.prefer_future(3)
            self.isAllDayTime = False
        else:
            rule = "(晚上|夜间|夜里|今晚|明晚|晚|夜里|下午|午后)(?<!(周|星期))([0-2]?[0-9]):[0-5]?[0-9]"
            pattern = re.compile(rule)
            match = pattern.search(self.exp_time)
            if match is not None:
                rule = '([0-2]?[0-9]):[0-5]?[0-9]'
                pattern = re.compile(rule)
                match = pattern.search(self.exp_time)
                tmp_target = match.group()
                tmp_parser = tmp_target.split(":")
                if 0 <= int(tmp_parser[0]) <= 11:
                    self.tp.unit[3] = int(tmp_parser[0]) + 12
                else:
                    self.tp.unit[3] = int(tmp_parser[0])
                self.tp.unit[4] = int(tmp_parser[1])
                self.prefer_future(3)
                self.isAllDayTime = False
        if match is None:
            rule = "(?<!(周|星期))([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9](PM|pm|p\\.m)"
            pattern = re.compile(rule, re.I)
            match = pattern.search(self.exp_time)
            if match is not None:
                rule = '([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]'
                pattern = re.compile(rule)
                match = pattern.search(self.exp_time)
                tmp_target = match.group()
                tmp_parser = tmp_target.split(":")
                if 0 <= int(tmp_parser[0]) <= 11:
                    self.tp.unit[3] = int(tmp_parser[0]) + 12
                else:
                    self.tp.unit[3] = int(tmp_parser[0])
                self.tp.unit[4] = int(tmp_parser[1])
                self.tp.unit[5] = int(tmp_parser[2])
                self.prefer_future(3)
                self.isAllDayTime = False
            else:
                rule = "(?<!(周|星期))([0-2]?[0-9]):[0-5]?[0-9](PM|pm|p.m)"
                pattern = re.compile(rule, re.I)
                match = pattern.search(self.exp_time)
                if match is not None:
                    rule = '([0-2]?[0-9]):[0-5]?[0-9]'
                    pattern = re.compile(rule)
                    match = pattern.search(self.exp_time)
                    tmp_target = match.group()
                    tmp_parser = tmp_target.split(":")
                    if 0 <= int(tmp_parser[0]) <= 11:
                        self.tp.unit[3] = int(tmp_parser[0]) + 12
                    else:
                        self.tp.unit[3] = int(tmp_parser[0])
                    self.tp.unit[4] = int(tmp_parser[1])
                    self.prefer_future(3)
                    self.isAllDayTime = False
        if match is None:
            rule = "(?<!(周|星期|晚上|夜间|夜里|今晚|明晚|晚|夜里|下午|午后))([0-2]?[0-9]):[0-5]?[0-9]:[0-5]?[0-9]"
            pattern = re.compile(rule)
            match = pattern.search(self.exp_time)
            if match is not None:
                tmp_target = match.group()
                tmp_parser = tmp_target.split(":")
                self.tp.unit[3] = int(tmp_parser[0])
                self.tp.unit[4] = int(tmp_parser[1])
                self.tp.unit[5] = int(tmp_parser[2])
                self.prefer_future(3)
                self.isAllDayTime = False
            else:
                rule = "(?<!(周|星期|晚上|夜间|夜里|今晚|明晚|晚|夜里|下午|午后))([0-2]?[0-9]):[0-5]?[0-9]"
                pattern = re.compile(rule)
                match = pattern.search(self.exp_time)
                if match is not None:
                    tmp_target = match.group()
                    tmp_parser = tmp_target.split(":")
                    self.tp.unit[3] = int(tmp_parser[0])
                    self.tp.unit[4] = int(tmp_parser[1])
                    self.prefer_future(3)
                    self.isAllDayTime = False
        rule = "[0-9]?[0-9]?[0-9]{2}-((10)|(11)|(12)|([1-9]))-((?<!\\d))([0-3][0-9]|[1-9])"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            tmp_target = match.group()
            tmp_parser = tmp_target.split("-")
            self.tp.unit[0] = int(tmp_parser[0])
            self.tp.unit[1] = int(tmp_parser[1])
            self.tp.unit[2] = int(tmp_parser[2])
        rule = "[0-9]?[0-9]?[0-9]{2}/((10)|(11)|(12)|([1-9]))/((?<!\\d))([0-3][0-9]|[1-9])"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            tmp_target = match.group()
            tmp_parser = tmp_target.split("/")
            self.tp.unit[0] = int(tmp_parser[0])
            self.tp.unit[1] = int(tmp_parser[1])
            self.tp.unit[2] = int(tmp_parser[2])
        rule = "((10)|(11)|(12)|([1-9]))/((?<!\\d))([0-3][0-9]|[1-9])/[0-9]?[0-9]?[0-9]{2}"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            tmp_target = match.group()
            tmp_parser = tmp_target.split("/")
            self.tp.unit[1] = int(tmp_parser[0])
            self.tp.unit[2] = int(tmp_parser[1])
            self.tp.unit[0] = int(tmp_parser[2])
        rule = "[0-9]?[0-9]?[0-9]{2}\\.((10)|(11)|(12)|([1-9]))\\.((?<!\\d))([0-3][0-9]|[1-9])"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            tmp_target = match.group()
            tmp_parser = tmp_target.split(".")
            self.tp.unit[0] = int(tmp_parser[0])
            self.tp.unit[1] = int(tmp_parser[1])
            self.tp.unit[2] = int(tmp_parser[2])

    def norm_set_base_related(self):
        """设置以上文时间为基准的时间偏移计算"""
        if self.tp.unit[0] > 0 and self.tp.unit[1] > 0 and self.tp.unit[2] > 0:
            cur = arrow.get(jtyoui.join('-', self.tp.unit[0:3]), "YYYY-M-D")
        else:
            cur = arrow.get(self.normalizer.timeBase, "YYYY-M-D")
        flag = [False, False, False]
        rule = "\\d+(?=天[以之]?前)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            day = int(match.group())
            cur = cur.shift(days=-day)
        rule = "\\d+(?=天[以之]?后)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            day = int(match.group())
            cur = cur.shift(days=day)
        rule = "\\d+(?=(个)?月[以之]?前)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[1] = True
            month = int(match.group())
            cur = cur.shift(months=-month)
        rule = "\\d+(?=(个)?月[以之]?后)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[1] = True
            month = int(match.group())
            cur = cur.shift(months=month)
        rule = "\\d+(?=年[以之]?前)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[0] = True
            year = int(match.group())
            cur = cur.shift(years=-year)
        rule = "\\d+(?=年[以之]?后)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[0] = True
            year = int(match.group())
            cur = cur.shift(years=year)
        if flag[0] or flag[1] or flag[2]:
            self.tp.unit[0] = int(cur.year)
        if flag[1] or flag[2]:
            self.tp.unit[1] = int(cur.month)
        if flag[2]:
            self.tp.unit[2] = int(cur.day)

    def norm_set_span_related(self):
        """设置时间长度相关的时间表达式"""
        rule = "\\d+(?=个月(?![以之]?[前后]))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.normalizer.isTimeSpan = True
            month = int(match.group())
            self.tp.unit[1] = int(month)
        rule = "\\d+(?=天(?![以之]?[前后]))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.normalizer.isTimeSpan = True
            day = int(match.group())
            self.tp.unit[2] = int(day)
        rule = "\\d+(?=(个)?小时(?![以之]?[前后]))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.normalizer.isTimeSpan = True
            hour = int(match.group())
            self.tp.unit[3] = int(hour)
        rule = "\\d+(?=分钟(?![以之]?[前后]))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.normalizer.isTimeSpan = True
            minute = int(match.group())
            self.tp.unit[4] = int(minute)
        rule = "\\d+(?=秒钟(?![以之]?[前后]))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.normalizer.isTimeSpan = True
            second = int(match.group())
            self.tp.unit[5] = int(second)
        rule = "\\d+(?=(个)?(周|星期|礼拜)(?![以之]?[前后]))"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            self.normalizer.isTimeSpan = True
            week = int(match.group())
            if self.tp.unit[2] == -1:
                self.tp.unit[2] = 0
            self.tp.unit[2] += int(week * 7)

    def norm_set_lunar_holiday(self):
        """识别农历节日和时节"""
        rule = "(中元节)|(端午)|(7夕)|(中和节)|(中秋)|(春节)|(元宵)|(元旦)|(重阳节)|(立春)|(雨水)|(惊蛰)|(春分)|(清明)|(谷雨)|" \
               "(立夏)|(小满 )|(芒种)|(夏至)|(小暑)|(大暑)|(立秋)|(处暑)|(白露)|(秋分)|(寒露)|(霜降)|(立冬)|(小雪)|(大雪)|" \
               "(冬至)|(小寒)|(大寒)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            if self.tp.unit[0] == -1:
                self.tp.unit[0] = int(self.normalizer.timeBase.split('-')[0])
            holiday = match.group()
            holiday = '七夕' if holiday == '7夕' else holiday
            if '节' not in holiday:
                holiday += '节'
            if holiday in self.normalizer.lunar_holiday:
                date = self.normalizer.lunar_holiday[holiday].split('-')
                ls_converter = LunarSolarDateConverter()
                lunar = LunarDate(self.tp.unit[0], int(date[0]), int(date[1]), False)
                solar = ls_converter.lunar_to_solar(lunar)
                self.tp.unit[0] = solar.solarYear
                date[0] = solar.solarMonth
                date[1] = solar.solarDay
            else:
                holiday = holiday.strip('节')
                if holiday in ['小寒', '大寒']:
                    self.tp.unit[0] += 1
                date = self.china_24_st(self.tp.unit[0], holiday)
            self.tp.unit[1] = int(date[0])
            self.tp.unit[2] = int(date[1])

    def norm_set_solar_holiday(self):
        """识别阳历节日"""
        rule = "(情人节)|(母亲节)|(青年节)|(教师节)|(劳动节)|(建党节)|(建军节)|(圣诞节)|(航海节)|(儿童节)|(国庆节)|(植树节)|(重阳节)|(妇女节)|(记者节)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            if self.tp.unit[0] == -1:
                self.tp.unit[0] = int(self.normalizer.timeBase.split('-')[0])
            holiday = match.group()
            if holiday in self.normalizer.solar_holiday:
                date = self.normalizer.solar_holiday[holiday].split('-')
                self.tp.unit[1] = int(date[0])
                self.tp.unit[2] = int(date[1])

    @staticmethod
    def china_24_st(year: int, china_st: str):
        """二十世纪和二十一世纪，24节气计算"""
        if (19 == year // 100) or (2000 == year):
            # 20世纪key值
            st_key = [6.11, 20.84, 4.6295, 19.4599, 6.3826, 21.4155, 5.59, 20.888, 6.318, 21.86, 6.5, 22.2, 7.928,
                      23.65, 8.35, 23.95, 8.44, 23.822, 9.098, 24.218, 8.218, 23.08, 7.9, 22.6]
        else:
            # 21世纪key值
            st_key = [5.4055, 20.12, 3.87, 18.73, 5.63, 20.646, 4.81, 20.1, 5.52, 21.04, 5.678, 21.37, 7.108, 22.83,
                      7.5, 23.13, 7.646, 23.042, 8.318, 23.438, 7.438, 22.36, 7.18, 21.94]
        # 二十四节气字典-- key值, 月份，(特殊年份，相差天数)
        solar_terms = {
            '小寒': [st_key[0], '1', (2019, -1), (1982, 1)],
            '大寒': [st_key[1], '1', (2082, 1)],
            '立春': [st_key[2], '2', (None, 0)],
            '雨水': [st_key[3], '2', (2026, -1)],
            '惊蛰': [st_key[4], '3', (None, 0)],
            '春分': [st_key[5], '3', (2084, 1)],
            '清明': [st_key[6], '4', (None, 0)],
            '谷雨': [st_key[7], '4', (None, 0)],
            '立夏': [st_key[8], '5', (1911, 1)],
            '小满': [st_key[9], '5', (2008, 1)],
            '芒种': [st_key[10], '6', (1902, 1)],
            '夏至': [st_key[11], '6', (None, 0)],
            '小暑': [st_key[12], '7', (2016, 1), (1925, 1)],
            '大暑': [st_key[13], '7', (1922, 1)],
            '立秋': [st_key[14], '8', (2002, 1)],
            '处暑': [st_key[15], '8', (None, 0)],
            '白露': [st_key[16], '9', (1927, 1)],
            '秋分': [st_key[17], '9', (None, 0)],
            '寒露': [st_key[18], '10', (2088, 0)],
            '霜降': [st_key[19], '10', (2089, 1)],
            '立冬': [st_key[20], '11', (2089, 1)],
            '小雪': [st_key[21], '11', (1978, 0)],
            '大雪': [st_key[22], '12', (1954, 1)],
            '冬至': [st_key[23], '12', (2021, -1), (1918, -1)]
        }
        if china_st in ['小寒', '大寒', '立春', '雨水']:
            flag_day = int((year % 100) * 0.2422 + solar_terms[china_st][0]) - int((year % 100 - 1) / 4)
        else:
            flag_day = int((year % 100) * 0.2422 + solar_terms[china_st][0]) - int((year % 100) / 4)
        # 特殊年份处理
        for special in solar_terms[china_st][2:]:
            if year == special[0]:
                flag_day += special[1]
                break
        return (solar_terms[china_st][1]), str(flag_day)

    def norm_set_cur_related(self):
        """设置当前时间相关的时间表达式 """
        if self.tp.unit[0] > 0 and self.tp.unit[1] > 0 and self.tp.unit[2] > 0:
            cur = arrow.get(jtyoui.join('-', self.tp.unit[0:3]), "YYYY-M-D")
        else:
            cur = arrow.get(self.normalizer.timeBase, "YYYY-M-D")
        flag = [False, False, False]
        rule = "前年"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[0] = True
            cur = cur.shift(years=-2)
        rule = "去年"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[0] = True
            cur = cur.shift(years=-1)
        rule = "今年"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[0] = True
            cur = cur.shift(years=0)
        rule = "明年"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[0] = True
            cur = cur.shift(years=1)
        rule = "后年"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[0] = True
            cur = cur.shift(years=2)
        rule = "上*上(个)?月"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[1] = True
            rule = "上"
            pattern = re.compile(rule)
            match = pattern.findall(self.exp_time)
            cur = cur.shift(months=-len(match))
        rule = "(本|这个)月"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[1] = True
            cur = cur.shift(months=0)
        rule = "下*下(个)?月"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[1] = True
            rule = "下"
            pattern = re.compile(rule)
            match = pattern.findall(self.exp_time)
            cur = cur.shift(months=len(match))
        rule = "大*大前天"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            rule = "大"
            pattern = re.compile(rule)
            match = pattern.findall(self.exp_time)
            cur = cur.shift(days=-(2 + len(match)))
        rule = "(?<!大)前天"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            cur = cur.shift(days=-2)
        rule = "昨"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            cur = cur.shift(days=-1)
        rule = "今(?!年)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            cur = cur.shift(days=0)
        rule = "明(?!年)"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            cur = cur.shift(days=1)
        rule = "(?<!大)后天"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            cur = cur.shift(days=2)
        rule = "大*大后天"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            rule = "大"
            pattern = re.compile(rule)
            match = pattern.findall(self.exp_time)
            flag[2] = True
            cur = cur.shift(days=(2 + len(match)))
        rule = "(?<=(上*上上(周|星期)))[1-7]?"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            try:
                week = int(match.group())
            except ValueError:
                week = 1
            week -= 1
            span = week - cur.weekday()
            rule = "上"
            pattern = re.compile(rule)
            match = pattern.findall(self.exp_time)
            cur = cur.replace(weeks=-len(match), days=span)
        rule = "(?<=((?<!上)上(周|星期)))[1-7]?"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            try:
                week = int(match.group())
            except ValueError:
                week = 1
            week -= 1
            span = week - cur.weekday()
            cur = cur.replace(weeks=-1, days=span)
        rule = "(?<=((?<!下)下(周|星期)))[1-7]?"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            try:
                week = int(match.group())
            except ValueError:
                week = 1
            week -= 1
            span = week - cur.weekday()
            cur = cur.replace(weeks=1, days=span)
        rule = "(?<=(下*下下(周|星期)))[1-7]?"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            try:
                week = int(match.group())
            except ValueError:
                week = 1
            week -= 1
            span = week - cur.weekday()
            rule = "下"
            pattern = re.compile(rule)
            match = pattern.findall(self.exp_time)
            cur = cur.replace(weeks=len(match), days=span)
        rule = "(?<=((?<!(上|下|个|[0-9]))(周|星期)))[1-7]"
        pattern = re.compile(rule)
        match = pattern.search(self.exp_time)
        if match is not None:
            flag[2] = True
            try:
                week = int(match.group())
            except ValueError:
                week = 1
            week -= 1
            span = week - cur.weekday()
            cur = cur.replace(days=span)
            cur = self.prefer_future_week(week, cur)
        if flag[0] or flag[1] or flag[2]:
            self.tp.unit[0] = int(cur.year)
        if flag[1] or flag[2]:
            self.tp.unit[1] = int(cur.month)
        if flag[2]:
            self.tp.unit[2] = int(cur.day)

    def modify_time_base(self):
        """该方法用于更新timeBase使之具有上下文关联性"""
        if not self.normalizer.isTimeSpan:
            if 30 <= self.tp.unit[0] < 100:
                self.tp.unit[0] = 1900 + self.tp.unit[0]
            if 0 < self.tp.unit[0] < 30:
                self.tp.unit[0] = 2000 + self.tp.unit[0]
            time_grid = self.normalizer.timeBase.split('-')
            arr = []
            for i in range(0, 6):
                if self.tp.unit[i] == -1:
                    arr.append(str(time_grid[i]))
                else:
                    arr.append(str(self.tp.unit[i]))
            self.normalizer.timeBase = '-'.join(arr)

    def prefer_future_week(self, weekday, cur):
        """预测下一个周的时间

        :param weekday: 星期几
        :param cur: 当前时间
        :return: 预测的时间
        """
        # 1. 确认用户选项
        if not self.normalizer.isPreferFuture:
            return cur
        # 2. 检查被检查的时间级别之前，是否没有更高级的已经确定的时间，如果有，则不进行处理.
        for i in range(0, 2):
            if self.tp.unit[i] != -1:
                return cur
        # 获取当前是在周几，如果识别到的时间小于当前时间，则识别时间为下一周
        tmp = arrow.get(self.normalizer.timeBase, "YYYY-M-D-H-m-s")
        week = tmp.weekday()
        if week > weekday:
            cur = cur.shift(days=7)
        return cur

    def prefer_future(self, check_time_index):
        """如果用户选项是倾向于未来时间，检查check_time_index所指的时间是否是过去的时间，如果是的话，将大一级的时间设为当前时间的+1。

        如在晚上说“早上8点看书”，则识别为明天早上;
        12月31日说3号买菜，则识别为明年1月的3号。
        """
        # 1. 检查被检查的时间级别之前，是否没有更高级的已经确定的时间，如果有，则不进行处理.
        for i in range(0, check_time_index):
            if self.tp.unit[i] != -1:
                return
        # 2. 根据上下文补充时间
        self.check_context_time(check_time_index)
        # 3. 根据上下文补充时间后再次检查被检查的时间级别之前，是否没有更高级的已经确定的时间，如果有，则不进行倾向处理.
        for i in range(0, check_time_index):
            if self.tp.unit[i] != -1:
                return

        # 4. 确认用户选项
        if not self.normalizer.isPreferFuture:
            return
        # 5. 获取当前时间，如果识别到的时间小于当前时间，则将其上的所有级别时间设置为当前时间，并且其上一级的时间步长+1
        time_arr = self.normalizer.timeBase.split('-')
        cur = arrow.get(self.normalizer.timeBase, "YYYY-M-D-H-m-s")
        cur_unit = int(time_arr[check_time_index])
        if self.tp.unit[0] == -1:
            self._no_year = True
        else:
            self._no_year = False
        if cur_unit < self.tp.unit[check_time_index]:
            return
        # 准备增加的时间单位是被检查的时间的上一级，将上一级时间+1
        cur = self.add_time(cur, check_time_index - 1)
        time_arr = cur.format("YYYY-M-D-H-m-s").split('-')
        for i in range(0, check_time_index):
            self.tp.unit[i] = int(time_arr[i])

    def _check_time(self, parse):
        """检查未来时间点"""
        time_arr = self.normalizer.timeBase.split('-')
        if self._no_year:
            if parse[1] == int(time_arr[1]):
                if parse[2] > int(time_arr[2]):
                    parse[0] = parse[0] - 1
            self._no_year = False

    def check_context_time(self, check_time_index):
        """根据上下文时间补充时间信息"""
        for i in range(0, check_time_index):
            if self.tp.unit[i] == -1 and self.tp_origin.unit[i] != -1:
                self.tp.unit[i] = self.tp_origin.unit[i]
        # 在处理小时这个级别时，如果上文时间是下午的且下文没有主动声明小时级别以上的时间，则也把下文时间设为下午
        if self.isFirstTimeSolveContext is True and check_time_index == 3 and \
                self.tp_origin.unit[check_time_index] >= 12 and self.tp.unit[check_time_index] < 12:
            self.tp.unit[check_time_index] += 12
        self.isFirstTimeSolveContext = False

    @staticmethod
    def add_time(cur, fore_unit: int):
        """修改日期

        :param cur: 当前日期
        :param fore_unit: 修改属性
        :return: 修改好的日期
        """
        if fore_unit == 0:
            cur = cur.shift(years=1)
        elif fore_unit == 1:
            cur = cur.shift(months=1)
        elif fore_unit == 2:
            cur = cur.shift(days=1)
        elif fore_unit == 3:
            cur = cur.shift(hours=1)
        elif fore_unit == 4:
            cur = cur.shift(minutes=1)
        elif fore_unit == 5:
            cur = cur.shift(seconds=1)
        return cur
