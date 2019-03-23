#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/3/23 0023
# @Email : jtyoui@qq.com

"""矩阵"""


class Matrix:

    def __init__(self, data):
        self.__data = data

    @property
    def i(self):
        """逆矩阵"""
        return 1

    @property
    def t(self):
        """转置矩阵"""
        return 1

    @property
    def det(self):
        """秩"""
        return 1


if __name__ == '__main__':
    d = [
        [2, 1, 1],
        [1, 2, -1],
        [1, -1, 3]
    ]
    m = Matrix(d)
    print(m.i)
