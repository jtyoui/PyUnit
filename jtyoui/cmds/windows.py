#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/5 17:41
# @Author: Jtyoui@qq.com
import os


def hide_file(file_path):
    """隐藏文件夹或者文件"""
    x = os.system(f'attrib +a +s +h +r {file_path}..')
    if x == 0:
        return True
    else:
        return False


def display_file(file_path):
    """显示文件夹或者文件"""
    x = os.system(f'attrib -a -s -h -r {file_path}..')
    if x == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(hide_file(r'D:/1/2.txt'))
    print(display_file(r'D:/1/2.txt'))
