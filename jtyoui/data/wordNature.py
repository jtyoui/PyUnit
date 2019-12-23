#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/7/15  17:27
# @Author: jtyoui@qq.com
from jtyoui.file_zip import file_zip_path, sep


def word_nature():
    """读取file_zip下的word_nature文件，返回词性字典"""
    p = file_zip_path + sep + 'word_nature.txt'
    cx = reader_conf(p)
    return cx


def reader_conf(path: str, encoding: str = 'UTF-8') -> dict:
    """读取配置文件
    [capitalize]
    a
    b

    :param path: 配置文件路径
    :param encoding: 文件编码
    """
    cx = {}
    with open(path, encoding=encoding)as fp:
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


def save_conf(cx: dict, path: str, encoding='UTF-8'):
    """保存配置文件

    :param cx: 保存的字典类型：{str：list}
    :param path: 保存的路径
    :param encoding: 保存文件的编码
    """
    with open(path, 'w', encoding=encoding, newline='\n')as fp:
        for key, value in cx.items():
            fp.write(f'[{key}]\n')
            if isinstance(value, (list, tuple)):
                for v in value:
                    fp.write(v.strip() + '\n')
            else:
                raise TypeError('字典的值必须是列表或者元组类型')


if __name__ == '__main__':
    print(word_nature())
