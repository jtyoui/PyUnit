#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 10:36
# @Author: jtyoui@qq.com


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


class CoordinateLengthNotEqualError(Exception):
    """坐标维数不相等"""
    pass


class ParameterNotEmptyError(Exception):
    """参数不能为空"""
    pass


class MatrixNotDottedError(Exception):
    """矩阵不能点乘"""
    pass


class InconsistentLengthError(Exception):
    """长度不一致错误"""
    pass


class NameOfTrainStationNotFoundError(Exception):
    """未找到该火车站名字"""
    pass


class DownloadDataExceptionError(Exception):
    """下载数据异常"""
    pass
