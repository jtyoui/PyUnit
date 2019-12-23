#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/20 18:12
# @Author: Jtyoui@qq.com
from jtyoui import parameter_set_length

"""
杰卡德距离
杰卡德距离是用来衡量两个集合差异性的一种指标，它是杰卡德相似系数的补集，
被定义为1减去杰卡德相似系数。而杰卡德相似系数，
也称杰卡德指数,是用来衡量两个集合相似度的一种指标
"""


@parameter_set_length
def jaccard_distance(set_, other_set):
    """杰卡德距离

    1）  m00:代表向量A与向量B都是0的维度个数；
    2）  m01:代表向量A是0而向量B是1的维度个数；
    3）  m10:代表向量A是1而向量B是0的维度个数；
    4)   m11:代表向量A和向量B都是1的维度个数。
    n维向量的每一维都会落入这4类中的某一类，因此：
    Jaccard距离为:m01+m10/m01+m10+m11+m00

    :param set_: 以1和0组合的集合
    :param other_set: 以1和0组合的集合
    :return: 两个不一样的频率
    """
    m00, m01, m10, m11 = 0, 0, 0, 0
    for x, y in zip(set_, other_set):
        if x == y == 0:
            m00 += 1
        elif x == 1 and y == 0:
            m10 += 1
        elif x == 0 and y == 1:
            m01 += 1
        else:
            m11 += 1
    return (m01 + m10) / (m01 + m10 + m11 + m00)


def jaccard_set_distance(set_, other_set):
    """杰卡德距离

    两个集合A和B的交集元素在A，B的并集中所占的比例，
    称为两个集合的杰卡德相似系数
    与杰卡德相似系数相反的概念是杰卡德距离
    杰卡德距离用两个集合中不同元素占所有元素的比例来衡量两个集合的区分度

    :param set_: 一个set类型
    :param other_set: 另一个set类型
    :return: 集合之间的值
    """
    if not (isinstance(set_, set) and isinstance(other_set, set)):
        raise TypeError("参数必须是set类型")
    intersection = len(set_.intersection(other_set))
    union = len(set_.union(other_set))
    return (union - intersection) / union


if __name__ == '__main__':
    print(jaccard_distance([0, 1, 1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1, 1, 0, 0]))
    print(jaccard_set_distance({1, 10, 31, 2, 13, 26, 43}, {21, 52, 31, 43, 6, 12, 31}))
