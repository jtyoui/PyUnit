#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/12 9:59
# @Author: Jtyoui@qq.com
from jtyoui.error import NotFindPipError
import os
import time
import importlib


def pips(module, package=None):
    """安装模块：有时候加载模块和下载模块的名字不一样，需要指定package

    :param module: 加载模块的名字
    :param package: 没有模块下载模块的名字
    """
    package = package.lower() if package else module.lower()
    try:
        m = importlib.import_module(module)
    except ModuleNotFoundError:
        if os.system('pip3.7') in [1, 32512]:  # 1是window退出码，32512是Linux退出码
            if os.system('pip3') in [1, 32512]:
                if os.system('pip') in [1, 32512]:
                    raise NotFindPipError('你的电脑没有安装与pip相关的命令')
                else:
                    p = 'pip'
            else:
                p = 'pip3'
        else:
            p = 'pip3.7'
        os.system(F'{p} install --user {package}')
        time.sleep(2)
        m = importlib.import_module(module)
    return m


if __name__ == '__main__':
    pips('PyMysql')
