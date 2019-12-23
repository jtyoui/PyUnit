#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/9/25 15:12
# @Author: Jtyoui@qq.com
from jtyoui.error import CoordinateLengthNotEqualError


def map_replace(str_: str, key: [list, str] = None, value: [list, str] = None, maps: dict = None) -> str:
    """映射替换,最好使用maps字典映射

    >>> print(map_replace('[中国]', '[]', '【】')) #【中国】
    >>> print(map_replace('[中国]', maps={'[': '【', ']': '】'})) #【中国】

    :param str_: 字符串
    :param key: 替换字符
    :param value: 被替换的字符
    :param maps: 字符映射
    :return: 替换完毕的字符串
    """
    if maps:
        strings = str_
        for k, v in maps.items():
            strings = strings.replace(k, v)
        return strings
    else:
        if len(key) != len(value):
            raise CoordinateLengthNotEqualError('替换的长度必须相同！')
        if isinstance(key, list):
            key = ''.join(key)
        if isinstance(value, list):
            value = ''.join(value)
    m = str.maketrans(key, value)
    return str_.translate(m)


if __name__ == '__main__':
    print(map_replace('[中国]', '[]', '【】'))
    print(map_replace('[中国]', maps={'[': '【', ']': '】'}))
