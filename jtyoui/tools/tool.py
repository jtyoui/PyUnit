#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/12 13:13
# @Author: Jtyoui@qq.com
import re
from jtyoui.error import InconsistentLengthError
import operator


class Tool:
    """自定义工具类

    >>> tool = Tool('我家在贵州省遵义县的一个地方是虾子')
    >>> i_s = tool.index_select_string('01056666600000056', '56+')
    >>> print(i_s)
    >>> tool.string = '我在这里、一、相亲最大的好处是。二、想要什么婚姻。三五、开放型的婚姻是凉鞋。'
    >>> t_s = tool.split('[一二三四五六七八九十]+、', retain=False)
    >>> print(t_s)
    >>> tool.string = '我家在贵州省遵义县的一个地方是虾子'
    >>> s_i = tool.string_select_index(ls=['贵州省', '遵义县', '虾子'], start_name='5', end_name='6')
    >>> print(s_i)
    >>> d = [[1, 2, 3],[1, 0, -1],[0, 1, 1]]
    >>> print(tool.select_row(d, 1))  # [2, 0, 1]
    >>> tool.generator = False
    >>> print(tool.select_ls(['遵义县', '虾子']))
    >>> tool.string = '9994599945545599945'
    >>> ts = tool.search('(45+)+')
    >>> print(ts.start(), ts.end(), ts.value())
    >>> print(tool.string)
    >>> tool.string = 'are you fuck!'
    >>> print(tool.replace('[0-9a-zA-Z]', ''))
    """
    generator = True

    def __init__(self, string):
        self._string = string

    def index_select_string(self, index, select):
        """利用索引的关系来标记字符串

        利用索引的关系来找字符串:一般用在深度学习中的标注模型

        :param index: 索引
        :param select: 索引匹配的正则
        :return: 匹配字符串列表
        """
        if len(index) != len(self._string):
            raise InconsistentLengthError("参数index和参数string长度不一致错误!")
        rf = re.finditer(select, index)
        return [self._string[r.start():r.end()] for r in rf]

    @property
    def string(self):
        """更新字符串"""
        return self._string

    @string.setter
    def string(self, string):
        self._string = string

    def split(self, re_, flag=0, retain=True):
        """支持正则分割

        :param re_: 正则表达式
        :param flag: re.search(re_, self.string, flag), 默认flag=0
        :param retain: 是否要保留正则匹配的字符,默认是保留
        """
        ls_word = re.split(pattern=re_, string=self._string, flags=flag)
        if retain:
            rs = re.finditer(pattern=re_, string=self._string, flags=flag)
            for index, r in enumerate(rs, start=1):
                ls_word[index] = r.group() + ls_word[index]
        return ls_word

    def string_select_index(self, ls, start_name, end_name, flag='O', labels=None):
        """将一段文字进行标记返回标记的列表

        :param ls: 标记的关键字列表
        :param start_name: 开始标记的名称
        :param end_name: 连续标记的名称
        :param flag: 不在关键字列表中默认标记，默认是O,大写的o
        :param labels: 自定义标记
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

    def select_ls(self, ls_):
        """根据列表里面的元素选取字符串中的元素

        :param ls_: 列表元素，比如['张三','李四','王麻子']，string='张三去李四家找东西'
        :return: ['张三','李四']
        """
        if self.generator:
            return (name for name in ls_ if self._string.find(name) > 0)
        else:
            return [name for name in ls_ if self._string.find(name) > 0]

    def select_row(self, iterable_, row):
        """选取可迭代对象中的某一列

        :param iterable_: 可迭代对象
        :param row: 每一列
        """
        g = operator.itemgetter(row)
        if self.generator:
            return (g(i) for i in iterable_)
        else:
            return [g(i) for i in iterable_]

    def search(self, pattern, flags=0):
        """根据正则获取字符串的索引以及值，索引和值都是list类型"""
        r = re.search(pattern, self.string, flags=flags)
        start, end, value = [], [], []
        flag = ''
        while r:
            start_ = r.start() + len(flag)
            end_ = r.end() + len(flag)
            start.append(start_)
            end.append(end_)
            value.append(self.string[start_:end_])
            flag = self.string[:end_]
            string = self.string[end_:]
            r = re.search(pattern, string, flags=flags)

        class _:

            @staticmethod
            def start():
                return start

            @staticmethod
            def end():
                return end

            @staticmethod
            def value():
                return value

        return _()

    def replace(self, pattern, repl, count=0, flags=0):
        """正则替换"""
        return re.sub(pattern, repl, self.string, count=count, flags=flags)


if __name__ == '__main__':
    tool = Tool('我家在贵州省遵义县的一个地方是虾子')
    i_s = tool.index_select_string('01056666600000056', '56+')
    print(i_s)
    tool.string = '我在这里、一、相亲最大的好处是。二、想要什么婚姻。三五、开放型的婚姻是凉鞋。'
    t_s = tool.split('[一二三四五六七八九十]+、', retain=False)
    print(t_s)
    tool.string = '我家在贵州省遵义县的一个地方是虾子'
    s_i = tool.string_select_index(ls=['贵州省', '遵义县', '虾子'], start_name='5', end_name='6')
    print(s_i)
    d = [
        [1, 2, 3],
        [1, 0, -1],
        [0, 1, 1]
    ]
    print(tool.select_row(d, 1))  # [2, 0, 1]
    tool.generator = False
    print(tool.select_ls(['遵义县', '虾子']))

    tool.string = '9994599945545599945'
    ts = tool.search('(45+)+')
    print(ts.start(), ts.end(), ts.value())
    print(tool.string)

    tool.string = 'are you fuck!'
    print(tool.replace('[0-9a-zA-Z]', ''))
