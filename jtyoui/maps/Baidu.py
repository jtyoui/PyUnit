#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 9:06
# @Author: Jtyoui
from jtyoui.web import random


def get_data(loc, page_num=0):
    pa = {
        'query': '公园',
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': page_num,
        'ak': 'rINxBQe6h4OGbmrLiImffAj96ZlhxCY8'
    }
