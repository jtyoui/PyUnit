#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 17:16
# @Author: Jtyoui@qq.com

"""
闵可夫斯基距离
闵氏空间指狭义相对论中由一个时间维和三个空间维组成的时空，
为俄裔德国数学家闵可夫斯基(1864-1909)最先表述。
他的平坦空间的概念以及表示为特殊距离量的几何学是与狭义相对论的要求相一致的。
闵可夫斯基空间不同于牛顿力学的平坦空间
当dimension=1时，得到绝对值距离，也叫曼哈顿距离
当dimension=2时，得到欧几里德距离
令dimension=无穷大(math.inf)，得到切比雪夫距离
"""


def minkowski_distance(coordinate_p, coordinate_q, dimension):
    """闵可夫斯基距离

    :param coordinate_p: p坐标
    :param coordinate_q: q坐标
    :param dimension: 闵可夫斯基维度
    :return: 闵可夫斯基距离
    """
    all_ = []
    for x, y in zip(coordinate_p, coordinate_q):
        p = abs(x - y) ** dimension
        all_.append(p)
    return pow(sum(all_), 1 / dimension)


if __name__ == '__main__':
    print(minkowski_distance([3, 0], [0, 4], 3))
