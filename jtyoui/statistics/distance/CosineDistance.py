#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:36
# @Author: Jtyoui@qq.com
from jtyoui import parameter_set_length

"""
余弦距离
几何中，夹角余弦可用来衡量两个向量方向的差异；
机器学习中，借用这一概念来衡量样本向量之间的差异。
余弦相似度用向量空间中两个向量夹角的余弦值作为衡量两个个体间差异的大小。
相比距离度量，余弦相似度更加注重两个向量在方向上的差异，而非距离或长度上
"""


@parameter_set_length
def cosine(coordinate_p, coordinate_q):
    """余弦距离又叫余弦角度

    :param coordinate_p: p坐标
    :param coordinate_q: q坐标
    :return: 余弦距离
    """
    numerator, denominator = 0, 1  # 分子和父母
    for x, y in zip(coordinate_p, coordinate_q):
        numerator += x * y
    q = [x ** 2 for x in coordinate_q]
    p = [y ** 2 for y in coordinate_p]
    return numerator / pow(sum(q) * sum(p), 0.5)


def cosine_distance(sentence, data):
    """余弦距离"""
    import jieba  # 安装 pip install jieba
    ls, ds = [], []
    s = jieba.cut(sentence)
    d = jieba.cut(data)
    for c in set(list(s) + list(d)):
        if len(c) > 0:
            ls.append(sentence.count(c))
            ds.append(data.count(c))
    return cosine(ls, ds)


if __name__ == '__main__':
    print(cosine_distance('我吃饭了', '我正在吃饭'))
