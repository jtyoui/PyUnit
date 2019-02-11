#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/10 0010
# @Email : jtyoui@qq.com
# @Software : PyCharm
import os
import requests
from fake_useragent import UserAgent
from urllib.request import urlretrieve
import io
from PIL import Image

GITEE = 'https://gitee.com/tyoui/{project}/raw/master/{package}/{name}'  # gitee上保存数据的格式


def fetch_gitee(package, name, project='logo', pil=True):
    """
    爬取非结构文本数据
    :param package: 包名
    :param name: 文件名
    :param project: 项目名
    :param pil: 是否返回PIL.Image类型
    :return: 返回字节数据
    """
    url = GITEE.format(project=project, package=package, name=name)
    response = requests.get(url=url, headers={'User-Agent': UserAgent().random})  # 动态增加UA
    content = response.content
    if pil:
        byte = io.BytesIO(content)  # 转成字节流
        return Image.open(fp=byte)
    return content


def download_gitee(package, name, address=None, project='logo'):
    """
    下载非结构文本数据
    :param package: 包名
    :param name: 文件名
    :param address: 保存文件的地址
    :param project: 项目名
    :return: 下载成功返回'success',失败返回'fail'
    """
    if not address:
        address = os.path.join(os.getcwd(), name)  # 默认保存地址是运行项目当前的位置
    url = GITEE.format(project=project, package=package, name=name)
    try:
        place = urlretrieve(url, address)  # 下载
        print('\033[1;33m' + place[0])
        return 'success'
    except:
        return 'fail'


if __name__ == '__main__':
    download_gitee('logo', 'logo.png', address='D:\\')  # 将照片logo.png下载到D盘
    pillow = fetch_gitee('logo', 'logo.png', pil=True)  # 返回PIL.image类型数据
