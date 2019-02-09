#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm

from jtyoui.bs import binary_system  # 任意进制转换
from jtyoui.code import cr  # 二维码识别
import jtyoui.imagepdf  # 照片和PDF互转
from jtyoui.plunar import Lunar  # 农历
from jtyoui.sogou import SoGou  # 下载搜狗
from jtyoui.word import analysis  # 新词发现
import jtyoui.wx.AutoChat  # 启动微信聊天机器人

__all__ = [a for a in dir() if not a.startswith('_')]
