#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/10 0010
# @Email : jtyoui@qq.com
# @Software : PyCharm
import os
import requests
from jtyoui.web import random
from urllib.request import urlretrieve

GITEE = 'https://gitee.com/tyoui/{project}/raw/master/{package}/{name}'  # gitee上保存数据的格式


def fetch_gitee(package, name, project='logo'):
    """爬取非结构文本数据

    :param package: 包名
    :param name: 文件名
    :param project: 项目名
    :return: 返回字节数据
    """
    url = GITEE.format(project=project, package=package, name=name)
    response = requests.get(url=url, headers={'User-Agent': random()})  # 动态增加UA
    content = response.content
    return content


def download_gitee(package, name, file_dir=None, project='logo'):
    """下载非结构文本数据

    :param package: 包名
    :param name: 文件名
    :param file_dir: 保存文件的文件夹地址
    :param project: 项目名
    :return: 下载成功返回'success',失败返回'fail'
    """
    if not file_dir:
        address = os.path.join(os.getcwd(), name)  # 默认保存地址是运行项目当前的位置
    elif os.path.isdir(file_dir):
        address = os.path.join(file_dir, name)
    elif not os.path.exists(file_dir):
        os.mkdir(file_dir)
        address = os.path.join(file_dir, name)
    else:
        address = file_dir
    url = GITEE.format(project=project, package=package, name=name)
    try:
        place = urlretrieve(url, address)  # 下载
        print('\033[1;33m' + place[0])
        return 'success'
    except Exception as e:
        print(e)
        return 'fail'


if __name__ == '__main__':
    status = download_gitee('logo', 'logo.png', file_dir='D://temp')  # 将照片logo.png下载到D盘
    print(status)
    pillow = fetch_gitee('logo', 'logo.png')  # 返回的是字节数据
    print(pillow)
    # byte = io.BytesIO(pillow)  # 转成字节流
    # Image.open(fp=byte)
