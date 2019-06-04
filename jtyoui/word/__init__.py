#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/26 9:47
# @Author: Jtyoui@qq.com

from .neologism import Neologism  # 没有多线程
from .ThreadNeologism import thread_analysis  # 有多线程
from .NAA import NAA  # 自动过滤的算法
