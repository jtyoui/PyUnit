#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/29 15:08
# @Author: Jtyoui@qq.com
from enum import Enum


class Languages(Enum):
    English = '英语'
    Japanese = '日语'
    Korean = '韩语'
    French = '法语'
    German = '德语'
    Spanish = '西班牙语'
    Chinese = '汉语'


if __name__ == '__main__':
    print(type(Languages.English))
    print(Languages.English)
