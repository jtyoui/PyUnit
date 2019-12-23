#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:34
# @Author: Jtyoui@qq.com
from jtyoui import parameter_set_length

"""
切比雪夫距离(棋盘距离)
在数学中，切比雪夫距离或是L∞度量，是向量空间中的一种度量，
二个点之间的距离定义是其各坐标数值差绝对值的最大值。以数学的观点来看，切比雪夫距离是由一致范数（uniform norm）
所衍生的度量，也是超凸度量的一种。
国际象棋中，国王可以直行、横行、斜行，所以国王走一步可以移动到相邻8个方格中的任意一个。
国王从格子(x1,y1)走到格子(x2,y2)最少需要多少步？这个距离就叫切比雪夫距离。
"""


@parameter_set_length
def chebyshev_distance(coordinate_p, coordinate_q):
    """传入的是两个可迭代对象,每一个是一个n位坐标,比如:p=(x1,x2,x3....xn),q=(y1,y2,y3....yn)

    :param coordinate_p: p坐标
    :param coordinate_q: q坐标
    :return: 切比雪夫距离(棋盘距离)
    """
    coordinate = []
    for x, y in zip(coordinate_p, coordinate_q):
        coordinate.append(abs(x - y))
    return max(coordinate)


if __name__ == '__main__':
    c_d = chebyshev_distance((11, 2, 2, 3, 23, 2), (3, 3, 2, 3, 2, 3))
    print(c_d)
