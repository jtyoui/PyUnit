#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:33
# @Author: Jtyoui@qq.com
from jtyoui import parameter_set_length

"""
曼哈顿距离
顾名思义，在曼哈顿街区要从一个十字路口开车到另一个十字路口
，驾驶距离显然不是两点间的直线距离。这个实际驾驶距离就是“曼哈顿距离”。
曼哈顿距离也称为“城市街区距离”(City Block distance)。
"""


@parameter_set_length
def manhattan_distance(coordinate_p, coordinate_q):
    """曼哈顿距离

    :param coordinate_p: p坐标
    :param coordinate_q: q坐标
    :return: 曼哈顿距离值
    """
    point = (abs(x - y) for x, y in zip(coordinate_q, coordinate_p))
    return sum(point)


if __name__ == '__main__':
    print(manhattan_distance((1, 1), (7, 7)))
