#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/9 17:56
# @Author: Jtyoui@qq.com
import zipfile
import bz2


def unzip(zip_address, file_name, encoding='UTF-8'):
    """解压zip数据包

    :param zip_address: 压缩包的地址
    :param file_name: 压缩包里面文件的名字
    :param encoding: 文件的编码
    :return: 压缩包里面的数据：默认编码的UTF-8
    """
    f = zipfile.ZipFile(zip_address)
    fp = f.read(file_name)
    lines = fp.decode(encoding)
    return lines


def unbz2_one(bz2_address, file_name, encoding='UTF-8'):
    """解压bz2数据包

    :param bz2_address: 压缩包的地址
    :param file_name: 压缩包里面文件的名字
    :param encoding: 文件的编码
    :return: 压缩包里面的数据：默认编码的UTF-8
    """
    bz = bz2.BZ2File(bz2_address)
    text = bz.read()
    lines = text.decode(encoding)
    return lines


if __name__ == '__main__':
    print(unzip('D:\\date.zip', 'date.txt'))
