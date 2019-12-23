#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/9/29 15:39
# @Author: Jtyoui@qq.com
import warnings
import functools


def warns(message, category=None):
    """警告装饰器

    :param message: 警告信息
    :param category: 警告类型：默认是None
    :return: 装饰函数的对象
    """

    def _(func):
        @functools.wraps(func)
        def warp(*args, **kwargs):
            warnings.warn(message, category, stacklevel=2)
            return func(*args, **kwargs)

        return warp

    return _


# 废除警告
deprecationWarning = warns('该函数已废弃！', DeprecationWarning)

# 运行警告
runtimeWarning = warns('该函数运行期间可能存在问题！', RuntimeWarning)

if __name__ == '__main__':
    @runtimeWarning
    def w(): ...


    w()
