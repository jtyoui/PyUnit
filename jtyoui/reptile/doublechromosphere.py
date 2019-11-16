#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/11/16 19:35:00
# @Email : jtyoui@qq.com
# @Software : PyCharm
from jtyoui.error import MathValueWarning
from jtyoui.web import get
import re


def double_data_chart(start, end):
    """爬取双色球数据,第一列数据是信息头。
    :param start:开始期号
    :param end:结束期号
    :return:二维列表
    """
    header = ['期号', '红球1', '红球2', '红球3', '红球4', '红球5', '红球6', '篮球', '奖池',
              '一等奖注数', '一等奖奖金', '二等奖注数', '二等奖奖金', '总投注额', '开奖日期']
    ls = [header]
    assert 3001 <= start < end, MathValueWarning('双色球的开始时间范围在：[03001-现在)')
    url = f'https://datachart.500.com/ssq/history/newinc/history.php?start={start}&end={end}'
    data = get(url)
    response = data.content.decode('utf-8')
    for charts in re.findall(r'<tr class="t_tr1">.+?</tr>', response):
        td = re.findall('<td.*?>(.+?)</td>', charts)
        td.pop(9)
        m = map(lambda x: x if '-' in x else int(x.replace(',', '')), td[1:])
        ls.append(list(m))
    return ls


if __name__ == '__main__':
    dc = double_data_chart(3001, 19131)
    print(dc)
