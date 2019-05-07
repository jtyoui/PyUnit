#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 23:26
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from platform import platform
import os
import bz2
import json

_Address = {}


def _load(file_address):  # 下载地址的压缩包
    from urllib.request import urlretrieve
    url = 'https://dev.tencent.com/u/zhangwei0530/p/logo/git/raw/master/rear.bz2'
    place = urlretrieve(url, file_address)  # 下载
    print('\033[1;33m' + place[0])


def find_address(name):
    """查询地址。输入一个地名，查到这个名字的详细地址：比如输入：大连市、朝阳区、遵义县、卡比村等
    :param name: 输入一个地址。
    :return: 地址的信息
    """
    assert True if name else False, '输入的字符串不能为空'
    global _Address
    if not _Address:
        if 'Windows' in platform():
            path = r'D:/jtyoui_address'
        else:
            path = r'./jtyoui_address'
        if not os.path.exists(path):
            _load(path)
        bz = bz2.BZ2File(path)
        text = bz.read().decode('utf-8')
        data = text[512:-1134]
        _Address = json.loads(data, encoding='utf8')
    address = []
    for province in _Address:
        city_s = _Address[province]
        for city in city_s:
            districts = city_s[city]
            for district in districts:
                towns = districts[district]
                for town in towns:
                    villages = towns[town]
                    for village in villages:
                        if name in village:
                            addr = province + ' ' + city + ' ' + district + ' ' + town + ' ' + village
                            address.append(addr)
                    if name in town:
                        addr = province + ' ' + city + ' ' + district + ' ' + town
                        address.append(addr)
                if name in district:
                    addr = province + ' ' + city + ' ' + district
                    address.append(addr)
            if name in city:
                addr = province + ' ' + city
                address.append(addr)
        if name in province:
            addr = province
            address.append(addr)
    return address


if __name__ == '__main__':
    import pprint

    pprint.pprint(find_address('晋安'))
