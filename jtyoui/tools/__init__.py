#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/12 13:13
# @Author: Jtyoui@qq.com
import re
from jtyoui.error import InconsistentLengthError
from dataclasses import dataclass
import operator


@dataclass
class Tool:
    """自定义工具类"""
    _string: str

    def index_select_string(self, index, select):
        """利用索引的关系来找字符串"""
        """
        利用索引的关系来找字符串:一般用在深度学习中的标注模型
        :param index: 索引
        :param string: 字符串
        :param select: 索引匹配的正则
        :return: 匹配字符串列表
        """
        ls, string = [], self._string
        if len(index) != len(self._string):
            raise InconsistentLengthError("参数index和参数string长度不一致错误!")
        while True:
            s = re.search(select, index)
            if s:
                ls.append(string[s.start():s.end()])
                index = index[s.start() + 1:]
                string = string[s.start() + 1:]
            else:
                break
        return ls

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        self._string = string

    def split(self, re_, flag=0, retain=True):
        """支持正则分割"""
        """
        :param re_:正则表达式
        :param flag: re.search(re_, self.string, flag), 默认flag=0
        :param retain: 是否要保留正则匹配的字符,默认是保留
        """
        ls_index, ls_word, string, end = [0], [], self._string, 0
        while True:
            match = re.search(re_, string, flag)
            if match:
                ls_index.append(match.start() + end)
                end += match.end()
                string = string[match.end():]
            else:
                break
        if ls_index[-1] != len(self._string):
            ls_index.append(len(self._string))
        if ls_index[1] == 0:
            ls_index.pop(0)
        for index, value in enumerate(ls_index):
            if index == len(ls_index) - 1:
                break
            ls_word.append(self._string[value:ls_index[index + 1]])
        if not retain:
            ls_words = []
            for word in ls_word:
                match = re.search(re_, word, flag)
                if match:
                    w = word[match.end():]
                    if w:
                        ls_words.append(w)
            ls_word = ls_words
        return ls_word

    def string_select_index(self, ls, start_name, end_name, flag='O', labels=None):
        """将一段文字进行标记返回标记的列表"""
        """
        :param ls:标记的关键字列表
        :param start_name:开始标记的名称
        :param end_name:连续标记的名称
        :param flag:不在关键字列表中默认标记，默认是O,大写的o
        :param labels:自定义标记
        """
        if not labels:
            labels = [flag for _ in range(len(self._string))]
        for word in ls:
            index = 0
            while True:
                start = self._string.find(word, index)
                if start > -1:
                    end = start + len(word)
                    labels[start] = start_name
                    for i in range(start + 1, end):
                        labels[i] = end_name
                    index = end
                else:
                    break
        return labels


def select_row(iterable_, row):
    """选取可迭代对象中的某一列"""
    """
    :param iterable_:可迭代对象
    :param row:每一列
    """
    g = operator.itemgetter(row)
    return [g(i) for i in iterable_]


if __name__ == '__main__':
    tool = Tool('我家在贵州省遵义县的一个地方是虾子')
    i_s = tool.index_select_string('01056666600000056', '56+')
    print(i_s)
    tool.string = '一、相亲最大的好处是。二、想要什么婚姻。三五、开放型的婚姻是凉鞋。三、'
    t_s = tool.split('[一二三四五六七八九十]+、', retain=True)
    print(t_s)
    tool.string = '我家在贵州省遵义县的一个地方是虾子'
    s_i = tool.string_select_index(ls=['贵州省', '遵义县', '虾子'], start_name='5', end_name='6')
    print(s_i)
    d = [
        [1, 2, 3],
        [1, 0, -1],
        [0, 1, 1]
    ]
    print(select_row(d, 1))  # [2, 0, 1]
