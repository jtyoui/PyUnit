#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm


import math
import re
from jtyoui.regular import Non_Chinese
from jtyoui.decorator import replace_regular
import os

ALL_WORDS = dict()
All_LENS = 0


def read_string(st, split_num, split_seq='[，。！？：.,?]'):
    """
    讲字符按照split_seq格式来分割
    :param st: 字符串
    :param split_num:分词的个数
    :param split_seq: 字符分割
    :return: None
    """
    ls = re.split(split_seq, st)
    read_ls(ls, split_num)


def read_ls(ls, split_num):
    """数据类型[str]
    :param ls: 表示链表
    :param split_num:分词的个数
    """
    global All_LENS
    for word in ls:
        All_LENS += len(word)
        clean_data, lens = clean(data=word)
        if lens > 2:
            split(clean_data, lens, split_num)


def split(words, lens, split_num):
    """
    拆分字符，最大匹配num个字符，并也字典的形式返回，
    [出现次数,出现频率,凝固程度,自由程度,关键字的左邻,关键字的右邻](作为信息熵的衡量)
    """
    for i in range(0, lens):
        for j in range(1, split_num + 1):
            if i + j < lens:
                key = words[i:i + j]
                word = ALL_WORDS.get(key)
                if word:
                    word[0] += 1
                    word[4].append(words[i - 1])
                    word[5].append(words[i + j])
                else:
                    ALL_WORDS[key] = [1, 0.0, 1, 0, [words[i - 1]], [words[i + j]]]


def statistics():  # 统计每个单词的频率
    for key in ALL_WORDS:
        ALL_WORDS[key][1] = ALL_WORDS[key][0] / All_LENS


def handle():
    """
    处理数据
    计算左邻字集合和右邻字集合的频率，左邻字信息熵和右邻字信息熵中的较小值
    计算凝固程度,自由程度
    """
    for key in ALL_WORDS:
        word_list = ALL_WORDS[key]  # 获得一个单词的链表信息
        if len(key) == 1:
            continue
        end_all = front_all = 0.0
        left = word_list[1] / (ALL_WORDS[key[0]][1] * ALL_WORDS[key[1:]][1])  # 左邻字集合的频率
        right = word_list[1] / (ALL_WORDS[key[-1]][1] * ALL_WORDS[key[:-1]][1])  # 右邻字集合的频率

        for front in word_list[4]:
            if ALL_WORDS.get(front):
                front_all -= math.log(ALL_WORDS[front][1]) * ALL_WORDS[front][1]  # 左邻字的信息熵

        for end in word_list[5]:
            if ALL_WORDS.get(end):
                end_all -= math.log(ALL_WORDS[end][1]) * ALL_WORDS[end][1]  # 右邻字的信息熵

        # 左邻字集合和右邻字集合的频率相比较.谁越少说明该词语越容易接近谁
        word_list[2] = left if left < right else right

        # 左邻字集合的信息熵和右邻字集合的信息熵的相比较.谁的信息熵越少说明该集合提供的信息越大
        word_list[3] = front_all if front_all < end_all else end_all


def filter_words(frequency, cond, free, flag):
    """
    过滤一些不重要的数据
    [出现次数,出现频率,凝固程度,自由程度]
    :param frequency: 过滤的频率
    :param cond:过滤凝聚度
    :param free:过滤自由度
    :param flag: 是否是并且还是或者,默认是或者，满足一个就过滤
    :return:过滤后的数据字典
    """
    key_words = dict()
    for key in ALL_WORDS.keys():
        if len(key) <= 1:
            continue
        one_word = ALL_WORDS[key]
        if flag:
            if one_word[1] > frequency and one_word[2] > cond and one_word[3] > free:
                key_words[key] = [one_word[0], one_word[1], one_word[2], one_word[3]]
        else:
            if one_word[1] > frequency or one_word[2] > cond or one_word[3] > free:
                key_words[key] = [one_word[0], one_word[1], one_word[2], one_word[3]]
    return key_words


@replace_regular(Non_Chinese, '')
def clean(data):
    # 去除非中文字符
    return data, len(data)


def analysis_single(file_str, split_num=4, frequency=0.0001, cond=10, free=0.1, flag=False):
    """
    :param file_str: 训练的文本,或者字符串,或者是句子列表
    :param split_num: 匹配个数
    :param frequency: 频率
    :param cond: 凝聚度
    :param free: 自由度
    :param flag:是否是并且还是或者,默认是或者，满足一个就过滤
    :return: 分析完毕的字典
    """
    if os.path.exists(file_str):
        with open(file_str, encoding='utf-8') as fp:
            for line in fp:
                read_string(line, split_num)
    elif isinstance(file_str, list):
        read_ls(file_str, split_num)
    else:
        read_string(file_str, split_num)

    print("开始统计频率.........")
    statistics()

    print("开始处理数据.........")
    handle()

    print("开始过滤数据.........")
    return filter_words(frequency, cond, free, flag)


if __name__ == '__main__':
    neologism_words = analysis_single(r'D:\data.txt', 6, 0.00001, 100, 0.1, flag=True)
    for k, v in neologism_words.items():
        print('key:{0} count:{1} frequency:{2} cond:{3} free:{4}'.format(k, v[0], v[1], v[2], v[3]))
