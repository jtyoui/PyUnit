#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/8 13:31
# @Author: Jtyoui@qq.com
from jtyoui.ml import sigmoid, get_cost, TRAIN_DATA, TEST_LABEL
from random import normalvariate
import numpy as np

__description__ = """
FM(因子分解机)算法
"""


def initialize_v(n: int, k: int):
    """初始化交叉项

    :param n: 特征个数
    :param k: FM模型的度
    :return: 交叉项的系数权重
    """
    v = np.mat(np.zeros(shape=(n, k)))
    for i in range(n):
        for j in range(k):
            v[i, j] = normalvariate(0, 0.2)
    return v


def get_prediction(data, w0, w, v):
    """预测值

    :param data: 特征
    :param w0: 一次项权重
    :param w: 常数项权重
    :param v: 交叉项权重
    :return: 预测结果
    """
    m = np.shape(data)[0]
    result = []
    for x in range(m):
        inter_1 = data[x] * v
        inter_2 = np.multiply(data[x], data[x]) * np.multiply(v, v)
        inter = np.sum(np.multiply(inter_1, inter_1) - inter_2) / 2.
        p = w0 + data[x] * w + inter
        pre = sigmoid(p[0, 0])
        result.append(pre)
    return result


def stop_grad_ascent(data: np.mat, label: np.mat, k: int, max_iter: int, alpha: float) -> (float, np.mat, np.mat):
    """利用随机梯度下降法训练FM模型

    :param data: 数据特征
    :param label: 标签
    :param k: v的维度
    :param max_iter: 最大迭代次数
    :param alpha: 学习率
    :return: w0,w,v权重
    """
    m, n = np.shape(data)
    w = np.random.randn(n).reshape((n, 1))
    w0 = 0
    v = initialize_v(n, k)
    for it in range(max_iter):
        for x in range(m):
            inter_1 = data[x] * v
            inter_2 = np.multiply(data[x], data[x]) * np.multiply(v, v)
            inter = np.sum(np.multiply(inter_1, inter_1) - inter_2) / 2.
            p = w0 + data[x] * w + inter
            loss = sigmoid(label[x] * p[0, 0]) - 1
            w0 -= alpha * loss * label[x]
            for i in range(n):
                if data[x, i] != 0:
                    w[i, 0] -= alpha * loss * label[x] * data[x, i]
                for j in range(k):
                    v[i, j] -= alpha * loss * label[x] * (
                            data[x, i] * inter_1[0, j] - v[i, j] * data[x, i] * data[x, i])
        if it % 100 == 0:
            pre = get_prediction(np.mat(data), w0, w, v)
            print(get_cost(np.mat(pre), label))
    return w0, w, v


if __name__ == '__main__':
    weight = stop_grad_ascent(TRAIN_DATA, TEST_LABEL, 3, 1000, 0.1)
    print(get_prediction(np.mat([[1, 1 / 24, 10 / 60, 32 / 60]]), *weight))
