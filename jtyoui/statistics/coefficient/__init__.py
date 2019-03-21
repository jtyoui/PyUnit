#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/21 14:56
# @Author: Jtyoui@qq.com

"""
相关关系
相关关系是一种非确定性的关系，相关系数是研究变量之间线性相关程度的量。
"""

from .Pearson import pearson_coefficient  # 皮尔森相关性系数
from .Spearman import spear_man_coefficient  # 斯皮尔曼相关系数
from .Kendall import kendall_coefficient  # 肯德尔相关性系数
