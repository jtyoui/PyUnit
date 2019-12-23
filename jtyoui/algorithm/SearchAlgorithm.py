#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/5 9:37
# @Author: Jtyoui@qq.com
"""搜索算法"""
import bisect


def binary_search(ls, x, sort=False):
    """二分查找算法

    >>> s = [1, 2, 3, 4, 5, 6, 10, 7]
    >>> print(binary_search(s, 7, True))

    :param ls: 列表。
    :param x: 被查找的数。
    :param sort: 是否要启动排序，False表示不启动排序，默认是不启动。
    :return: 找到返回True，反之亦然
    """
    if sort:
        ls = sorted(ls)
    v = bisect.bisect_left(ls, x)
    if v != len(ls) and ls[v] == x:
        return True
    return False


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 10, 7]
    print(binary_search(s, 7, True))
