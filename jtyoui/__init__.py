#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm

from jtyoui.bs import binary_system  # 任意进制转换
from jtyoui.code import cr  # 二维码识别
from jtyoui.imagepdf import *  # 照片和PDF互转
from jtyoui.plunar import Lunar  # 农历
from jtyoui.sogou import SoGou  # 下载搜狗
from jtyoui.word import analysis  # 新词发现
from jtyoui.wx import *  # 启动微信聊天机器人
from jtyoui.mail import *  # 邮箱
from jtyoui.data import *  # 常量
from jtyoui.fractal import *  # 分形
from jtyoui.web import *  # 网页
from jtyoui.language import *  # 语言
from jtyoui.regular import *  # 正则
from jtyoui.decorator import *  # 装饰器
from jtyoui.error import *  # 异常
from jtyoui.maps import *  # 地图
from jtyoui.similarity import *  # 文本相似度算法

__all__ = [a for a in dir() if not a.startswith('_')]
__all__.append('game')
__version__ = '19.3.14'
__author__ = 'Jtyoui'
