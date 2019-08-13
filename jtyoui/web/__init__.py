#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/19
# @Email : jtyoui@qq.com
from .header import header, free_header  # 封装header
from .ua import random, ua, headers_ua  # 封装UA
from .HTML import ParseHtml  # 增加HTML解析
from .Request import get, post, get_js  # 增加爬虫网站
from .interfaces import *  # 增加后端调用接口测试
