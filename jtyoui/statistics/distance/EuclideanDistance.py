#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:32
# @Author: Jtyoui@qq.com

from jtyoui.error import CoordinateLengthNotEqualError
import math

"""
欧氏距离
欧氏距离是最容易直观理解的距离度量方法，
我们小学、初中和高中接触到的两个点在空间中的距离一般都是指欧氏距离。
"""


def euclidean_distance(coordinate_p, coordinate_q):
    """
    欧氏距离
    :param coordinate_p: p坐标
    :param coordinate_q: q坐标
    :return: 欧氏距离值
    """
    if len(coordinate_q) != len(coordinate_p):
        raise CoordinateLengthNotEqualError("坐标长度不一致")
    numerator = 0
    for x, y in zip(coordinate_p, coordinate_q):
        numerator += (x - y) ** 2
    return math.sqrt(numerator)


if __name__ == '__main__':
    print(euclidean_distance((0, 0, 3), (4, 0, 0)))
