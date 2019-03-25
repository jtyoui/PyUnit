#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/3/23 0023
# @Email : jtyoui@qq.com

"""处理二维矩阵"""
from copy import deepcopy
from jtyoui.error import MatrixNotDottedError


class Matrix:

    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("传入list类型")
        self.__data = data
        self.__length = len(data)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            other = other.__data
        elif not isinstance(other, list):
            raise TypeError("传入list类型")
        other_w, other_h = len(other[0]), len(other)
        data_w, data_h = len(self.__data[0]), self.__length
        dot = []
        if data_w != other_h:
            raise MatrixNotDottedError("矩阵不能点乘")

        for data_j in range(data_h):
            dot.append([])
            for i in range(other_w):
                all_ = [self.__data[data_j][j] * other[j][i] for j in range(other_h)]
                dot[data_j].append(sum(all_))
        return dot

    @property
    def i(self):
        """逆矩阵"""
        n = self.__length
        original = deepcopy(self.__data)
        i_ = self.unitized(n)  # 获得单位矩阵
        swap, triangle = self.elimination(original)  # 消元
        diagonal = self.diagonal_unitized(original)  # 对角单位化
        trace = self.trace_vector(original)

        for i in range(n):
            if swap[i] != i:
                i_[i], i_[swap[i]] = i_[swap[i]], i_[i]
            for j in range(i + 1, n):
                for k in range(n):
                    if triangle[j][i]:
                        i_[j][k] = i_[j][k] - triangle[j][i] * i_[i][k]
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if diagonal[n - 1 - i - j - 1][n - 1 - i]:
                    for k in range(n):
                        i_[n - 1 - i - j - 1][k] -= diagonal[n - 1 - i - j - 1][n - 1 - i] * i_[n - 1 - i][k]
        for i in range(n):
            for j in range(n):
                i_[i][j] = i_[i][j] / trace[i]
        return i_

    @property
    def t(self):
        """转置矩阵"""
        transposition = []
        for i in range(len(self.__data[0])):
            transposition.append([self.__data[j][i] for j in range(self.__length)])
        return transposition

    @property
    def det(self):
        """秩"""
        return 1

    def unitized(self, length):
        """单位E矩阵"""
        eye = self.zero_matrix(length)
        for i in range(length):
            eye[i][i] = 1
        return eye

    def elimination(self, data):
        """消元矩阵"""
        """交换操作记录数组"""
        swap, triangle = list(range(self.__length)), self.zero_matrix(self.__length)  # 交换矩阵 三角矩阵

        """对每一列进行操作"""
        for i in range(self.__length):
            max_row, row = data[i][i], i
            for j in range(i, self.__length):
                if data[j][i] >= max_row:
                    max_row, row = data[j][i], j
            swap[i] = row

            """交换"""
            if row != i:
                for j in range(self.__length):
                    data[i][j], data[row][j] = data[row][j], data[i][j]

            """消元"""
            for j in range(i + 1, self.__length):
                if data[j][i]:
                    triangle[j][i] = data[j][i] / data[i][i]
                    for k in range(self.__length):
                        data[j][k] = data[j][k] - triangle[j][i] * data[i][k]

        return swap, triangle

    def diagonal_unitized(self, data):
        """对角单位化"""
        diagonal, position = self.zero_matrix(self.__length), self.__length - 1  # 对角矩阵

        for i in range(position):
            for j in range(position - i):
                if data[position - i - j - 1][position - i] and data[position - i][position - i]:
                    diagonal[position - i - j - 1][position - i] = (
                            data[position - i - j - 1][position - i] / data[position - i][position - i])
                    for k in range(self.__length):
                        data[position - i - j - 1][k] = data[position - i - j - 1][k] - (
                                diagonal[position - i - j - 1][position - i] * data[position - i][k])

        return diagonal

    def trace_vector(self, data):
        """矩阵迹向量"""
        return [data[i][i] for i in range(self.__length)]

    @staticmethod
    def zero_matrix(length):
        """单位零矩阵"""
        eye = []
        for i in range(length):
            eye.append([0 for _ in range(length)])
        return eye


if __name__ == '__main__':
    d = [
        [1, 2, 3],
        [1, 0, -1],
        [0, 1, 1]
    ]
    mat = Matrix(d)
    print(mat * d)
