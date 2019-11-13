#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/13 15:08
# @Author: Jtyoui@qq.com
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer

"""
one-hot编码测试用例
"""
if __name__ == '__main__':
    # .toarray()返回的是ndarray格式，.todense()返回的是matrix格式

    x = [{'city': 'a', 'age': 1}, {'city': 'b', 'age': 2}, {'city': 'c', 'age': 3}]
    d = DictVectorizer()
    print(d.fit_transform(x).toarray())

    corpus = ['UNC played Duke in basketball', 'Duke lost the basketball game']
    count = CountVectorizer()
    print(count.fit_transform(corpus).toarray())
