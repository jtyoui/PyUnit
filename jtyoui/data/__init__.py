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
from .Enums import *  # 增加枚举
from .Address import *  # 查询地址
from .TimeZone import TZ  # 时区
from .WeatherAddress import WeatherForecast  # 天气预报
from .methods import *  # 一些常见的方法
from .wordNature import *  # 词性
from .fileFormat import FileFormat  # 文件格式
from .genericity import fun_generic  # 重载
from .phoneRegularity import *  # 电话号码匹配
from .CardId import *  # 增加身份证校验功能
from .platenumber import *  # 增加车牌号验证
from .tencent import download_dev_tencent  # 下载远程数据
