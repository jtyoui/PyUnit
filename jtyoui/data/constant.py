#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/19
# @Email : jtyoui@qq.com

from enum import Enum, unique

# 常见的照片格式
Photo_Format = (
    'bmp', 'jpg', 'png', 'tif', 'gif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd', 'cdr', 'pcd', 'dxf', 'ufo', 'eps',
    'ai', 'raw', 'WMF', 'webp'
)

# 常见的文字编码格式
Decode = ('Unicode', 'ASCII', 'GBK', 'GB2312', 'UTF-8', 'ISO-8859-1', 'UTF-16', 'GB18030', 'ISO-8859-2')


@unique
class MathSymbols(Enum):
    """‖‰℃℉←↑→↓∈∏∑°√∝∞∟∠∣∧∨∩∪∫∮～≈≌≒≠≡"""
    vector_value = '‖'  # ‖A‖ 表示A向量的值
    one_thousand = '‰'  # 千分号
    celsius_scale = '℃'  # 摄氏温标的温度计量单位
    fahrenheit_scale = '℉'  # 华氏温标
    right = '→'  # 向右
    left = '←'  # 向左
    up = '↑'  # 向上
    down = '↓'  # 向下
    belong_to = '∈'  # 属于
    product = '∏'  # 求乘积
    summation = '∑'  # 求累加
    one_degrees = '°'  # 1度,度角单位
    check_mark = '√'  # 对钩
    positive_proportion = '∝'
    infinity = '∞'
    slope = '∠'
    intersection = '∩'  # 交集
    and_ = '∧'  # 逻辑和
    condition = '∣'  # 条件概率P(A∣B)
    union = '∪'  # 并集
    integral = '∫'  # 积分
    or_ = '∨'  # 逻辑或
    closed_curve = '∮'  # 闭合曲线
    asymptotically_equal = '～'  # 逐渐相等,f(x)～g(x),表示lim f(x)=lim g(x)
    approximately_equal = '≈'  # 约等于
    identically_equal = '≌'  # 全等
    reversible = '≒'  # 可逆
    not_equal = '≠'  # 不等于
    identity = '≡'  # 恒等于
