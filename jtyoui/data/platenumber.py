#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/8 10:10
# @Author: Jtyoui@qq.com
import re

# 普通车牌
ORDINARY_CAR_RE = "[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z][A-Z][A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9挂学警港澳]"
# 新能源车牌
NEW_ENERGY_VEHICLE_RE = "[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z][A-Z](?:(?:[0-9]{5}[DF])|(?:[DF][A-HJ-NP-Z0-9][0-9]{4}))"
# 所有的车牌
ALL_CAR_RE = ORDINARY_CAR_RE + "|" + NEW_ENERGY_VEHICLE_RE


def plate_number(number: str, car_re: str = ALL_CAR_RE) -> list:
    """车牌号验证

    默认校验车牌号号码包括：\n
    —— 普通车牌\n
    —— 新能源车牌\n

    具体的引用正则包括：\n
    —— 普通车牌 jtyoui.ORDINARY_CAR_RE\n
    —— 新能源车牌 jtyoui.NEW_ENERGY_VEHICLE_RE\n
    —— 所有的车牌 jtyoui.ALL_CAR_RE\n

    :param car_re: 匹配车牌号的正则，默认是：CAR_RE
    :param number: 车牌号
    :return: 车牌号
    """
    return re.findall(car_re, number, flags=re.I)


if __name__ == '__main__':
    print(plate_number('我家车牌号是：au134567'))
