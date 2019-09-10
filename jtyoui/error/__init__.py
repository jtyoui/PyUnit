#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 10:36
# @Author: jtyoui@qq.com


class BrowserTypeError(Exception):
    """浏览器异常.在web模块下的ua文件"""
    ...


class UAPageVersionError(Exception):
    """ua版本异常,重新指定版本即可"""
    ...


class BaiDuMapError(Exception):
    """百度地图接口异常"""
    ...


class LibraryNotInstallError(Exception):
    """第三方库没有安装"""
    ...


class CoordinateLengthNotEqualError(Exception):
    """坐标维数不相等"""
    ...


class ParameterNotEmptyError(Exception):
    """参数不能为空"""
    ...


class MatrixNotDottedError(Exception):
    """矩阵不能点乘"""
    ...


class InconsistentLengthError(Exception):
    """长度不一致错误"""
    ...


class NameOfTrainStationNotFoundError(Exception):
    """未找到该火车站名字"""
    ...


class DownloadDataExceptionError(Exception):
    """下载数据异常"""
    ...


class NotLegitimateNumberError(Exception):
    """不是一个合法的数字"""
    ...


class NotFindPipError(Exception):
    """没有找到pip命令"""
    ...


class NumberValueError(Exception):
    """number值错误"""
    ...


class IdCardCheckError(Exception):
    """身份证校验成功"""
    ...


class NotLinuxSystemError(Exception):
    """不是Linux系统异常"""
    ...


class MathValueWarning(Warning):
    """数值错误"""
    ...
