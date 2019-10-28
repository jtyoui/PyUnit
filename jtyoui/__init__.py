#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm

from jtyoui.bs import binary_system  # 任意进制转换
from jtyoui.code import cr  # 二维码识别
from jtyoui.plunar import *  # 农历、阳历
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
from jtyoui.c import *  # 增加c代码引用
from jtyoui.baidu import *  # 增加关于百度的资料及应用
from jtyoui.jp import *  # 提取日语意思
from jtyoui.compress import *  # 压缩包文件
from jtyoui.algorithm import *  # 常见算法
from jtyoui.cmd import *  # CMD命令
from jtyoui.interface import *  # 界面
from jtyoui.reflex import *  # 反射
from jtyoui.logger import *  # 增加日志文件夹
from jtyoui.project import *  # 项目接口
from jtyoui.person import *  # 中国人属性

__all__ = [a for a in dir() if not a.startswith('_')]
__all__.extend(['game', 'imagepdf', 'wx', 'neuralNetwork'])  # 游戏 pdf和照片互转 微信抓电影和聊天机器人
__version__ = '19.10.28'
__author__ = 'Jtyoui'
__description__ = f'这是一个Python集合包,包含了:{len(__all__)}个模块。'
