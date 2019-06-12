#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/17 14:43
# @Author: Jtyoui@qq.com
from jtyoui.error import NotLegitimateNumberError
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


def is_prime(n):
    """判断一个数是否为质数"""
    if (not isinstance(n, int)) or (n <= 1):
        raise NotLegitimateNumberError('不是一个合法的数字')
    if n % 2 == 0:  # 判断偶数
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):  # 判断奇数
            if n % i == 0:
                return False
        return True


def primes(n):
    """埃拉托斯特尼质数筛法
    >>> print(len(list(primes(1_0000_0000))))  # 时间5.5541136264801025秒
     10万内：9592
     100万内：78498
     1000万内：664579
     1亿内：5761455
    """
    n += 1
    ps = [True] * n
    total = [2]
    half = int(math.sqrt(n))
    for index in range(3, half + 1, 2):
        if is_prime(index):  # 取开平方的质数
            ps[index * index: n: index] = [False] * math.ceil((n - index * index) / index)
    for y in range(3, n, 2):
        if ps[y]:
            total.append(y)
    return total


if __name__ == '__main__':
    print(sign_function(123.22))
    print(integral_function(25.2))
    print(integral_function('-3.1'))
    print(dirichlet_function(math.pi))
    print(is_prime(915452))
    print(len(primes(1_0000_0000)))  # 时间5.5541136264801025秒
