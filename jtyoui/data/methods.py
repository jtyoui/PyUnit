#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 22:34
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from itertools import combinations_with_replacement, permutations, combinations
from collections.abc import Iterable
import random
import string
import collections
import re
import os
import unicodedata
import jtyoui
import copy
import hashlib

_special = "#$%&@"


# 随机选择字母:
def random_char(number=1):
    """随机选择字母

    :param number: 生成个数
    """
    ls = random.choices(string.ascii_letters, k=number)
    return ''.join(ls)


# 随机选择小写字母:
def random_lower_char(number=1):
    """随机选择小写字母

    :param number: 生成个数
    """
    ls = random.choices(string.ascii_lowercase, k=number)
    return ''.join(ls)


# 随机选择大写字母:
def random_upper_char(number=1):
    """随机选择大写字母

    :param number: 生成个数
    """
    ls = random.choices(string.ascii_uppercase, k=number)
    return ''.join(ls)


# 随机选择数字:
def random_digits(number=1):
    """随机选择数字

    :param number: 生成个数
    """
    ls = random.choices(string.digits, k=number)
    return ''.join(ls)


# 随机选择特殊字符:
def random_special(number=1):
    """随机选择特殊字符

    :param number: 生成个数
    """
    ls = random.choices(_special, k=number)
    return ''.join(ls)


def flag_contain_subset(str_: str, ls: list) -> bool:
    """输入一个字符串判断字符串的子集是否在ls列表中"""
    v = (True if subset in str_ else False for subset in ls)
    return any(v)


