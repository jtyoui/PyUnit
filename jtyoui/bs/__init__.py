#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/1/31 0031
# @Email : jtyoui@qq.com
# @Software : PyCharm

"""任意进制相互转化"""


def __successive_division(n, x):  # 辗转相除法
    while n:
        yield n % x  # 将余数返回
        n //= x  # 剩下余数


def binary_system(x, base_x, base_y):
    """转化进制

    >>> print(binary_system(2542, 7, 12))

    :param x: 字符串非负整数
    :param base_x: 字符串的进制
    :param base_y: 转化的进制
    :return: 被转化的进制
    """
    if base_y <= 1 or base_x <= 1:  # 进制不可能小于1
        raise ValueError('进制不可能小于1')
    if not isinstance(x, (int, str)):
        raise ValueError('x值应该是int类型或者字符串类型')
    if isinstance(x, int):
        if x < 1:
            raise ValueError('x的值不可能小于1')
        x = str(x)
    y = int(x, base_x)  # 将其他进制先转为十进制
    # 在将十进制转为其他进制,并且将大于10的数字用ASCII值来表示,第一个ASCII是97小写的a
    m = map(lambda b: chr(b + 87) if b >= 10 else str(b), __successive_division(y, base_y))
    bs = ''.join(m)[::-1]  # 返回字符串并且反转
    if int(bs, base_y) == y:  # 检验进制是否正确
        return bs
    raise ValueError('验证进制错误!')  # 如果检验失败,返回错误


def gcd(m, n):
    """最大公约数

    >>> print(gcd(97 * 2, 97 * 3))

    :param m: 大于零的整数
    :param n: 大于零的整数
    :return:  返回最大公约数
    """
    if n == 0:
        m, n = m, n
    while m != 0:
        m, n = n % m, m
    return n


if __name__ == '__main__':
    print(binary_system(2542, 7, 12))
    print(gcd(97 * 2, 97 * 3))
