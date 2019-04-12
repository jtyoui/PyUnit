#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/12 13:13
# @Author: Jtyoui@qq.com
import re
from jtyoui.error import InconsistentLengthError


def index_select_string(index, string, select):
    """利用索引的关系来找字符串"""
    """
    利用索引的关系来找字符串:一般用在深度学习中的标注模型
    :param index: 索引
    :param string: 字符串
    :param select: 索引匹配的正则
    :return: 匹配字符串列表
    """
    ls = []
    if len(index) != len(string):
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


if __name__ == '__main__':
    s = index_select_string('01056666600000056', '我家在贵州省遵义县的一个地方是虾子', '56+')
    print(s)
