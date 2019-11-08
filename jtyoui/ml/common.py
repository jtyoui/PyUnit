#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/7 16:01
# @Author: Jtyoui@qq.com
import numpy as np


def sigmoid(x):
    """Sigmoid函数"""
    return 1.0 / (1 + np.exp(-x))


def error_rate(h, label):
    """计算当前的损失函数值
    :param h:预测值
    :param label:实际值
    :return:错误率
    """
    m = np.shape(h)[0]
    sum_err = 0
    for i in range(m):
        if 0 < h[i, 0] < 1:
            sum_err -= label[i, 0] * np.log(h[i, 0]) + (1 - label[i, 0]) * np.log(1 - h[i, 0])
        else:
            sum_err -= 0
    return sum_err / m
