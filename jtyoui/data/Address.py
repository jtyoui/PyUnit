#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 23:26
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from jtyoui.error import DownLoadDataError
from jtyoui.decorators import deprecationWarning
from jtyoui.algorithm import dict_create_tree
from platform import platform
import time
import os
import bz2
import json
import re

re_id_card = """
(?P<province>[^省]+省|.+自治区)
(?P<city>[^自治州]+自治州|[^市]+市|[^盟]+盟|[^地区]+地区|.+区划)
(?P<county>[^市]+市|[^县]+县|[^旗]+旗|[^区]+区)?
(?P<town>[^区]+区|[^镇]+镇)?
(?P<village>.*)
""".replace('\n', '')

_Address = {}
_TREE = None


def _download_address_file(file_address_path):
    """下载地址数据包

    :param file_address_path: 保存地址文件的路径
    """
    from urllib.request import urlretrieve
    url = 'https://dev.tencent.com/u/zhangwei0530/p/logo/git/raw/master/rear.bz2'
    place = urlretrieve(url, file_address_path)  # 下载
    print('---------验证数据-------')
    time.sleep(2)
    if not os.path.exists(file_address_path):
        print('下载失败')
        return False
    elif os.stat(file_address_path).st_size != 2292518:
        print('下载失败、移除无效文件！')
        os.remove(file_address_path)
        return False
    else:
        print('\033[1;33m' + place[0])
    return True


def load_address_file(file_address_path):
    """加载地址文件数据

    :param file_address_path: 加载地址文件的路径，没有地址文件默认自动下载。
    :return: 地址文件数据，类型字典
    """
    file_address_path = os.path.abspath(file_address_path) + os.sep + 'address'
    if not os.path.exists(file_address_path):
        if not _download_address_file(file_address_path):
            raise DownLoadDataError('检查网络设置，下载地址文件数据异常！')
    bz = bz2.BZ2File(file_address_path)
    text = bz.read().decode('utf-8')
    data = text[512:-1134]
    address = json.loads(data, encoding='utf8')
    return address


@deprecationWarning
def find_address(name):
    """查询地址

    该函数也废除，建议使用：finds_address函数
    输入一个地名，查到这个名字的详细地址：比如输入：大连市、朝阳区、遵义县、卡比村等

    :param name: 输入一个地址。
    :return: 地址的信息
    """
    assert True if name else False, '输入的字符串不能为空'
    global _Address
    if not _Address:
        if 'Windows' in platform():
            path = r'D://'
        else:
            path = r'./'
        _Address = load_address_file(path)
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


def find_identity_card_address(card_addr):
    """识别身份证地址

    输入一个地址，判断是否是身份证上的地址，返回格式包括：
    一级地址：省|自治区
    二级地址：自治州|市|盟|地区|区划
    三级地址：市|县|旗|区
    四级地址：区|镇
    五级地址：其他


    :param card_addr: 一串地址
    :return: 返回元组，包括五级地址
    """
    names = re.match(re_id_card, card_addr)
    province = names.group('province')
    city = names.group('city')
    county = names.group('county')
    town = names.group('town')
    village = names.group('village')
    return province, city, county, town, village


def finds_address(data, name: str):
    """查询地址

    输入一个地名，查到这个名字的详细地址：比如输入：大连市、朝阳区、遵义县、卡比村等

    :param data: 地址数据
    :param name: 输入一个地址名
    :return: 地址的信息
    """
    global _TREE
    if not _TREE:
        _TREE = dict_create_tree(data)
    return _TREE.search_tree_value(name)


if __name__ == '__main__':
    import pprint

    pprint.pprint(find_address('晋安'))  # 已废弃，建议用：finds_address
    print(find_identity_card_address('贵州省贵阳市南明区花果园延安南路28号'))

    print('---------------------搜索树查找，第一次比较慢------------------------------------------')
    for t in finds_address(load_address_file('D://'), '晋安'):
        print(t)

    for t in finds_address(load_address_file(r'D://'), '遵义县'):
        print(t)
