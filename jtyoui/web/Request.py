#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/11 16:06
# @Author: Jtyoui@qq.com
from jtyoui.web import headers_ua
from jtyoui.error import LibraryNotInstallError
import requests

"""爬虫网站。请求Get和Post封装"""


def get(url, cookie=None):
    """Get网站"""
    if cookie:
        headers_ua['cookie'] = cookie
    response = requests.get(url=url, headers=headers_ua)
    return response


def post(url, params, cookie=None):
    """Post网站"""
    if cookie:
        headers_ua['cookie'] = cookie
    response = requests.post(url=url, data=params, headers=headers_ua)
    return response


def get_js(js, js_fun, js_params):
    try:
        import execjs  # pip install PyExecJS
    except:
        raise LibraryNotInstallError('安装：pip install PyExecJS')
    ctx = execjs.compile(js)  # 加载JS文件
    return ctx.call(js_fun, *js_params)  # 调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数


if __name__ == '__main__':
    print(get('http://www.27k.cc/'))
