#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:34
# @Author: Jtyoui@qq.com
from jtyoui.statistics.analysis import Matrix, cov, AnalysisMath

"""
马氏距离
马氏距离是由印度统计学家马哈拉诺比斯提出的，
表示数据的协方差距离。它是一种有效的计算两个未知样本集的相似度的方法。与欧氏距离不同的是，
它考虑到各种特性之间的联系（例如：一条关于身高的信息会带来一条关于体重的信息，因为两者是有关联的），
并且是尺度无关的(scale-invariant)，即独立于测量尺度。对于一个均值为μ，协方差矩阵为Σ的多变量向量，
其马氏距离为sqrt( (x-μ)'Σ^(-1)(x-μ) )。
"""


def mahalanobis_distance(matrix, coordinate):
    """求解马氏距离

    马氏距离要求样本数要大于维数，否则无法求协方差矩阵
    此处进行转置，表示10个样本，每个样本2维

    :param matrix: 矩阵列表
    :param coordinate: 坐标
    :return result: 两个点的马氏距离
    """
    s = Matrix(matrix).t
    ana = AnalysisMath()
    mean, c, distance = [], [], []
    for index, i in enumerate(s):
        c.append([cov(i, j) for j in s])
    s_i = Matrix(c).i  # 协方差矩阵的逆矩阵
    for data in s:
        mean.append(ana.expect(data))
    distance.append([i - j for i, j in zip(coordinate, mean)])
    ma = Matrix(Matrix(distance) * s_i) * Matrix(distance).t
    return pow(ma[0][0], 0.5)


if __name__ == '__main__':
    mat = [
        [3, 4],
        [5, 6],
        [2, 8],
        [8, 4]
    ]
    print(mahalanobis_distance(mat, [3, 4]))
