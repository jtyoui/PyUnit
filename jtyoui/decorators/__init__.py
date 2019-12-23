#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/11 11:43
# @Author: Jtyoui@qq.com
from jtyoui.decorators.warn import *
import re
from jtyoui.error import CoordinateLengthNotEqualError, ParameterNotEmptyError

"""
装饰器模式
"""


@warns('也废除，请使用functools.wraps函数来替代', DeprecationWarning)
def warps(func):
    """这个装饰器等效：functools.wraps(fun)"""

    def call(*args, **kwargs):
        return func(*args, **kwargs)

    call.__doc__ = func.__doc__
    call.__name__ = func.__name__
    call.__dict__.update(func.__dict__)
    return call


def replace_regular(re_, replace_):
    """根据正则来修改参数

    :param re_: 匹配的正则
    :param replace_: 替换正则的数据
    :return: 被替换完毕的参数
    """
    r = re.compile(re_)

    def remove_replace(fun):

        @functools.wraps(fun)
        def wraps(*args, **kwargs):
            args_, kwargs_ = list(args), {}
            for i in range(len(args)):
                if isinstance(args[i], str):
                    args_[i] = r.sub(replace_, args[i])
                else:
                    args_[i] = args[i]
            for k, v in kwargs.items():
                if isinstance(v, str):
                    kwargs_.setdefault(k, r.sub(replace_, v))
                else:
                    kwargs_.setdefault(k, v)

            return fun(*args_, **kwargs_)

        return wraps

    return remove_replace


def parameter_set_length(fun):
    """参数集合长度验证修饰器"""

    @functools.wraps(fun)
    def wraps(x, y):
        if not (x and y):
            raise ParameterNotEmptyError("参数不能为空")
        if len(x) != len(y):
            raise CoordinateLengthNotEqualError("两个参数长度不一致")
        return fun(x, y)

    return wraps


def singleton(cls, *args, **kwargs):
    """单列模式修饰器"""
    instances = {}

    @functools.wraps(cls, *args, **kwargs)
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


def coroutine(func):
    """自动激活协程装饰器"""

    @functools.wraps(func)
    def warp(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return warp


if __name__ == '__main__':
    from jtyoui.regular import Non_Chinese


    @replace_regular(' ', '')
    def remove_blank(a, b):
        print(a, b)


    @replace_regular(Non_Chinese, '')
    def remove_non_chinese(a, b):
        print(a, b)


    remove_blank('你好  吗?', b='我  很好!')
    remove_non_chinese('你好#$%76#%吗wore?', b='我$%787word很好!')


    @singleton
    class A:
        pass


    a = A()
    b = A()
    print(id(a) == id(b))  # True


    @coroutine
    def receiver():
        n = 0
        while True:
            n = yield n + n


    print(receiver().send(10))
