#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/11/16 19:35:00
# @Email : jtyoui@qq.com
# @Software : PyCharm
from jtyoui.web import get
import re


def double_data_chart(start=None, end=None):
    """爬取双色球数据,第一列数据是信息头

    :param start: 开始期号：默认是第一期时间
    :param end: 结束期号：默认是现在时间
    :return: 二维列表
    """
    if start is None and end is None:
        return double_data_chart(*_get_start_end())
    header = ['期号', '红球1', '红球2', '红球3', '红球4', '红球5', '红球6', '篮球', '奖池',
              '一等奖注数', '一等奖奖金', '二等奖注数', '二等奖奖金', '总投注额', '开奖日期']
    ls = [header]
    url = f'https://datachart.500.com/ssq/history/newinc/history.php?start={start}&end={end}'
    data = get(url)
    response = data.content.decode('utf-8')
    for charts in re.findall(r'<tr class="t_tr1">.+?</tr>', response):
        td = re.findall('<td.*?>(.+?)</td>', charts)
        td.pop(9)
        m = map(lambda x: x if '-' in x else int(x.replace(',', '')), td[1:])
        ls.append(list(m))
    return ls


def _get_start_end():
    """获取开始期号和结束期号"""
    url = 'https://datachart.500.com/ssq/history/history.shtml'
    data = get(url)
    response = data.content.decode('gbk')
    search = re.search('<input id="end" name="end" value="(.+?)" size="10" />', response)
    start, end = search.start() + 34, search.end() - 14
    return 3001, response[start:end]


if __name__ == '__main__':
    print(double_data_chart())
