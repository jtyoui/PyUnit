#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/9 17:56
# @Author: Jtyoui@qq.com
import zipfile


def unzip(zip_address, file_name, encoding='UTF-8', sep='\n'):
    """解压zip数据包

    :param zip_address: 压缩包的地址
    :param file_name: 压缩包里面文件的名字
    :param encoding: 文件的编码
    :param sep: 文件内容换行符
    :return: 压缩包里面的数据：默认编码的UTF-8
    """
    f = zipfile.ZipFile(zip_address)
    fp = f.read(file_name)
    lines = fp.decode(encoding)
    if '\r\n' in lines:
        return lines.split('\r\n')
    elif '\r' in lines:
        return lines.split('\r')
    elif '\n' in lines:
        return lines.split('\n')
    else:
        return lines.split(sep)


if __name__ == '__main__':
    line = unzip('D:\\date.zip', 'date.txt')
    for l in line:
        print(l)
