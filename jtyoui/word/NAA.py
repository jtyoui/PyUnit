#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2018/2/28 10:58
# @Author: Jtyoui@qq.com
import math

"""
NAA(New Word Analysis Algorithms):分析新词算法
"""


class NAA:
    all_lens = 0.0
    naa_words = dict()

    def __init__(self, split_num=4, seq=0.001, cond=50, free=0.5):
        """初始化参数

        :param split_num: 匹配个数
        :param seq: 关键字出现的频率
        :param cond: 凝固程度
        :param free: 自由程度
        """
        self.split_num = split_num
        self.seq = seq
        self.cond = cond
        self.free = free

    def read_ls(self, ls):
        st = ''.join(ls)
        self.all_lens = len(st)
        for word in ls:
            self.split(words=word)
        print("split over!")

    def __read_ls(self, ls):
        """读取链表，格式是[str,str,str,.....]一维链表

        :param ls: 链表
        """
        for word in ls:
            self.split(words=word)
        print("split over!")

    def read_string(self, st, split_seq='\n'):
        """讲字符按照split_seq格式来分割

        :param st: 字符串
        :param split_seq: 字符分割
        :return: None
        """
        self.all_lens = len(st)
        ls = st.split(split_seq)
        print("reader over!")
        self.__read_ls(ls=ls)

    def read_file(self, file, file_encoding='utf-8-sig'):
        """读取文件内容，注意文件是UTF-8的格式且不是BOM格式

        :param file: 读取的文件
        :param file_encoding: 文本编码
        """
        fp = open(file, "r", encoding=file_encoding)
        d = fp.read()
        self.read_string(st=d)
        fp.close()

    def split(self, words):
        """拆分字符，最大匹配num个字符，并也字典的形式返回

        [出现次数,出现频率,凝固程度,自由程度,关键字的左邻,关键字的右邻](作为信息熵的衡量)
        """
        lens = len(words)
        for i in range(0, lens):
            for j in range(1, self.split_num + 1):
                if i + j < lens:
                    k = words[i:i + j]
                    word = self.naa_words.get(k)
                    if word:
                        word[0] += 1
                        word[1] = word[0] / self.all_lens
                        word[4].append(words[i - 1])
                        word[5].append(words[i + 1])
                    else:
                        self.naa_words[k] = [1, 1 / self.all_lens, 1, 0, [words[i - 1]], [words[i + 1]]]

    def handle(self):
        """处理数据
        计算左邻字集合和右邻字集合有多随机，左邻字信息熵和右邻字信息熵中的较小值
        计算凝固程度,自由程度
        """
        for k in self.naa_words:
            if len(k) == 1:
                continue
            word = self.naa_words[k]
            end_all = front_all = 0.0
            left = word[1] / (self.naa_words[k[0]][1] * self.naa_words[k[1:]][1])
            right = word[1] / (self.naa_words[k[-1]][1] * self.naa_words[k[:-1]][1])

            for front in word[4]:
                if front in self.naa_words:
                    front_all -= math.log(self.naa_words[front][1]) * self.naa_words[front][1]

            for end in word[5]:
                if end in self.naa_words:
                    end_all -= math.log(self.naa_words[end][1]) * self.naa_words[end][1]

            word[2] = left if left < right else right
            word[3] = front_all if front_all < end_all else end_all
        print("handle over!")

    def filter(self, filter_cond=10, filter_free=0.5, flag=False):
        """过滤一些不重要的数据

        [出现次数,出现频率,凝固程度,自由程度]

        :param filter_cond: 过滤凝聚度
        :param filter_free: 过滤自由度
        :param flag: 是否是并且还是或者,默认是或者，满足一个就过滤
        :return: 过滤后的数据字典
        """
        key_words = dict()
        for k in self.naa_words:
            if len(k) <= 1:
                continue
            splits = self.naa_words[k]
            if splits[1] > self.seq and splits[2] > self.cond and splits[3] > self.free:
                key_words[k] = [splits[0], splits[1], splits[2], splits[3]]

        new_key = key_words.copy()
        keys = key_words.keys()
        for max_key in keys:
            """
                去除关键字像：中国新时，这种不能分成更多的词语
            """
            lens = len(max_key)
            if lens > 4:
                i = 2
                split_flag = 0
                while i <= lens:
                    if max_key[split_flag:i] in keys and max_key[split_flag:i] != max_key:
                        split_flag = i
                    i += 1
                if split_flag != lens:
                    new_key.pop(max_key)
                    continue
            for min_key in keys:
                """
                    去除子集
                """
                max_keys = key_words[max_key]
                if max_key in min_key and max_key != min_key:
                    if max_keys[0] <= key_words[min_key][0] + 5:
                        new_key.pop(max_key)
                        break
                    else:
                        if flag:
                            if max_keys[2] < filter_cond and max_keys[3] < filter_free:
                                new_key.pop(max_key)
                                break
                        elif max_keys[2] < filter_cond or max_keys[3] < filter_free:
                            new_key.pop(max_key)
                            break

        print("filter over!")
        return new_key


if __name__ == '__main__':
    naa = NAA(split_num=10, seq=0.0001)
    naa.read_file(file=r"D:\data.txt")
    naa.handle()
    data = naa.filter(filter_free=0.7, filter_cond=84, flag=False)
    for key, value in data.items():
        print(F'关键字:{key},次数:{value[0]},频率:{value[1]},凝聚度:{value[2]},自由度:{(value[3])}')
