#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/7 16:01
# @Author: Jtyoui@qq.com
import numpy as np


def sigmoid(x):
    """Sigmoid函数"""
    return 1.0 / (1 + np.exp(-x))


def error_rate(h, label):
    """计算当前的错误率函数值

    :param h: 预测值
    :param label: 实际值
    :return: 错误率
    """
    m = np.shape(h)[0]
    sum_err = 0
    for i in range(m):
        if 0 < h[i, 0] < 1:
            sum_err -= label[i, 0] * np.log(h[i, 0]) + (1 - label[i, 0]) * np.log(1 - h[i, 0])
        else:
            sum_err -= 0
    return sum_err / m


def get_cost(predict: np.mat, label: np.mat) -> float:
    """计算损失函数的值

    :param predict: 预测值
    :param label: 标签
    :return: 损失函数的值
    """
    m = len(predict)
    error = 0.0
    for i in range(m):
        error -= np.log(sigmoid(predict[i, 0] * label[i, 0]))
    return error


def line_regression_a_b(x: np.array, y: np.array):
    """求解线性回归的a和β值。即y=b+a*x

    :param x: 数据特征值：应该是两维度。即：[[],[],[]]
    :param y: 数据预测值;一维度。即：[]
    :return: a值、和b值
    """
    var = np.var(x, ddof=1)  # 贝塞尔校正,方差
    cov = np.cov(x.transpose(), y)[0][1]  # 协方差
    x_ = np.mean(x)
    y_ = np.mean(y)
    a = cov / var
    b = y_ - a * x_
    return a, b


if __name__ == '__main__':
    a_, b_ = line_regression_a_b(np.array([[6], [8], [10], [14], [18]]), np.array([7, 9, 13, 17.5, 18]))
    print(np.array([[12]]) * a_ + b_)  # [[13.68103448]]
