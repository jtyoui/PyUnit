#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/13 16:23
# @Author: Jtyoui@qq.com
import json
import time
import requests


def interface_test(dict_, address, record_time=True, **kwargs):
    """简单接口测试

    :param dict_: 传入的参数
    :param address: url地址
    :param kwargs: 参考requests.post **kwargs
    :param record_time: 是否记录消耗时间
    :return: 接口返回值
    """
    start = time.time()
    j = json.dumps(dict_, ensure_ascii='utf8')
    response = requests.post(address, j, **kwargs)
    page = json.loads(response.text)
    end = time.time()
    if record_time:
        return page, end - start
    return page


def interface_tests(method, url, data, record_time=True, **kwargs):
    """简单接口测试

    :param method: 请求方法，比如：post、get
    :param url: url地址
    :param data: 传入的参数
    :param record_time: 是否记录消耗时间
    :param kwargs: 参考requests.post **kwargs
    :return: 接口返回值
    """
    start = time.time()
    response = requests.request(method=method.upper(), url=url, data=data, **kwargs)
    end = time.time()
    if record_time:
        return response.text, end - start
    return response.text


interface_post_test = interface_test  # post接口测试
interface_all_tests = interface_tests  # 接口测试

if __name__ == '__main__':
    d = {'answer': '我要告南明区政府贪污。', 'event_id': 'df99f4bb7f94c69c1b37ece4b41f1d05'}
    ji = interface_test(d, 'http://222.85.147.140:10056/commit_org')
    print(ji)
