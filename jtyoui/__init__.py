#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm

from .bs import binary_system  # 任意进制转换
from .code import cr  # 二维码识别
from .imagepdf import *  # 照片和PDF互转
from .plunar import Lunar  # 农历
from .sogou import SoGou  # 下载搜狗
from .word import analysis  # 新词发现
from .wx import *  # 启动微信聊天机器人
from .mail import *  # 邮箱
from .data import *  # 常量
from .fractal import *  # 分形
from .web import *  # 网页
from .language import *  # 语言
from .regular import *  # 正则
from .decorator import *  # 装饰器

__all__ = [a for a in dir() if not a.startswith('_')]
