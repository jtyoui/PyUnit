#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/7 13:20
# @Author: Jtyoui@qq.com

import functools


@functools.singledispatch
def fun_generic(*args, **kwargs):
    """自定义泛型类型"""
    pass


if __name__ == '__main__':
    @fun_generic.register(str)  # 定义类型
    def _(*arg, **kwargs):
        print("str:", arg, kwargs)


    fun_generic('hello', 'world', key=1)
