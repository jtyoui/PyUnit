#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm
import math
import re
from jtyoui.regular import Non_Chinese
from jtyoui.decorator import replace_regular
from collections import Counter
import os


@replace_regular(Non_Chinese, '')
def clean(data):
    # 去除非中文字符
    return data, len(data)


class Neologism:
    def __init__(self):
        self.ALL_WORDS = dict()
        self.All_LENS = 0

    def read_file(self, file, split_num):
        """按文件读取
        :param file: 文件地址
        :param split_num: 最大分割词语
        """
        if os.path.exists(file):
            with open(file, encoding='utf-8') as fp:
                for line in fp:
                    self.read_string(line, split_num)

    def read_string(self, st, split_num, split_seq='[，。！？：.,?]'):
        """按字符按照split_seq格式来分割
        :param st: 字符串
        :param split_num:分词的个数
        :param split_seq: 字符分割
        :return: None
        """
        ls = re.split(split_seq, st)
        self.read_ls(ls, split_num)

    def read_ls(self, ls, split_num):
        """数据类型[str]
        :param ls: 表示链表
        :param split_num:分词的个数
        """
        for word in ls:
            self.All_LENS += len(word)
            clean_data, lens = clean(data=word)
            if lens > 2:
                self._split(clean_data, lens, split_num)

    def _split(self, words, lens, split_num):
        """拆分字符，最大匹配num个字符，并也字典的形式返回，
        [出现次数,出现频率,凝固程度,自由程度,关键字的左邻,关键字的右邻](作为信息熵的衡量)
        """
        for i in range(lens):
            for j in range(i + 1, split_num + 1 + i):
                if j < lens:
                    key = words[i:j]
                    word = self.ALL_WORDS.get(key)
                    if word:
                        word[0] += 1
                        word[4].append(words[i - 1])
                        word[5].append(words[j])
                    else:
                        self.ALL_WORDS[key] = [1, 0.0, 1, 0, [words[i - 1]], [words[j]]]

    def statistics(self):
        """统计每个单词的频率"""
        for key in self.ALL_WORDS:
            self.ALL_WORDS[key][1] = self.ALL_WORDS[key][0] / self.All_LENS

    def _information_entropy(self, word_ls):
        """信息熵"""
        entropy_all = 0.0
        key_count = Counter(word_ls)
        for key, count in key_count.items():
            word = self.ALL_WORDS.get(key)
            if word:
                entropy_all -= math.log(word[1]) * word[1] * count  # 邻字的信息熵
        return entropy_all

    def handle(self):
        """处理数据
        计算左邻字集合和右邻字集合的频率，左邻字信息熵和右邻字信息熵中的较小值
        计算凝固程度,自由程度
        """
        for key, word_list in self.ALL_WORDS.items():
            if len(key) > 1:
                # 左邻字集合的凝聚度和右邻字集合的凝聚度相比较.谁越少说明该词语越容易接近谁
                left = word_list[1] / (self.ALL_WORDS[key[0]][1] * self.ALL_WORDS[key[1:]][1])  # 左邻字集合的凝聚度
                right = word_list[1] / (self.ALL_WORDS[key[-1]][1] * self.ALL_WORDS[key[:-1]][1])  # 右邻字集合的凝聚度
                word_list[2] = left if left < right else right
                # 左邻字集合的信息熵和右邻字集合的信息熵的相比较.谁的信息熵越少说明该集合提供的信息越大
                front_all = self._information_entropy(word_list[4])  # 左邻字集合的信息熵
                end_all = self._information_entropy(word_list[5])  # 右邻字集合的信息熵
                word_list[3] = front_all if front_all < end_all else end_all

    def filter_words(self, count, frequency, cond, free):
        """过滤一些不重要的数据
        [出现次数,出现频率,凝固程度,自由程度]
        :param count:key出现的次数
        :param frequency: 过滤的频率
        :param cond:过滤凝聚度
        :param free:过滤自由度
        :return:过滤后的数据字典
        """
        for key, one_word in self.ALL_WORDS.items():
            if len(key) <= 1:
                continue
            if (one_word[0] > count or one_word[1] > frequency) and one_word[2] > cond and one_word[3] > free:
                yield key, one_word


if __name__ == '__main__':
    n = Neologism()
    n.read_file(r'D:\data.txt', 6)
    n.statistics()
    n.handle()
    for k, v in n.filter_words(count=10, frequency=0.0001, cond=84, free=0.7):
        print(F'关键字:{k} 次数:{v[0]} 频率:{v[1]} 凝聚度:{v[2]} 自由度:{v[3]}')
