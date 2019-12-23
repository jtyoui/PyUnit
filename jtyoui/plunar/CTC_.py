#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/9 11:47
# @Author: Jtyoui@qq.com

"""
CTC (Chinese traditional calendar)：农历
农历转阳历
"""
from jtyoui.plunar import SC


class CTC:

    def __init__(self, ctc_year, ctc_mon, ctc_day):
        """农历的年、农历的月、农历的日，如果是闰月在月的前面加负号， 比如：闰6月 -6

        :param ctc_year: 农历的年：2017（2017年）
        :param ctc_mon: 农历的月：-6 （闰6月）。6 （6月）
        :param ctc_day: 农历的日：8（初八）
        """
        self.ctc_year = ctc_year
        self.ctc_mon = abs(ctc_mon)
        self.ctc_day = ctc_day
        if ctc_mon < 0:
            self.raw_date = F'{ctc_year}年闰{self.ctc_mon}月{ctc_day}日'
        else:
            self.raw_date = F'{ctc_year}年{self.ctc_mon}月{ctc_day}日'
        self.sc_start_year = ctc_year - 1 if ctc_mon <= 3 else ctc_year
        self.sc_end_year = ctc_year + 1 if ctc_mon >= 10 else ctc_year
        self.sc_start_mon = (ctc_mon + 12 - 3) % 12
        self.sc_end_mon = (ctc_mon + 12 + 3) % 12
        self.sc_start_mon = self.sc_start_mon if self.sc_start_mon else 12
        self.sc_end_mon = self.sc_end_mon if self.sc_end_mon else 12
        self.date = None

    def find_sc(self):
        """返回阳历,如果找不倒返回None"""
        date = []
        if self.sc_start_year == self.sc_end_year:
            for month in range(self.sc_start_mon, self.sc_end_mon + 1):
                date.append(F'{self.ctc_year} {month}')
        else:
            for month in range(self.sc_start_mon, 13):
                date.append(F'{self.sc_start_year} {month}')
            for month in range(1, self.sc_end_mon + 1):
                date.append(F'{self.sc_end_year} {month}')
        for d in date:
            ds = d.split()
            for day in range(1, 32):
                try:
                    sc = SC(int(ds[0]), int(ds[1]), day)
                    sc_string = sc.to_sc()
                    if self.raw_date == sc_string:
                        self.date = [ds[0], ds[1], str(day)]
                        return ds[0] + '年' + ds[1] + '月' + str(day) + '日'
                except ValueError:
                    pass
        return None

    def get_year(self):
        if not self.date:
            if not self.find_sc():
                return '没有找到年'
        return self.date[0]

    def get_month(self):
        if not self.date:
            if not self.find_sc():
                return '没有找到月'
        return self.date[1]

    def get_day(self):
        if not self.date:
            if not self.find_sc():
                return '没有找到日'
        return self.date[2]


if __name__ == '__main__':
    c = CTC(ctc_year=2017, ctc_mon=-6, ctc_day=8)  # 农历的日期2017年闰6月初八
    print(c.find_sc())  # 阳历：2017年7月30日
    print(c.get_year())  # 2017
    print(c.get_month())  # 7
    print(c.get_day())  # 30
