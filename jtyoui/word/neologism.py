#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm
import math
import re
from jtyoui.regular import Non_Chinese
from jtyoui.decorators import replace_regular
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
        :param split_num: 分词的个数
        :param split_seq: 字符分割
        """
        ls = re.split(split_seq, st)
        self.read_ls(ls, split_num)

    def read_ls(self, ls, split_num):
        """数据类型[str]

        :param ls: 表示链表
        :param split_num: 分词的个数
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

        :param count: key出现的次数
        :param frequency: 过滤的频率
        :param cond: 过滤凝聚度
        :param free: 过滤自由度
        :return: 过滤后的数据字典
        """
        ls = []
        for key, one_word in self.ALL_WORDS.items():
            if len(key) <= 1:
                continue
            if (one_word[0] > count or one_word[1] > frequency) and one_word[2] > cond and one_word[3] > free:
                ls.append((key, one_word))
        return remove_subset(ls)


def remove_subset(ls: list) -> list:
    """去除列表中的子集。比如：['aa','a','ab'] --> ['aa','ab']"""
    ls.sort(key=lambda x: len(x[0]), reverse=True)
    total = []
    for subset in ls:
        flag = True
        for word in total:
            if subset[0] in word[0]:
                flag = False
                break
        if flag:
            total.append(subset)
    return total


def mains(file, split_num, count, frequency, cond, free):
    """成词发现算法。保存结果在当前运行环境下的result.txt文件中

    :param file: 文本地址
    :param split_num: 成词最大粒度
    :param count: key出现的次数
    :param frequency: 过滤的频率
    :param cond: 过滤凝聚度
    :param free: 过滤自由度
    """
    wf = open('result.txt', 'w', encoding='utf-8')
    n = Neologism()
    n.read_file(file, split_num)
    n.statistics()
    n.handle()
    print('正在保存文件数据：result.txt')
    for k, v in n.filter_words(count=count, frequency=frequency, cond=cond, free=free):
        s = F'关键字:{k} 次数:{v[0]} 频率:{v[1]} 凝聚度:{v[2]} 自由度:{v[3]}'
        wf.write(s + '\n')
    wf.flush()
    wf.close()
    print('保存完毕')


if __name__ == '__main__':
    mains(r'D:\data.txt', 6, count=10, frequency=0.0001, cond=84, free=0.7)
