#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/4 0004
# @Email : jtyoui@qq.com
# @Software : PyCharm
from jtyoui.data import Han_J_F  # 引入简体字与繁体字的映射表

J_F, F_J = Han_J_F, {f: j for j, f in Han_J_F.items()}  # 简体字:J表示, 繁体字用F表示


def j_to_f(str_):
    """简体字转繁体字

    :param str_: 字符串
    :return: 转换后的字符串生成器
    """
    for s in str_:
        yield J_F.get(s, s)


def f_to_j(str_):
    """繁体字转简体字

    :param str_: 字符串
    :return: 转换后的字符串生成器
    """
    for s in str_:
        yield F_J.get(s, s)


if __name__ == '__main__':
    j = j_to_f('千载正字一夕改,如今吾辈来重光!')
    print(''.join(j))
    f = f_to_j('千載正字一夕改,如今吾輩來重光!')
    print(''.join(f))
