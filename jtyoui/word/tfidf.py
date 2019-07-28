#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/7/28 11:58
# @Author: jtyoui@qq.com
import math
from jtyoui.tools import Tool


class TFIDF:

    def __init__(self):
        """增加IFIDF"""
        self.word = None
        self.length = 0
        self.data = None
        self.ls = None

    def input_str(self, str_):
        self.data = str_
        if not self.ls:
            self.input_ls(Tool(str_).split('[。？！.?!]', retain=False))

    def input_ls(self, ls):
        self.length = len(ls)
        self.ls = ls
        if not self.data:
            self.input_str('。'.join(ls))

    def get_tf_idf(self, word):
        """传入一个词语，获得重要性"""
        self.word = word
        c, t = 0, 0
        for line in self.ls:
            num = line.count(self.word)
            if num:
                t += num / len(line)
                c += 1
        return t * math.log10(self.length / c)


if __name__ == '__main__':
    tfidf = TFIDF()
    tfidf.input_str("这是只猫,猫是朋友。这是只狗,狗是朋友")
    print(tfidf.get_tf_idf('猫'))
    print(tfidf.get_tf_idf('这'))
