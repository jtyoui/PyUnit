#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/9/10 13:47
# @Author: Jtyoui@qq.com
from jtyoui.error import MathValueWarning
import math
import warnings


def theorem_Zero(function, x1: float, x2: float) -> float:
    """零点定理

    定义一个函数：x^3-2x-5=0,求x等于多少。x的值域：[1,1000]
    原理利用二分法不断的逼近，求出答案

    :param function: 定一个函数
    :param x1: 开始值
    :param x2: 结束值
    :return: 返回零点的值
    """
    if function(x1) == 0:
        return x1
    elif function(x2) == 0:
        return x2
    elif function(x1) * function(x2) > 0:
        warnings.warn('[a,b]区间的值应该满足:f(a)*f(b)<0', category=MathValueWarning)
        return math.inf
    else:
        mid = x1 + (x2 - x1) / 2.0
        while abs(x1 - mid) > math.pow(10, -9):  # x值小于10亿分之一
            if function(mid) == 0:
                return mid
            elif function(mid) * function(x1) < 0:
                x2 = mid
            else:
                x1 = mid
            mid = x1 + (x2 - x1) / 2.0
        return mid


if __name__ == '__main__':
    # 定义一个函数：x^3-2x-5=0,求x等于多少。x的值域：[1,1000]
    print(theorem_Zero(lambda x: x ** 2 - 1, 0, 1000))
