#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/21 15:04
# @Author: Jtyoui@qq.com
from jtyoui.decorators import parameter_set_length
from jtyoui.statistics.analysis import AnalysisMath, cov

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


@parameter_set_length
def pearson_coefficient(sample_x, sample_y):
    """皮尔森相关性系数

    :param sample_x: x样本数据变量集合
    :param sample_y: y样本数据变量集合
    :return: x和y的相关系数
    """
    ana = AnalysisMath()  # 数学分析模块
    numerator = cov(sample_x, sample_y)  # 分子是协方差
    denominator = pow(ana.variance(sample_x) * ana.variance(sample_y), 0.5)  # 分母是两个方差的积开平方
    return numerator / denominator


if __name__ == '__main__':
    print(pearson_coefficient([1, 2, 3, 4, 5, 6], [0.3, 0.9, 2.7, 2, 3.5, 5]))
