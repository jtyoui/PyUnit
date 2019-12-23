#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:36
# @Author: Jtyoui@qq.com
from jtyoui.decorators import replace_regular
from jtyoui.regular import punctuation_re

import hashlib

"""
海明距离
在信息编码中，两个合法代码对应位上编码不同的位数称为码距，又称海明距离。
举例如下：10101和00110从第一位开始依次有第一位、第四、第五位不同，则海明距离为3。
"""


def handle(participle_ls, weight, f):
    """将内容转成字典格式

    :param participle_ls: 文本分词内容,是一个list分词对象
    :param weight: 特征值
    :param f: simHash的bit位数
    :return: 海明距离值
    """
    c = []
    for ls in participle_ls:
        if weight:
            v = weight.get(ls, 1)
        else:
            v = 1
        c.append((ls, v))
    return features_dict(c, f)


def hash_func(x):
    """hash算法"""
    return int(hashlib.md5(x).hexdigest(), 16)


def features_dict(features, f):
    """特征值字典

    :param features: 特征值
    :param f: simHash的bit位数
    :return: simHash值
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
    """计算两个simHash的距离

    :param sim_hash: simHash值
    :param another: 另一个simHash的值
    :param f: simHash的bit位数
    :return: 海明距离
    """
    x = (sim_hash ^ another) & ((1 << f) - 1)
    value = 0
    while x:
        value += 1
        x &= x - 1
    return value


def ham_distance(chars, other_chars, weight=None, f=64):
    """比较那个字符串的海明距离

    :param chars: 字符串
    :param other_chars: 另一个字符串
    :param weight: 权重字典:weight={"电影": 3}
    :param f: samHash的bit位数
    :return: 海明距离值
    """
    v0 = handle(chars, weight, f)
    v1 = handle(other_chars, weight, f)
    return distance(v0, v1, f)


@replace_regular(punctuation_re, '')
def simHash_similarity(text1: (str, dict), text2: (str, dict), weight: dict = None, f: int = 64) -> float:
    """文本相似度算法

    :param text1: 文本1
    :param text2: 文本2
    :param weight: 文本词权重
    :param f: hash bit位数
    :return: 相似度
    """
    v = ham_distance(text1, text2, weight=weight, f=f)
    return 1 - v / f


if __name__ == '__main__':
    a = ['我', '吃饭', '了', '明天', '去', '看', '电影']
    b = ['我', '在', '吃饭', '了', '马上', '去', '看', '电影']
    print(ham_distance(a, b, weight={"电影": 3}))
    print(simHash_similarity(''.join(a), ''.join(b)))
