#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 18:35
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from jtyoui.baidu import BaiDuInfoSearch
from jtyoui.error import NameOfTrainStationNotFoundError
from jtyoui.file_zip import load_zip
from jtyoui.baidu import Load_BaiDuBaiKe

_lines = load_zip('train.zip', 'train.txt')

_train, _province = [], []
_flag = False
for _line in _lines:
    if '----' not in _line:
        if _flag:
            _province.append(_line)
        else:
            _train.append(_line)
    else:
        _flag = True

Train_Station = dict(zip(_train, _province))


def _find_train_station_(name):
    if not ('火车站' in name or '站' in name):
        if Train_Station.get(name):
            name += '站'
        else:
            raise NameOfTrainStationNotFoundError(F"没有找到{name}火车站信息，请正确输入！")
    text = Load_BaiDuBaiKe(name)
    if '站' in text:
        return text
    return ''


def find_train_info(name):
    """查询火车站的基本信息"""
    data = _find_train_station_(name)
    bd = BaiDuInfoSearch(data)
    return bd.info()


def find_train_desc(name):
    """查询火车站的摘要信息"""
    data = _find_train_station_(name)
    bd = BaiDuInfoSearch(data)
    return bd.desc()


def find_train_desc_info(name):
    """查询火车站的摘要和基本信息"""
    data = _find_train_station_(name)
    bd = BaiDuInfoSearch(data)
    return bd.desc(), bd.info()


if __name__ == '__main__':
    print(Train_Station['安顺'])  # 查看安顺火车站是哪个省
    desc = find_train_desc('安顺火车站')  # 查看安顺火车站的摘要
    print(desc)
    info = find_train_info('安顺站')  # 查询安顺火车站的基本信息
    print(info)
    di = desc_info = find_train_desc_info('宋')
    print(di)
