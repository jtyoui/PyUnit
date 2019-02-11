#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/11
# @Email : jtyoui@qq.com
# @Software : PyCharm
import turtle

"""
康托三分集
选取一个欧氏长度的直线段，将该线段三等分，去掉中间一段，剩下两段。
将剩下的两段分别再三等分，各去掉中间一段，剩下四段。
将这样的操作继续下去，直到无穷，则可得到一个离散的点集。
点数趋于无穷多，而欧氏长度趋于零。经无限操作，达到极限时所得到的离散点集称之为Cantor集。
"""


class CantorTernarySet:

    def __init__(self, start=-300, end=300, n=6):
        self.start = start  # 初始的起始点
        self.end = end  # 初始的终结点
        self.dot = [[(start, end)]]  # 离散的点集
        self.row(n)

    def row(self, n):
        every_time = algorithm(self.start, self.end)  # 保存每一次分割的点集
        for _ in range(1, n):  # 一共分割多少次
            self.dot.append(every_time)  # 保存每一次分割的点集的集合
            ls = []  # 临时保存每一次点集
            for dot in every_time:  # 遍历每一个点
                s = algorithm(*dot)
                ls.extend(s)
                every_time = ls  # 复制再遍历

    def draw(self):  # 绘画
        pen = turtle.Pen()
        turtle.title('康托三分集')
        pen.width(2)
        for index, dot in enumerate(self.dot):
            for x, y in dot:
                pen.penup()
                pen.goto(x=x, y=100 - index * 10)
                pen.pendown()
                pen.forward(y - x)
        turtle.done()


def algorithm(start, end):
    length = end - start  # 线段的长度
    equal = length / 3
    one_dot = start + equal  # 第一个点的位置
    two_dot = end - equal  # 第二个点的位置
    return [(start, one_dot), (two_dot, end)]


if __name__ == '__main__':
    ct = CantorTernarySet()
    ct.draw()
