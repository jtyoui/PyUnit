#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/12 9:59
# @Author: Jtyoui@qq.com
import os
import time


def pips(module, package=None):
    """安装模块：有时候加载模块和下载模块的名字不一样，需要指定package
    :param module: 加载模块的名字
    :param package: 没有模块下载模块的名字
    """
    module = module.lower()
    package = package.lower() if package else module
    try:
        m = __import__(module)
    except ModuleNotFoundError:
        os.system(F'pip install --user {package}')
        time.sleep(2)
        m = __import__(module)
    return m


if __name__ == '__main__':
    pips('PyMysql')
