#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/1/10 14:19
# @Author: Jtyoui@qq.com
from random import randint

"""
米勒-拉宾素性检验是一种素数判定法则，利用随机化算法判断一个数是合数还是可能是素数。
卡内基梅隆大学的计算机系教授Gary Lee Miller首先提出了基于广义黎曼猜想的确定性算法，
由于广义黎曼猜想并没有被证明，其后由以色列耶路撒冷希伯来大学的Michael O. Rabin教授作出修改，
提出了不依赖于该假设的随机化算法。
"""


def miller_rabin_prime(n, k=50):
    """米勒-拉宾素性检验是一种素数判定法则

    米勒-拉宾素性检验是一种素数判定法则，利用随机化算法判断一个数是合数还是可能是素数。
    卡内基梅隆大学的计算机系教授Gary Lee Miller首先提出了基于广义黎曼猜想的确定性算法，
    由于广义黎曼猜想并没有被证明，其后由以色列耶路撒冷希伯来大学的Michael O. Rabin教授作出修改，
    提出了不依赖于该假设的随机化算法。

    :param n: 质数
    :param k: 检验的次数
    :return: 是质数返回True，不是返回False
    """
    if n < 6:
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:
        return False
    else:
        s, d = 0, n - 1
        while d % 2 == 0:
            s += 1
            d >>= 1
        for _ in range(k):
            a = randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                elif x == n - 1:
                    a = 0
                    break
            if a:
                return False
    return True


def random_big_prime(n=15):
    """随机生成一个大位质数

    >>> print(random_big_prime(128))

    这种算法具有不确定，错误概率在亿分之一以下。犹如买彩票一样

    :param n: 质数的位数
    :return: 大质数
    """
    while True:
        s = randint(10 ** (n - 1), 10 ** n)
        if miller_rabin_prime(s):
            return s


if __name__ == '__main__':
    m = miller_rabin_prime(1202665577221067947046558160900252532924577373213201474275893551111)
    print(m)
    print(random_big_prime(128))
