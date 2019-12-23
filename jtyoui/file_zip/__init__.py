#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/22 11:41
# @Author: Jtyoui@qq.com
import zipfile
from os import path

file_zip_path = path.dirname(path.abspath(__file__))
sep = path.sep


def load_zip(zip_name, file_name, encoding='UTF-8', sep='\n'):
    """加载zip数据

    :param zip_name: 压缩包的名字
    :param file_name: 压缩包里面文件的名字
    :param encoding: 文件的编码
    :param sep: 压缩文件里面的换行符
    :return: 压缩包里面的数据：默认编码的UTF-8
    """
    file_zip = path.join(file_zip_path, zip_name)
    f = zipfile.ZipFile(file_zip)
    fp = f.read(file_name)
    lines = fp.decode(encoding).split(sep)
    return lines


if __name__ == '__main__':
    line = load_zip('train.zip', 'train.txt')
    for l in line:
        print(l)

# 关于文件压缩包目录
# py.zip是汉语拼音
# train.zip是中国火车站名字压缩包
# city.zip是中国天气预报城市与编码
