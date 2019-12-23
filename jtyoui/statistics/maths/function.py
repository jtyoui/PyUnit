#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/17 14:43
# @Author: Jtyoui@qq.com
from jtyoui.error import NotLegitimateNumberError
from jtyoui.file_zip import load_zip
from functools import reduce
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

    print(len(list(primes(1_0000_0000))))  # 时间5.5541136264801025秒
    10万内：9592
    100万内：78498
    1000万内：664579
    1亿内：5761455

    :param n: 表示[0,n]范围的质数
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


def collatz(n):
    """Collatz猜想:也叫3n+1猜想，给一个正整数，如果是偶数，则减半；如果是奇数，则变为它的三倍加一。直到变为一停止"""
    if n > 1 and isinstance(n, int):
        total = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            total += 1
    else:
        raise TypeError('类型错误。必须是大于1的整数')
    return total


def tetrahedron_volume(r1, r2, r3, r4, r5, r6):
    """知道四面体的边求体积，r1-r6都是边"""
    R1, R2, R3, R4, R5, R6 = r1 ** 2, r2 ** 2, r3 ** 2, r4 ** 2, r5 ** 2, r6 ** 2
    one = R1 * R2 * R4 + R1 * R3 * R6 + R2 * R3 * R5 + R4 * R5 * R6
    two = R1 * R2 * R5 + R1 * R2 * R6 + R1 * R3 * R4 + R1 * R3 * R5 + R1 * R4 * R5 + R1 * R5 * R6 + R2 * R3 * R4 + R2 * R3 * R6 + R2 * R4 * R6 + R2 * R5 * R6 + R3 * R4 * R5 + R3 * R4 * R6
    three = R1 * R1 * R5 + R1 * R5 * R5 + R2 * R2 * R6 + R2 * R6 * R6 + R3 * R3 * R4 + R3 * R4 * R4
    s = two - one - three
    v = math.sqrt(s / 144)
    return v


def tetrahedron_volume2(a, b, c, m, n, l):
    """知道四面体的边求体积，a, b, c, m, n, l都是边"""
    v = math.sqrt((4.0 * a * a * b * b * c * c - a * a * (b * b + c * c - m * m) * (b * b + c * c - m * m) - b * b * (
            c * c + a * a - n * n) * (c * c + a * a - n * n) - c * c * (a * a + b * b - l * l) * (
                           a * a + b * b - l * l) + (a * a + b * b - l * l) * (b * b + c * c - m * m) * (
                           c * c + a * a - n * n))) / 12.0
    return v


def helen_formula(a, b, c):
    """海伦公式，知道三边求面积

    a、b、c是三角形的三条边
    """
    if a > 0 and b > 0 and c > 0:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s
    else:
        raise TypeError('类型错误,三角形三边必须是大于0的数字类型')


def factorial(n, number=1):
    """求n的阶乘

    当number==1时，表示n!
    当number==2时，表示n!!
    当number==3时，表示n!!!
    ...................

    :param n: 输入大于1的整数
    :param number: 阶乘数
    :return: n的number阶乘
    """
    return reduce(lambda x, y: x * y, range(1, n + 1, number))


def pi(n=7):
    """计算PI,能精确到小数点：15万5千6百42位

    :param n: 表示精确的小数，n的范围是：0-155640
    :return: 返回的是字符串，默认是返回小数点7位
    """
    line = load_zip('pi.zip', 'pi.txt')
    return line[0][:n + 2]


if __name__ == '__main__':
    print(sign_function(123.22))
    print(integral_function(25.2))
    print(integral_function('-3.1'))
    print(dirichlet_function(math.pi))
    print(is_prime(915452))
    # print(len(primes(1_0000_0000)))  # 时间5.5541136264801025秒
    print(collatz(27))
    print(helen_formula(3, 3, 3))
    print(tetrahedron_volume(3, 3, 3, 3, 3, 3))
    print(tetrahedron_volume2(3, 3, 3, 3, 3 * math.sqrt(3), 3 * math.sqrt(3)))
    print(factorial(5, 2))
    print(pi())
