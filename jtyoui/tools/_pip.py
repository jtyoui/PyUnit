#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/12 9:59
# @Author: Jtyoui@qq.com
import os
import time


def pips(module):
    """安装模块"""
    module = module.lower()
    try:
        m = __import__(module)
    except ModuleNotFoundError:
        os.system('pip install --user ' + module)
        time.sleep(2)
        m = __import__(module)
    return m


if __name__ == '__main__':
    pips('PyMysql')
