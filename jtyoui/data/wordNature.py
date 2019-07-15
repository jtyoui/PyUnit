#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/7/15  17:27
# @Author: jtyoui@qq.com
from jtyoui.file_zip import file_zip_path, sep


def word_nature():
    """读取file_zip下的word_nature文件，返回词性字典"""
    cx = {}
    with open(file_zip_path + sep + 'word_nature.txt', encoding='utf-8')as fp:
        for data in fp:
            data = data.strip()
            if data.startswith('[') and data.endswith(']'):
                key = data[1:-1]
                cx.setdefault(key, [])
            elif (not data.startswith('#')) and data:
                cx[key].append(data)
            else:
                pass
    return cx


if __name__ == '__main__':
    print(word_nature())
