#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/21 15:08
# @Author: Jtyoui@qq.com
from jtyoui.decorators import parameter_set_length
from collections import Counter

"""
肯德尔相关性系数
肯德尔相关系数是以Maurice Kendall命名的，并经常用希腊字母τ（tau）表示其值。
肯德尔相关系数是一个用来测量两个随机变量相关性的统计值。
一个肯德尔检验是一个无参数假设检验，它使用计算而得的相关系数去检验两个随机变量的统计依赖性。
肯德尔相关系数的取值范围在-1到1之间，当τ为1时，表示两个随机变量拥有一致的等级相关性；
当τ为-1时，表示两个随机变量拥有完全相反的等级相关性；当τ为0时，表示两个随机变量是相互独立的

举个例子。比如评委对选手的评分（优、中、差等），我们想看两个（或者多个）评委对几位选手的评价标准是否一致；
或者医院的尿糖化验报告，想检验各个医院对尿糖的化验结果是否一致，这时候就可以使用肯德尔相关性系数进行衡量。
"""


@parameter_set_length
def kendall_coefficient(sample_x, sample_y):
    """肯德尔相关性系数

    其中C表示XY中拥有一致性的元素对数（两个元素为一对）；D表示XY中拥有不一致性的元素对数。
    n1,n2,n3可以参考 https://blog.csdn.net/wsywl/article/details/5889419

    :param sample_x: 数据集合
    :param sample_y: 数据集合
    :return: 两个集合的肯德尔相关性系数
    """
    if not (isinstance(sample_y, set) and isinstance(sample_x, set)):
        set_x, set_y = set(sample_x), set(sample_y)
    else:
        set_x, set_y = sample_x, sample_y
    n = len(sample_x)
    intersection = set_x.intersection(set_y)  # 交集
    c = len(intersection)  # 一致性的元素个数
    union = set_x.union(set_y)  # 并集
    d = len(union) - c  # 不一致性的元素个数
    n3 = n * (n - 1) / 2
    count_x, count_y = Counter(sample_x), Counter(sample_y)
    n1, n2 = 0, 0
    for i in intersection:
        n1 += count_x.get(i) * (count_x.get(i) - 1) / 2  # x中第i个小集合所包含的元素数
        n2 += count_y.get(i) * (count_y.get(i) - 1) / 2  # y中第i个小集合所包含的元素数
    return (c - d) * 2 / (pow((n3 - n1) * (n3 - n2), 0.5))


if __name__ == '__main__':
    print(kendall_coefficient([3, 1, 2, 2, 1, 3], [1, 2, 3, 2, 1, 1]))
