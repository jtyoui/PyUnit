#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:34
# @Author: Jtyoui

"""
马氏距离
马氏距离(Mahalanobis distance)是由印度统计学家马哈拉诺比斯(P. C. Mahalanobis)提出的，
表示数据的协方差距离。它是一种有效的计算两个未知样本集的相似度的方法。与欧氏距离不同的是，
它考虑到各种特性之间的联系（例如：一条关于身高的信息会带来一条关于体重的信息，因为两者是有关联的），
并且是尺度无关的(scale-invariant)，即独立于测量尺度。对于一个均值为μ，协方差矩阵为Σ的多变量向量，
其马氏距离为sqrt( (x-μ)'Σ^(-1)(x-μ) )。
"""


def mahalanobis_distance():
    pass


if __name__ == '__main__':
    print(mahalanobis_distance())
