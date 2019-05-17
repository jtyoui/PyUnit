#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/17 14:43
# @Author: Jtyoui@qq.com
import math


def real_number(value):
    """判断是否是实数"""
    if isinstance(value, (int, float)):
        return value
    elif isinstance(value, str):
        return float(value)
    elif isinstance(value, complex):
        raise TypeError('不支持复数')
    else:
        raise ValueError('类型错误')


def sign_function(value):
    """符号函数"""
    value = real_number(value)
    if value < 0:
        return -1
    elif value > 0:
        return 1
    return 0


def abs_function(value):
    """绝对值函数"""
    value = real_number(value)
    return abs(value)


def integral_function(value):
    """取整函数"""
    value = real_number(value)
    return value // 1


def dirichlet_function(value):
    """狄利克雷函数：只是简单的判断"""
    value = real_number(value)
    a, b = value.as_integer_ratio()
    if len(str(a)) >= 15 and len(str(b)) >= 15:
        return 0
    return 1


if __name__ == '__main__':
    print(sign_function(123.22))
    print(integral_function(25.2))
    print(integral_function('-3.1'))
    print(dirichlet_function(math.pi))
