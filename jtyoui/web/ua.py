#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 9:15
# @Author: Jtyoui
import requests
from random import choice
from jtyoui.error import BrowserTypeError, UAPageVersionError

browsers = None


def ua(browser='chrome', version='0.1.11'):
    """
    随机返回browser浏览器一条UA
    :param browser: 浏览器名字,包括如下:[chrome,opera,firefox,internetexplorer,safari]
    :param version: 爬取ua网页版本
    :return: 字典类型
    """
    global browsers
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
    cache = 'https://fake-useragent.herokuapp.com/browsers/' + version
    response = requests.get(cache)
    if response.status_code != 200:
        if version != '0.1.3':
            return ua(browser, '0.1.3')
        else:
            raise UAPageVersionError('版本问题,重新指定版本')
    json = response.json()
    browsers = json['browsers'][browser]
    return choice(browsers)


random = ua

if __name__ == '__main__':
    print(random())
