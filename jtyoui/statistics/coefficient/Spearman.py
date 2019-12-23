#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/21 15:07
# @Author: Jtyoui@qq.com
from jtyoui.decorators import parameter_set_length

"""
斯皮尔曼相关系数
在统计学中, 以查尔斯·斯皮尔曼命名的斯皮尔曼等级相关系数，即SpearMan相关系数。
经常用希腊字母ρ表示。 它是衡量两个变量的依赖性的 非参数 指标。
它利用单调方程评价两个统计变量的相关性。 如果数据中没有重复值，
并且当两个变量完全单调相关时，斯皮尔曼相关系数则为+1或−1。
"""


@parameter_set_length
def spear_man_coefficient(sample_x, sample_y):
    """斯皮尔曼相关系数

    :param sample_x: x样本数据变量集合
    :param sample_y: y样本数据变量集合
    :return: x和y的相关系数
    """
    n = len(sample_x)
    sort_x = sorted(sample_x)  # 排序
    sort_y = sorted(sample_y)
    dict_x = dict(zip(sort_x, range(n)))  # 排序的字典
    dict_y = dict(zip(sort_y, range(n)))
    rank_x = [dict_x.get(x) for x in sample_x]  # x的秩
    rank_y = [dict_y.get(y) for y in sample_y]
    rank = [(x - y) ** 2 for x, y in zip(rank_x, rank_y)]  # 每一个秩的平方
    return 1 - 6 * sum(rank) / (n * (pow(n, 2) - 1))


if __name__ == '__main__':
    print(spear_man_coefficient((11, 490, 14, 43, 30, 3), (2, 75, 3, 44, 7, 42)))
