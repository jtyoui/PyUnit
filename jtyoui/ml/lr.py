#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/7 10:14
# @Author: Jtyoui@qq.com
from jtyoui.ml import sigmoid, error_rate, TEST_LABEL, TRAIN_DATA
import numpy as np

__description__ = """
LR(逻辑回归)算法
"""


def lr_train_bgd(feature: np.array, label: np.array, max_cycle: int, alpha: float) -> np.mat:
    """利用梯度下降法训练逻辑回归模型（LR）

    :param feature: 特征
    :param label: 标签
    :param max_cycle: 最大迭代次数
    :param alpha: 学习率
    :return: w的权重
    """
    n = np.shape(feature)[1]  # 特征个数
    w = np.random.rand(n).reshape((n, 1))  # 随机初始化权重
    i = 0
    while i <= max_cycle:
        i += 1
        h = sigmoid(np.dot(feature, w))  # 做点乘，计算sigmoid值
        err = label - h  # 误差
        if i % 100 == 0:
            print(f'error rate: {error_rate(h, label)}')
        w += alpha * np.dot(feature.T, err)  # wi+ 1= wi+ α·d 梯度下降进行权重修正

    return w


if __name__ == '__main__':
    weight = lr_train_bgd(TRAIN_DATA, TEST_LABEL, 2000, 0.01)
    print(sigmoid(np.dot(np.array([[1, 1 / 24, 10 / 60, 32 / 60]], dtype=np.float), weight)))
