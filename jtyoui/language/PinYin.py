#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/22 11:44
# @Author: Jtyoui@qq.com

import zipfile
from jtyoui.data import letter_maps  # 声调映射表
from os import path


def load_pin_yin(tone=False):
    """加载拼音模型字典

    参数：True 有声调， False没有声调

    :param tone: 是否要加载声调
    :return: 拼音模型字典
    """
    d = {}
    file_zip = path.dirname(path.abspath(__file__))
    file_zip = path.join(path.dirname(file_zip), 'file_zip', 'py.zip')
    f = zipfile.ZipFile(file_zip)
    fp = f.read('py.txt')
    lines = fp.decode('utf-8').split('\n')
    for line in lines:
        v, k = line.split('#')
        if ',' in v:
            v = v[:v.index(',')]
        if tone:
            d.setdefault(k, v)
        else:
            vs = ''
            for v_ in v:
                vs += letter_maps[v_]
            d.setdefault(k, vs)
    return d


def chinese_to_pin_yin(pin_yin, string_):
    """将汉字转为拼音

    :param pin_yin: 拼音模型
    :param string_: 汉字
    :return: 拼音列表
    """
    py = []
    for str_ in string_:
        data = pin_yin.get(str_)
        if data:
            py.append(data)
        else:
            py.append('@')
    return py


if __name__ == '__main__':
    load = load_pin_yin(True)
    print(chinese_to_pin_yin(load, '我喜欢你！'))
    load = load_pin_yin(False)
    print(chinese_to_pin_yin(load, '你好！世界'))
