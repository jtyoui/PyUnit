#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:37
# @Author: Jtyoui@qq.com

"""
编辑距离
编辑距离又称Levenshtein距离，是指两个字串之间，由一个转成另一个所需的最少编辑操作次数。
许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。一般来说，
编辑距离越小，两个串的相似度越大。
"""


def edit_distance(chars, other_chars):
    """编辑距离

    :param chars: 字符串
    :param other_chars: 另一个字符串
    :return: 编辑距离值
    """
    w, h = len(chars), len(other_chars)  # 计算出长和宽
    array = [[0 for _ in range(h + 1)] for _ in range(w + 1)]  # 初始化
    for i in range(w + 1):
        for j in range(h + 1):
            array[i][j] = i + j if i == 0 or j == 0 else min(array[i - 1][j - 1], array[i - 1][j], array[i][j - 1]) + 1
            array[i][j] = array[i - 1][j - 1] if chars[i - 1] == other_chars[j - 1] else array[i][j]
    return array[w][h]


if __name__ == '__main__':
    print(edit_distance('我吃饭了', '我正在吃饭'))
