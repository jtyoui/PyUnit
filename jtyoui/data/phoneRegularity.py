#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/9 9:56
# @Author: Jtyoui@qq.com
# 一组匹配中国大陆手机号码的正则表达式。
import re

# 匹配所有号码（手机卡 + 数据卡 + 上网卡）
ALL_Mobile_Data_Network_Card_RE = r'^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[01356789]\d{2}|4(?:0\d|1[0-2]|9\d))|9[189]\d{2}|6[567]\d{2}|4(?:[14]0\d{3}|[68]\d{4}|[579]\d{2}))\d{6}$'

# 匹配所有支持短信功能的号码（手机卡 + 上网卡）
ALL_Mobile_Network_Card_RE = r'^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[01356789]\d{2}|4(?:0\d|1[0-2]|9\d))|9[189]\d{2}|6[567]\d{2}|4[579]\d{2})\d{6}$'

# 手机卡
ALL_Mobile_Card_RE = r'^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[35678]\d{2}|4(?:0\d|1[0-2]|9\d))|9[189]\d{2}|66\d{2})\d{6}$'

# 移动手机卡
MOVE_Card_RE = r'^(?:\+?86)?1(?:3(?:4[^9\D]|[5-9]\d)|5[^3-6\D]\d|8[23478]\d|(?:78|98)\d)\d{7}$'

# 联通手机卡
UNICOM_Card_RE = r'^(?:\+?86)?1(?:3[0-2]|[578][56]|66)\d{8}$'

# 电信手机卡
TELECOM_Card_RE = r'^(?:\+?86)?1(?:3(?:3\d|49)\d|53\d{2}|8[019]\d{2}|7(?:[37]\d{2}|40[0-5])|9[19]\d{2})\d{6}$'

# 匹配北京船舶通信导航有限公司（海事卫星通信）
Maritime_Communications_RE = r'^(?:\+?86)?1749\d{7}$'

# 工业和信息化部应急通信保障中心（应急通信）
Emergency_Communication_RE = r'^(?:\+?86)?174(?:0[6-9]|1[0-2])\d{6}$'

# 虚拟运营商
ALL_Virtual_Operator_RE = r'^(?:\+?86)?1(?:7[01]|6[57])\d{8}$'

# 移动虚拟运营商
Move_Virtual_Operator_RE = r'^(?:\+?86)?1(?:65\d|70[356])\d{7}$'

# 联通虚拟运营商
UNICOM_Virtual_Operator_RE = r'^(?:\+?86)?1(?:70[4789]|71\d|67\d)\d{7}$'

# 电信虚拟运营商
TELECOM_Virtual_Operator_RE = r'^(?:\+?86)?170[0-2]\d{7}$'

# 物联网数据卡
ALL_Internet_of_Things_Data_Card_RE = r'^(?:\+?86)?14(?:[14]0|[68]\d)\d{9}$'

# 移动物联网数据卡
Move_Internet_of_Things_Data_Card_RE = r'^(?:\+?86)?14(?:40|8\d)\d{9}$'

# 联通物联网数据卡
UNICOM_Internet_of_Things_Data_Card_RE = r'^(?:\+?86)?146\d{10}$'

# 电信物联网数据卡
TELECOM_Internet_of_Things_Data_Card_RE = r'^(?:\+?86)?1410\d{9}$'

# 上网卡
ALL_Wireless_Network_Card_RE = r'^(?:\+?86)?14[579]\d{8}$'

# 移动上网卡
MOVE_Wireless_Network_Card_RE = r'^(?:\+?86)?147\d{8}$'

# 联通上网卡
UNiCOM_Wireless_Network_Card_RE = r'^(?:\+?86)?145\d{8}$'

# 电信上网卡
TELECOM_Wireless_Network_Card_RE = r'^(?:\+?86)?149\d{8}$'


def telephone_number_matching_verification(re_, str_: str):
    """电话号码匹配

    默认匹配到的电话号码包括：
    —— 移动、联通、电信手机卡
    —— 海事卫星通信
    —— 应急通信
    —— 移动、联通、电信虚拟运营商
    —— 移动、联通、电信物联网数据卡
    —— 移动、联通、电信上网卡

    具体使用默认正则：请看： https://github.com/jtyoui/Jtyoui/blob/master/jtyoui/data/phoneRegularity.py

    :param re_: 电话号码匹配的正则
    :param str_: 一串数字
    :return: 匹配到的电话号码
    """
    numbers, number = [], ''
    for char_ in str_:
        if char_.isdigit():
            number += char_
        elif number:
            numbers.append(number)
            number = ''
    if number:
        numbers.append(number)
        del number
    if numbers:
        for num in numbers:
            if re.search(re_, num):
                yield num


if __name__ == '__main__':
    s = '我的电话是15180864679，你的电话是13314415519'
    for i in telephone_number_matching_verification(ALL_Mobile_Data_Network_Card_RE, s):
        print(i)
