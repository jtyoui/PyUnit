#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/12/26 9:44
# @Author: Jtyoui@qq.com
from urllib.request import urlretrieve
import jtyoui
import os


def download_dev_tencent(file_path: str, username: str, package: str, save_path: str, md5: str):
    """下载数据

    下载数据在coding平台上

    >>> download_dev_tencent('date.zip', 'zhangwei0530', 'logo', 'D://', '79A5A43F33CA300CD2671DF1168B24E5')

    :param file_path: 文件路径
    :param username: 账号
    :param package: 项目
    :param save_path: 保存文件在该文件夹
    :param md5: MD5校验值
    :return: 下载成功返回保存的地址
    """
    name = os.path.basename(file_path)
    url = f'https://dev.tencent.com/u/{username}/p/{package}/git/raw/master/{file_path}'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    if os.path.isdir(save_path):
        save_path = os.path.join(save_path, name)
    urlretrieve(url, save_path)
    print('---------验证数据-------')
    if not os.path.exists(save_path):
        raise jtyoui.DownloadDataExceptionError('下载失败！请检查网络。')
    elif jtyoui.get_file_md5(save_path) != md5:
        print('下载失败、移除无效文件！')
        os.remove(save_path)
        return False
    else:
        print('\033[1;33m' + save_path)
    return save_path


if __name__ == '__main__':
    download_dev_tencent('date.zip', 'zhangwei0530', 'logo', 'D://', '79A5A43F33CA300CD2671DF1168B24E5')
