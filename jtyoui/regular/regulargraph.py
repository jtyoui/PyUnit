#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/1/19 16:16
# @Author: Jtyoui@qq.com
import os
import regex as re  # pip install regex


class RegularGraph:
    """正则解析器：解析格式包括sqlite3和execl格式"""

    def __init__(self, path):
        self.re = []
        suffix = os.path.splitext(path)[1]
        if path and isinstance(path, str) and os.path.exists(path):
            if '.xls' == suffix or '.xlsx' == suffix:
                import xlrd  # pip install xlrd==1.2.0
                read = xlrd.open_workbook(path)
                table = read.sheets()[0]
                for x in range(2):
                    row = table.row_values(x)
                    self.re.append(row)
            elif '.sqlite' == path:
                pass
            else:
                raise TypeError('类型异常，只支持sqlite3和execl格式')

    def parse(self, string):
        """正则匹配"""
        result = {}
        for name, rule in self.re:
            match = re.search(rule, string)
            if match:
                result[name] = match.group()
        return result


if __name__ == '__main__':
    r = RegularGraph('re.xlsx')
    print(r.parse('我的车是贵AU1234'))
