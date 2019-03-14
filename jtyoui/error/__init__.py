#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 10:36
# @Author: Jtyoui


class BrowserTypeError(Exception):
    """浏览器异常.在web模块下的ua文件"""
    pass


class UAPageVersionError(Exception):
    """ua版本异常,重新指定版本即可"""
    pass


class BaiDuMapError(Exception):
    """百度地图接口异常"""
    pass


class LibraryNotInstallError(Exception):
    """第三方库没有安装"""
    pass
