#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:36
# @Author: Jtyoui

import hashlib
import jieba

"""
海明距离
"""


def handle(content, weight, f):
    """
    将内容转成字典格式
    :param content: 文本内容
    :param weight: 特征值
    :param f: simhash的bit位数
    :return: 海明距离值
    """
    c = []
    for jb in jieba.cut(content):
        if weight:
            v = weight.get(jb, 1)
        else:
            v = 1
        c.append((jb, v))
    return features_dict(c, f)


def hash_func(x):
    """hash算法"""
    return int(hashlib.md5(x).hexdigest(), 16)


def features_dict(features, f):
    """
    特征值字典
    :param features: 特征值
    :param f: simhash的bit位数
    :return: simhash值
    """
    v = [0] * f
    masks = [1 << i for i in range(f)]
    for values, weight in features:
        h = hash_func(values.encode('utf-8'))
        for i in range(f):
            v[i] += weight if h & masks[i] else -weight
    value = 0
    for i in range(f):
        if v[i] > 0:
            value |= masks[i]
    return value


def distance(sim_hash, another, f):
    """
    计算两个simhash的距离
    :param sim_hash: simhash值
    :param another: 另一个simhash的值
    :param f: simhash的bit位数
    :return: 海明距离
    """
    x = (sim_hash ^ another) & ((1 << f) - 1)
    value = 0
    while x:
        value += 1
        x &= x - 1
    return value


def ham_distance(chars, other_chars, weight=None, f=64):
    """
    比较那个字符串的海明距离
    :param chars: 字符串
    :param other_chars: 另一个字符串
    :param weight: 权重字典:weight={"电影": 3}
    :param f: samhash的bit位数
    :return: 海明距离值
    """
    v0 = handle(chars, weight, f)
    v1 = handle(other_chars, weight, f)
    return distance(v0, v1, f)


if __name__ == '__main__':
    print(ham_distance('我吃饭了,明天去看电影', '我在吃饭了,马上去看电影', weight={"电影": 3}))
