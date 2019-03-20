#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 17:16
# @Author: Jtyoui@qq.com
import os

"""
闵可夫斯基距离
闵氏空间指狭义相对论中由一个时间维和三个空间维组成的时空，
为俄裔德国数学家闵可夫斯基(1864-1909)最先表述。
他的平坦空间的概念以及表示为特殊距离量的几何学是与狭义相对论的要求相一致的。
闵可夫斯基空间不同于牛顿力学的平坦空间
当p=1时，得到绝对值距离，也叫曼哈顿距离
当p=2时，得到欧几里德距离
令p无穷大，得到切比雪夫距离
"""


def minkowski_distance(coordinate_p, coordinate_q, dimension):
    """
    闵可夫斯基距离
    :param coordinate_p: p坐标
    :param coordinate_q: q坐标
    :param dimension:闵可夫斯基维度
    :return: 闵可夫斯基距离
    """
