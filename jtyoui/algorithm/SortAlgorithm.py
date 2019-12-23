#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/26 17:20
# @Author: Jtyoui@qq.com
"""排序算法"""


def bubbled_sort(ls):
    """冒泡算法

    >>> import random
    >>> import time
    >>> s = []
    >>> for _ in range(100):
            jr = random.randint(0, 1000)
            s.append(jr)
    >>> start = time.time()
    >>> bs = bubbled_sort(s)
    >>> print(bs)
    >>> print(time.time() - start)
    """
    length = len(ls)
    flag = True  # 判断是否要进行数据交换，True表示要进行
    k = length - 1  # 表示已经排序好的上界值,默认是列表的长度
    last = 0  # 记住上一次循环交换的位置。默认是开头
    for i in range(length):
        if not flag:
            break
        flag = False  # 每次循环都默认为不进行数据交换
        for j in range(k):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                flag = True  # 要交换数据
                last = j  # 交换数据的位置
        k = last
    return ls


if __name__ == '__main__':
    import random
    import time

    s = []
    for _ in range(1_00):
        jr = random.randint(0, 1000)
        s.append(jr)
    start = time.time()
    bs = bubbled_sort(s)
    print(bs)
    print(time.time() - start)