def contain_subset(str_: str, ls: list) -> (bool, list):
    """输入一个字符串判断字符串的子集是否在ls列表中,并且返回子集列表

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
    """输入一个字符串判断字符串是否属于某个列表的子集

    例如：str_：贵州，ls：[贵州省，遵义市]，那么贵州属于ls某个字符串的子集

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

    :param re_: 正则表达式
    :param str_: 字符串
    :param flag: re.search(re_, self.string, flag), 默认flag=0
    :param max_split: 最大分割数量
    """
    return re.split(pattern=re_, string=str_, maxsplit=max_split, flags=flag)


def replace(re_, repl, string_, count=0, flags=0):
    """支持正则替换"""
    return re.sub(re_, repl, string_, count, flags)


def remove_subset(ls: list) -> list:
    """去除列表中的子集

    比如：['aa','a','ab'] --> ['aa','ab']

    :param ls: 字符串列表
    :return: 返回去重后的结果
    """
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
    print("\033[5;31m" + ''.join(ls) + '\033[0m')
    return ls


def get_argCount(func) -> int:
    """获取函数对象的参数个数

    def sum(a,b):
        return(a+b)
    print(sum.__code__.co_argcount) # 2

    #输出的函数参数个数
    print(sum.__code__.co_varnames) # ('a', 'b')
    #这里会输出函数用到的所有变量名，不只是参数名

    print(sum.__defaults__) # None
    # 返回参数的初始值

    import inspect
    inspect.getargspec(sum) #ArgSpec(args=['a', 'b'], varargs=None, keywords=None, defaults=None)

    :param func: 函数对象
    :return: 函数对象的参数个数
    """
    return func.__code__.co_argcount


def strip(data: str, re_) -> str:
    """支持正则去除data中的数据。类似于str.strip()函数

    :param data: 数据
    :param re_: 去除data中的数据
    :return: 去除后的数据
    """

    @jtyoui.replace_regular(re_, '')
    def _(data_):
        return data_

    return _(data)


def find_unicodedata_name(data: str) -> list:
    """查询Unicode编码中的名字

    ♠ == BLACK SPADE SUIT
    \\N{BLACK SPADE SUIT} == ♠

    :param data: 字符串
    :return: 字符的Unicode名字列表
    """
    ls = []
    for i in data:
        ls.append(unicodedata.name(i))
    return ls


def join(chars: str, obj: Iterable) -> str:
    """同str.join函数一样，只不过数字会自动转为字符串

    :param chars: 要拼接的字符串
    :param obj: 拼接对象
    :return: 字符串
    """
    o = (str(i) for i in obj)
    return chars.join(o)


def find(str_: str, re_: str) -> list:
    """功能类似于str.find(),但是支持正则表达式

    :param str_: 字符串
    :param re_: 正则
    :return: 返回列表，包含元组：（匹配正则对象，匹配正则的开始索引）
    """
    return [(v, v.start()) for v in re.finditer(re_, str_)]


def key_value_re(key: list, value: list, value_re: str = None, key_re: str = None) -> list:
    """根据value值的索引获取key或者根据key的索引获取到value

    :param key: k值。['a','b']
    :param value: v值。[0,1]
    :param value_re: 根据值的正则获取key。比如：01正则表达式获取到ab
    :param key_re: 同理。根据key的正则。获取到值。比如：ab正则表达式。返回01
    """
    if key_re is None and value_re is None:
        raise TypeError('value_re和key_re必须写一个')
    if len(key) == len(value):
        if value_re:
            tool = jtyoui.Tool(join('', key))
            return tool.index_select_string(join('', value), value_re)
        else:
            tool = jtyoui.Tool(join('', value))
            return tool.index_select_string(join('', key), key_re)
    else:
        "这里当key和value不相等时。暂时没有想到怎么处理，比如：['我', '叫', '刘', '万', '光'], [6, 6, 10, 11, 11],这种情况"
    return []


def dict_key_value_re(dicts: dict, value_re: str = None, key_re: str = None) -> list:
    """根据字典的key-value来进行正则匹配

    根据value值的索引获取key或者根据key的索引获取到value
    同理：key_value_re函数

    >>> print(dict_key_value_re({'我': '6', '叫': '6', '张': '0', '伟': '1'}, value_re='01+'))

    :param dicts: 字典
    :param value_re: 根据值的正则获取key。比如：01正则表达式获取到ab
    :param key_re: 同理。根据key的正则。获取到值。比如：ab正则表达式。返回01
    """
    return key_value_re(key=list(dicts.keys()), value=list(dicts.values()), value_re=value_re, key_re=key_re)


def merge_address(work: str, address: list, new_address: list) -> list:
    """合并地址

    当模型无法提取一些地址的时候，需要手动添加一些地址，添加后的地址需要进行合并

    >>> print(merge_address('观山湖区长岭北路89号金融城B座', ['观山湖区'], ['观山湖区长岭北路']))

    :param work: 地址数据
    :param address: 地址1
    :param new_address: 地址2
    :return: 返回合并后的地址
    """
    char_ = chr(9775)
    work = work.replace(char_, '')
    flag = copy.deepcopy(work)
    address_ls = remove_subset(new_address + address)
    for addr in address_ls:
        flag = flag.replace(addr, char_ * len(addr))
    return key_value_re(list(work), list(flag), value_re=char_ + '{2,}')


def get_file_md5(file_path):
    """获取文件的MD5值

    :param file_path: 文件地址
    :return: MD5校验值
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'{file_path}文件不存在或者不是文件')
    hash_ = hashlib.md5()
    f = open(file_path, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        else:
            hash_.update(b)
    f.close()
    data = hash_.hexdigest()
    if data and isinstance(data, str):
        return data.upper()
    return ''


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
    for cns in char_number_split('我家住在北京', 4): print(cns)
    print(split('[.,，。]', '我家组在北京。我去玩，啊'))
    print(remove_subset(['aa', 'a', 'ab'] * 1_0000))
    print(combination(range(1, 20)))
    print(combination_repeat(range(1, 20)))
    print(permutation(range(1, 20)))
    print(is_chinese('张'), is_chinese('a'))
    print_heart()
    print(get_argCount(contain_subset))
    print(strip('张a伟', 'a'))
    print(find_unicodedata_name('♠'))
    print(key_value_re(['我', '叫', '刘', '万', '光'], [6, 6, 0, 1, 1], value_re='01+'))
    print(find('abc', 'a|b'))  # 查找a或者b的索引
    print(dict_key_value_re({'我': '6', '叫': '6', '张': '0', '伟': '1'}, value_re='01+'))
    print(merge_address('观山湖区长岭北路89号金融城B座', ['观山湖区'], ['观山湖区长岭北路']))
    print(get_file_md5(r'C:\Users\jtyou\Downloads\date.zip'))
