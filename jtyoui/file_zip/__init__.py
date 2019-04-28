#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/22 11:41
# @Author: Jtyoui@qq.com
import zipfile
from os import path


def load_zip(zip_name, file_name):
    """加载zip数据
    :param zip_name:模型名字
    :param file_name:文件名字
    :return: 模型数据
    """
    file_zip = path.dirname(path.abspath(__file__))
    file_zip = path.join(path.dirname(file_zip), 'file_zip', zip_name)
    f = zipfile.ZipFile(file_zip)
    fp = f.read(file_name)
    lines = fp.decode('utf-8').split('\n')
    return lines


if __name__ == '__main__':
    line = load_zip('train.zip', 'train.txt')
    for l in line:
        print(l)

# 关于文件压缩包目录
# py.zip是汉语拼音
# train.zip是中国火车站名字压缩包
