#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:34
# @Author: Jtyoui@qq.com
import numpy as np
from jtyoui import parameter_set_length

"""
马氏距离
马氏距离是由印度统计学家马哈拉诺比斯提出的，
表示数据的协方差距离。它是一种有效的计算两个未知样本集的相似度的方法。与欧氏距离不同的是，
它考虑到各种特性之间的联系（例如：一条关于身高的信息会带来一条关于体重的信息，因为两者是有关联的），
并且是尺度无关的(scale-invariant)，即独立于测量尺度。对于一个均值为μ，协方差矩阵为Σ的多变量向量，
其马氏距离为sqrt( (x-μ)'Σ^(-1)(x-μ) )。
"""


@parameter_set_length
def mahalanobis_distance(coordinate_x, coordinate_y):
    """
    求解马氏距离
    :param coordinate_x: x轴向量
    :param coordinate_y: y轴向量
    :return result: 两个点的马氏距离
    """
    # 马氏距离要求样本数要大于维数，否则无法求协方差矩阵
    # 此处进行转置，表示10个样本，每个样本2维
    x = np.vstack([coordinate_x, coordinate_y])
    x_t = x.T  # 转置
    s = np.cov(x)  # 两个维度之间协方差矩阵
    s_i = np.linalg.inv(s)  # 协方差矩阵的逆矩阵
    # 马氏距离计算两个样本之间的距离，此处共有4个样本，两两组合，共有6个距离。
    n = x_t.shape[0]
    result = []
    for i in range(0, n):
        for j in range(i + 1, n):
            delta = x_t[i] - x_t[j]
            point = x_t[i], x_t[j]
            distance = np.sqrt(np.dot(np.dot(delta, s_i), delta.T))
            result.append((point, distance))

    return result


if __name__ == '__main__':
    print(mahalanobis_distance((3, 5, 2, 8), (4, 6, 2, 4)))
