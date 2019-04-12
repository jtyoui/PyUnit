#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm

from jtyoui.bs import binary_system  # 任意进制转换
from jtyoui.code import cr  # 二维码识别
from jtyoui.plunar import Lunar  # 农历
from jtyoui.sogou import SoGou  # 下载搜狗
from jtyoui.word import *  # 新词发现
from jtyoui.mail import *  # 邮箱
from jtyoui.data import *  # 常量
from jtyoui.fractal import *  # 分形
from jtyoui.web import *  # 网页
from jtyoui.language import *  # 语言
from jtyoui.regular import *  # 正则
from jtyoui.decorator import *  # 装饰器
from jtyoui.error import *  # 异常
from jtyoui.maps import *  # 地图
from jtyoui.statistics import *  # 文本统计方法
from jtyoui.bayes import *  # 贝叶斯算法
from jtyoui.tools import *  # 常见的工具类函数

__all__ = [a for a in dir() if not a.startswith('_')]
__all__.extend(['game', 'imagepdf', 'wx'])  # 游戏 pdf和照片互转 微信抓电影和聊天机器人
__version__ = '19.4.12'
__author__ = 'Jtyoui'
