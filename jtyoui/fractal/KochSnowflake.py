#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/11
"""
科赫雪花
在一单位长度的线段上对其三等分，将中间段直线换成一个去掉底边的等边三角形，
再在每条直线上重复以上操作，如此进行下去直到无穷，就得到分形Koch曲线。
"""

import turtle


def koch(p, order, size):
    if order == 0:
        p.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(p, order - 1, size / 3)
            p.left(angle)


def draw_koch(n=3, polygon=6):
    """绘画科赫雪花

    :param n: 迭代次数
    :param polygon: 多边形雪花
    """
    pen = turtle.Pen()
    turtle.title('科赫雪花')
    pen.speed(0)
    r = pen.screen.canvwidth / 2
    pen.penup()
    pen.goto(-r, 0)
    pen.pendown()
    a = 180 - (polygon - 2) * 180 / polygon  # 计算多边形旋转的角度,计算公式
    # 多边形的内角和公式（n-2）*180/n
    for i in range(polygon):
        angle = a * (1 - i)
        pen.setheading(angle)
        koch(pen, n, r)
    turtle.done()


if __name__ == '__main__':
    draw_koch(3, 7)
