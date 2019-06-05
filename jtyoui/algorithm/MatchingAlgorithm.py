#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/5 9:57
# @Author: Jtyoui@qq.com
from jtyoui.algorithm.SearchAlgorithm import binary_search


class FMMA:
    """FMMA(Forward Maximum Matching Algorithms)正向最大匹配算法"""

    def __init__(self, ls, sort=False):
        """匹配的词典
        :param ls: 词典
        :param sort: 是否要排序
        """
        if sort:
            self.ls = sorted(ls)
        else:
            self.ls = ls

    def cut(self, line, max_length):
        """输入一行字符串，最大按照max_length拆分"""
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
    """RMMA(Reverse Maximum Matching Algorithms)逆向最大匹配算法"""

    def __init__(self, ls, sort=False):
        """匹配的词典
        :param ls: 词典
        :param sort: 是否要排序
        """
        if sort:
            self.ls = sorted(ls)
        else:
            self.ls = ls

    def cut(self, line, max_length):
        """输入一行字符串，最大按照max_length拆分"""
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


if __name__ == '__main__':
    r = RMMA(ls=['我们', '野生', '动物园'], sort=True)
    print(r.cut('我们在野生动物园玩', 3))
    print('-----------------------------------------')
    r = FMMA(ls=['我们', '野生', '动物园'], sort=True)
    print(r.cut('我们在野生动物园玩', 3))
