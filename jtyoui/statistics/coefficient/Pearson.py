#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/21 15:04
# @Author: Jtyoui@qq.com
from jtyoui.decorator import parameter_set_length

"""
皮尔森相关性系数
Pearson相关系数是用来衡量两个数据集合是否在一条线上面，它用来衡量定距变量间的线性关系。
相关系数 0.8-1.0 极强相关
0.6-0.8 强相关
0.4-0.6 中等程度相关
0.2-0.4 弱相关
0.0-0.2 极弱相关或无相关
就好比我们想研究人跑步的速度与心脏跳动的相关性，如果你无论跑多快，
心跳都不变（即心跳这个变量的标准差为0），或者你心跳忽快忽慢的，
却一直保持一个速度在跑（即跑步速度这个变量的标准差为0），
那我们都无法通过皮尔森相关性系数的计算来判断心跳与跑步速度到底相不相关。
"""


def expect(data):
    """计算data数据的数学期望"""
    return sum(data) / len(data)


@parameter_set_length
def pearson_coefficient(sample_x, sample_y):
    """
    皮尔森相关性系数
    :param sample_x: x样本数据变量集合
    :param sample_y: y样本数据变量集合
    :return:x和y的相关系数
    """
    xy = [x * y for x, y in zip(sample_x, sample_y)]
    square_x = [x ** 2 for x in sample_x]
    square_y = [y ** 2 for y in sample_y]
    numerator = expect(xy) - expect(sample_x) * expect(sample_y)
    denominator = (expect(square_x) - expect(sample_x) ** 2) * (expect(square_y) - expect(sample_y) ** 2)
    return numerator / pow(denominator, 0.5)


if __name__ == '__main__':
    print(pearson_coefficient([1, 2, 3, 4, 5, 6], [0.3, 0.9, 2.7, 2, 3.5, 5]))
