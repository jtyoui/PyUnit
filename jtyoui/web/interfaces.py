#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/13 16:23
# @Author: Jtyoui@qq.com
import json
import time
import requests


def interface_test(dict_, address, record_time=True):
    """简单接口测试
    :param dict_: 传入的参数
    :param address: url地址
    :param record_time: 是否记录消耗时间
    :return: 接口返回值
    """
    start = time.time()
    j = json.dumps(dict_, ensure_ascii='utf8')
    d = requests.post(address, j)
    page = json.loads(d.text)
    end = time.time()
    if record_time:
        return page, end - start
    return page
