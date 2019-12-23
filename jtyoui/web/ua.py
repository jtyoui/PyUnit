#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 9:15
# @Author: Jtyoui
import requests
from random import choice
from jtyoui.error import BrowserTypeError, UAPageVersionError
import pickle
import os

browsers = None


def ua(browser='chrome', version='0.1.11', update=False):
    """随机返回browser浏览器一条UA

    :param browser: 浏览器名字,包括如下:[chrome,opera,firefox,internetexplorer,safari]
    :param version: 爬取ua网页版本
    :param update: 是否更新保存的UA文件数据
    :return: 字典类型
    """
    global browsers
    save_path = r'C:\browser.json' if os.name == 'nt' else '/etc/browser.json'
    other_save_path = r'D:\browser.json' if os.name == 'nt' else '/home/browser.json'
    browser_type = ['chrome', 'opera', 'firefox', 'internetexplorer', 'safari']
    b = {
        'c': 'chrome',
        'o': 'opera',
        'ff': 'firefox',
        'ie': 'internetexplorer',
        's': 'safari'
    }
    browser = b.get(browser, browser)
    if browser not in browser_type:
        raise BrowserTypeError('浏览器类型异常,类型支持:[chrome,opera,firefox,internetexplorer,safari]')
    if browsers:
        return choice(browsers)
    if (not update) and os.path.exists(save_path):
        with open(save_path, 'rb')as fp:
            json = pickle.load(fp)
    elif (not update) and os.path.exists(other_save_path):
        with open(other_save_path, 'rb')as fp:
            json = pickle.load(fp)
    else:
        print(f'第一次在线加载，加载保存的文件在：{save_path}，以后都是离线加载，想改变请修改参数:update==True')
        cache = 'https://fake-useragent.herokuapp.com/browsers/' + version
        response = requests.get(cache)
        if response.status_code != 200:
            if version != '0.1.3':
                return ua(browser, '0.1.3')
            else:
                raise UAPageVersionError('版本问题,重新指定版本')
        json = response.json()
        try:
            with open(save_path, 'wb')as fp:
                pickle.dump(json, fp)
        except PermissionError:
            with open(other_save_path, 'wb')as fp:
                pickle.dump(json, fp)
    browsers = json['browsers'][browser]
    return choice(browsers)


random = ua


def headers_ua():
    return {'user-agent': random()}


if __name__ == '__main__':
    print(random())
    print(headers_ua())
    print(ua(update=True))  # 更新文件
