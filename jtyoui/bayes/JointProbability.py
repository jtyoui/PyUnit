#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/9 9:03
# @Author: Jtyoui@qq.com
from jtyoui.data.constant import MathSymbols

"""
联合概率:两件事情同时发生的概率
"""


def independent_joint(a, operation, b):
    """独立联合事件

    :param operation: and==∩，or==|,比如:independent_joint(a,'and',b)等价于P(a∩b)
    """
    if operation == 'and' or operation == MathSymbols.intersection:
        return a * b
    elif operation == 'or' and operation == MathSymbols.condition:
        return a


def non_independent_joint(a, operation, b):
    """非独立联合事件"""
    if operation == 'and' or operation == MathSymbols.intersection:
        return a * non_independent_joint(b, MathSymbols.condition, a)
