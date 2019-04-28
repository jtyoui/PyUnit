#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/10 0010
# @Email : jtyoui@qq.com
# @Software : PyCharm
from .gitee import fetch_gitee, download_gitee  # 爬取我自己Gitee上的数据
from .han_table import Han_J_F  # 导入繁体字和简体字的数据
from .constant import *  # 平时常见的常量
from .province import *  # 中国省市所有名字
from .Train import find_train_info, find_train_desc, find_train_desc_info, Train_Station  # 关于火车站的信息
