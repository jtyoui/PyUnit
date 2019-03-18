#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:37
# @Author: Jtyoui
from array import array

"""
编辑距离
编辑距离又称Levenshtein距离，是指两个字串之间，由一个转成另一个所需的最少编辑操作次数。
许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。一般来说，
编辑距离越小，两个串的相似度越大。
"""


def edit_distance(chars, other_chars):
    w, h = len(chars), len(other_chars)
