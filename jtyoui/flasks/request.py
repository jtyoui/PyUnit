#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/28 14:58
# @Author: Jtyoui@qq.com
import json


def content_type(requests):
    """根据不同的content_type来解析数据"""
    if requests.content_type == 'application/x-www-form-urlencoded':
        data = requests.form
    elif requests.content_type == 'application/json':
        data = json.loads(requests.data)
    else:  # 暂时
        data = json.loads(requests.data)
    return data
