#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 22:34
# @Email  : jtyoui@qq.com
# @Software: PyCharm
import random
import string
import collections

_special = "#$%&@"


# 随机选择字母:
def random_char(number=1):
    """随机选择字母:number是生成个数"""
    ls = random.choices(string.ascii_letters, k=number)
    return ''.join(ls)


# 随机选择小写字母:
def random_lower_char(number=1):
    """随机选择小写字母:number是生成个数"""
    ls = random.choices(string.ascii_lowercase, k=number)
    return ''.join(ls)


# 随机选择大写字母:
def random_upper_char(number=1):
    """随机选择大写字母:number是生成个数"""
    ls = random.choices(string.ascii_uppercase, k=number)
    return ''.join(ls)


# 随机选择数字:
def random_digits(number=1):
    """随机选择数字:number是生成个数"""
    ls = random.choices(string.digits, k=number)
    return ''.join(ls)


# 随机选择特殊字符:
def random_special(number=1):
    """随机选择特殊字符:number是生成个数"""
    ls = random.choices(_special, k=number)
    return ''.join(ls)


def flag_contain_subset(str_: str, ls: list) -> bool:
    """输入一个字符串判断字符串的子集是否在ls列表中"""
    v = (True if subset in str_ else False for subset in ls)
    return any(v)


def contain_subset(str_: str, ls: list) -> (bool, list):
    """
    输入一个字符串判断字符串的子集是否在ls列表中,并且返回子集列表
    :param str_: 字符串
    :param ls: 字符串列表
    :return: 存在返回True。不存在返回False。都会返回list列表
    """
    v = [subset for subset in ls if subset in str_]
    return any(v), v


def max_str(ls: list):
    """统计字符串列表出现字符串最多的字符串"""
    c = collections.Counter(ls)
    return max(c.keys(), key=c.get)


def contain_list_subset(str_: str, ls: list) -> (bool, list):
    """
    输入一个字符串判断字符串是否属于某个列表的子集。例如：str_：贵州，ls：[贵州省，遵义市]，那么贵州属于ls某个字符串的子集
     :param str_: 字符串
    :param ls: 字符串列表
    :return: 存在返回True。不存在返回False。都会返回list列表
    """
    v = [subset for subset in ls if str_ in subset]
    return any(v), v


if __name__ == '__main__':
    print(random_char(4))
    print(random_lower_char(4))
    print(random_special(4))
    print(random_upper_char(4))
    print(random_digits(4))
    print(flag_contain_subset('我家住在北京', '家住、诉求、请求'.split('、')))
    print(contain_subset('我家住在北京', '家住、诉求、请求'.split('、')))
    print(max_str(['a', 'a', 'a', 'b', 'c', 'd', 'd']))
    print(contain_list_subset('贵州', ['贵州省', '遵义市', '贵州省贵阳市']))
