#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/16 17:45
# @Author: Jtyoui@qq.com
from types import FunctionType, ModuleType


def string_function(module: [str, ModuleType], func: str, *args, **kwargs):
    """根据字符串方法名来进行调用模块方法

    :param module: 模块名
    :param func: 模块中的方法名字
    :param args: 方法里面的参数值
    :param kwargs: 方法里面的参数值
    :return: 返回一个返回值
    """
    if isinstance(module, ModuleType):
        if hasattr(module, func):
            func_or_var = getattr(module, func)
            if isinstance(func_or_var, FunctionType):
                return func_or_var(*args, **kwargs)
            else:
                return func_or_var
        else:
            print(f'{func}不是一个方法')
    elif isinstance(module, str):
        m = __import__(module)
        return string_function(m, func, *args, **kwargs)
    else:
        print(f'{module}不是一个模块')
    return None


if __name__ == '__main__':
    print(string_function('jtyoui', 'BaiDuInfoSearch')('万绮雯').info())
    print(list(string_function('jtyoui', 'f_to_j', str_='載')))
    print(list(string_function('jtyoui', 'f_to_j', '載')))
