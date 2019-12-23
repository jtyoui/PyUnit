#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/9 13:53
# @Author: Jtyoui@qq.com
# -*- coding: utf-8 -*-
from jtyoui.error import IdCardCheckError
import re


def check_id_card(id_card: str):
    """身份证号码识别

    :param id_card: 一串号码
    :return: 识别出身份证号码
    """
    errors = ['验证通过!', '身份证号码位数不对!', '身份证号码出生日期超出范围或含有非法字符!', '身份证号码校验错误!', '身份证地区非法!']
    area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁", "22": "吉林", "23": "黑龙江",
            "31": "上海", "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东", "41": "河南", "42": "湖北",
            "43": "湖南", "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州", "53": "云南", "54": "西藏",
            "61": "陕西", "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆", "71": "台湾", "81": "香港", "82": "澳门", "91": "国外"}
    length = len(id_card)
    key = id_card[0: 2]  # 地区中的键是否存在
    assert area.get(key, False), errors[4]
    leap_year = int(id_card[6:10]) % 4 == 0 or (int(id_card[6:10]) % 100 == 0 and int(id_card[6:10]) % 4 == 0)  # 闰年
    # 15位身份号码检测
    if length == 15:
        if leap_year:
            erg = re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)'
                             '(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')
        else:
            erg = re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)'
                             '(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')
        if re.match(erg, id_card):
            return errors[0]
        else:
            raise IdCardCheckError(errors[2])
    # 18位身份号码检测
    elif length == 18:
        if leap_year:
            # 闰年出生日期的合法性正则表达式
            erg = re.compile('[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|'
                             '(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')
        else:
            # 平年出生日期的合法性正则表达式
            erg = re.compile('[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|'
                             '(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')

        if re.match(erg, id_card):
            m = id_card_calibration(id_card)
            if m == id_card[17].upper():  # 校验身份证最后一位，如果是x那么转为大写的X
                return errors[0]
            else:
                raise IdCardCheckError(errors[3])
        else:
            raise IdCardCheckError(errors[2])
    else:
        raise IdCardCheckError(errors[1])


def id_card_calibration(id_card: str):
    """身份证号码检验

    校对身份证最后一位数字

    :param id_card: 一串号码
    :return: 检验值
    """
    id_card_list = list(id_card)
    # 计算校验位
    s = (int(id_card_list[0]) + int(id_card_list[10])) * 7 + (
            int(id_card_list[1]) + int(id_card_list[11])) * 9 + (
                int(id_card_list[2]) + int(id_card_list[12])) * 10 + (
                int(id_card_list[3]) + int(id_card_list[13])) * 5 + (
                int(id_card_list[4]) + int(id_card_list[14])) * 8 + (
                int(id_card_list[5]) + int(id_card_list[15])) * 4 + (
                int(id_card_list[6]) + int(id_card_list[16])) * 2 + (
                int(id_card_list[7]) * 1 + int(id_card_list[8]) * 6 +
                int(id_card_list[9]) * 3
        )
    m = "10X98765432"[s % 11]  # 判断校验位
    return m


if __name__ == "__main__":
    print(check_id_card('522121199505302563'))
