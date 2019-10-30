#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 22:34
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from itertools import combinations_with_replacement, permutations, combinations
from jtyoui.decorator import replace_regular
import random
import string
import collections
import re
import os

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


def char_number_split(str_: str, number: int):
    """根据字符串个数来分割字符串"""
    while str_:
        yield str_[:number]
        str_ = str_[number:]


def split(re_, str_, flag=0, max_split=0) -> list:
    """支持正则分割
    :param re_:正则表达式
    :param str_:字符串
    :param flag: re.search(re_, self.string, flag), 默认flag=0
    :param max_split: 最大分割数量
    """
    return re.split(pattern=re_, string=str_, maxsplit=max_split, flags=flag)


def replace(re_, repl, string_, count=0, flags=0):
    """支持正则替换"""
    return re.sub(re_, repl, string_, count, flags)


def remove_subset(ls: list) -> list:
    """去除列表中的子集。比如：['aa','a','ab'] --> ['aa','ab']"""
    ls = sorted(ls, key=lambda x: len(x), reverse=True)
    total = []
    for subset in ls:
        if subset not in total:
            flag = True
            for word in total:
                if subset in word:
                    flag = False
                    break
            if flag:
                total.append(subset)
    return total


def rm_empty_dir(dir_path):
    """删除空目录"""
    for root, dirs, files in os.walk(dir_path):
        if not os.listdir(root):
            os.rmdir(root)


def combination(ls: iter, number=2) -> list:
    """组合：不重复"""
    c = combinations(ls, number)
    return list(c)


def combination_repeat(ls: iter, number=2) -> list:
    """组合：可重复"""
    c = combinations_with_replacement(ls, number)
    return list(c)


def permutation(ls: iter, number=2) -> list:
    """排列"""
    c = permutations(ls, number)
    return list(c)


def is_chinese(char: str) -> bool:
    """判断一个字符是否是中文
    :param char: 一个字符
    :return: 是中文返回真，否则是假
    """
    if len(char) == 1 and '\u4e00' < char < '\u9fa5':
        return True
    return False


def print_heart(s='♥'):
    """输出一个心脏的符号
    :param s: 字符串
    :return: 心脏的格式
    """
    ls = []
    s += ' '
    for y in range(15, -15, -1):
        flag = []
        for x in range(-30, 30):
            x1 = x * 0.04
            y1 = y * 0.1
            m = (x1 ** 2 + y1 ** 2 - 1) ** 3 - x1 ** 2 * y1 ** 3  # 心脏公式
            flag.append(s[(x - y) % len(s)] if m <= 0 else ' ')
        ls.append(''.join(flag) + '\n')
    print("\033[91m" + ''.join(ls))
    return ls


def get_argCount(func) -> int:
    """获取函数对象的参数个数

    def sum(a,b):
        return(a+b)
    print(sum.__code__.co_argcount)
    # 2
    #输出的函数参数个数
    print(sum.__code__.co_varnames)
    # ('a', 'b')
    #这里会输出函数用到的所有变量名，不只是参数名

    print(sum.__defaults__)
    # None
    # 返回参数的初始值

    import inspect
    inspect.getargspec(sum)
    # ArgSpec(args=['a', 'b'], varargs=None, keywords=None, defaults=None)
    :param func: 函数对象
    :return: 函数对象的参数个数
    """
    return func.__code__.co_argcount


def strip(data: str, re_) -> str:
    """支持正则去除data中的数据。类似于str.strip()函数
    :param data: 数据
    :param re_:去除data中的数据
    :return: 去除后的数据
    """

    @replace_regular(re_, '')
    def clean(data_):
        return data_

    return clean(data)


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
    for cns in char_number_split('我家住在北京', 4):
        print(cns)
    print(split('[.,，。]', '我家组在北京。我去玩，啊'))
    print(remove_subset(['aa', 'a', 'ab'] * 1_0000))
    print(combination(range(1, 20)))
    print(combination_repeat(range(1, 20)))
    print(permutation(range(1, 20)))
    print(is_chinese('张'), is_chinese('a'))
    print_heart()
    print(get_argCount(contain_subset))
    print(strip('张a伟', 'a'))
