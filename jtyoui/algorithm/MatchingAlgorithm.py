#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/5 9:57
# @Author: Jtyoui@qq.com
"""匹配算法"""
from jtyoui.algorithm.SearchAlgorithm import binary_search
from jtyoui.error import NumberValueError


def _verification(number):
    if not isinstance(number, int) or number < 2:
        raise NumberValueError(f'输入的值必须大于1，你输入的值是：{number}')


class FMMA:
    """FMMA(Forward Maximum Matching Algorithms)正向最大匹配算法

    >>> r = FMMA(ls=['我们', '野生', '动物园', '在野'], sort=True)
    >>> print(r.cut('我们在野生动物园玩', 3))
    >>> # ['我们', '在野', '生', '动物园', '玩']
    """

    def __init__(self, ls, sort=False):
        """正向最大匹配算法、匹配的词典

        :param ls: 词典
        :param sort: 是否要排序
        """
        if sort:
            self.ls = sorted(ls)
        else:
            self.ls = ls

    def cut(self, line, max_length):
        """输入一行字符串，最大按照max_length拆分"""
        _verification(max_length)
        total = []
        while len(line) > 0:
            word = line[:max_length]
            while not binary_search(self.ls, word):
                if len(word) == 1:
                    break
                else:
                    word = word[:-1]
            total.append(word)
            line = line[len(word):]
        return total


class RMMA:
    """RMMA(Reverse Maximum Matching Algorithms)逆向最大匹配算法

    >>> r = RMMA(ls=['我们', '野生', '动物园', '在野'], sort=True)
    >>> print(r.cut('我们在野生动物园玩', 3))
    >>> # ['我们', '在', '野生', '动物园', '玩']
    """

    def __init__(self, ls, sort=False):
        """逆向最大匹配算法、匹配的词典

        :param ls: 词典
        :param sort: 是否要排序
        """
        if sort:
            self.ls = sorted(ls)
        else:
            self.ls = ls

    def cut(self, line, max_length):
        """输入一行字符串，最大按照max_length拆分"""
        _verification(max_length)
        total = []
        while len(line) > 0:
            word = line[-max_length:]
            while not binary_search(self.ls, word):
                if len(word) == 1:
                    break
                else:
                    word = word[1:]
            total.append(word)
            line = line[:len(line) - len(word)]
        return list(reversed(total))


def _kmp(p):
    i, k, m = 0, -1, len(p)
    p_next = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                p_next[i] = p_next[k]
            else:
                p_next[i] = k
        else:
            k = p_next[k]
    return p_next


def kmp(string, str_):
    """KMP(The Knuth-Morris-Pratt Algorithm)无回溯串匹配算法

    >>> print(kmp('我们在野生动物园玩', '动物园'))
    """
    j, i = 0, 0
    p_next = _kmp(string)
    n, m = len(string), len(str_)
    while j < n and i < m:
        if i == -1 or string[j] == str_[i]:
            j, i = j + 1, i + 1
        else:
            i = p_next[i]
    if i == m:
        return j - i
    return -1


def max_sub_array(ls: list) -> tuple:
    """求解最大子数组

    >>> print(max_sub_array([5, 4, -12, 1, 3, -1, 4, 1, -6]))

    :param ls: 数字类列表
    :return: （起始位置，结束位置，最大值）
    """
    min_, max_, sum_ = 0, 0, 0
    return_max = 0, 0, 0
    for index, value in enumerate(ls):
        sum_ += value
        rm = max(sum_, sum_ - ls[index])
        if sum_ < 0:
            sub_max = min_, index - 1, sum_ - ls[index]
            min_, sum_ = index + 1, 0
        elif rm != sum_ and index > 0:
            sub_max = min_, index - 1, rm
        else:
            continue
        return_max = sub_max if return_max[2] < sub_max[2] else return_max
    else:
        return_max = (min_, len(ls) - 1, sum_) if return_max[2] < sum_ else return_max
    return return_max


if __name__ == '__main__':
    r = RMMA(ls=['我们', '野生', '动物园', '在野'], sort=True)
    print(r.cut('我们在野生动物园玩', 3))
    # ['我们', '在', '野生', '动物园', '玩']
    print('-----------------------------------------')
    r = FMMA(ls=['我们', '野生', '动物园', '在野'], sort=True)
    print(r.cut('我们在野生动物园玩', 3))
    # ['我们', '在野', '生', '动物园', '玩']
    print('-----------------------------------------')
    print(kmp('我们在野生动物园玩', '动物园'))
    print('-----------------------------------------')
    print(max_sub_array([5, 4, -12, 1, 3, -1, 4, 1, -6]))
