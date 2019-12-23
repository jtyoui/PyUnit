#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 21:56
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from html.parser import HTMLParser
from urllib.parse import quote
import requests
from jtyoui.web import headers_ua
import re


class _InfoSearch(HTMLParser):
    """基类"""

    def __init__(self):
        HTMLParser.__init__(self)
        self._data_flag = ''
        self.desc = ''
        self._desc_flag = False
        self.info_name = []
        self.info_value = []
        self._info_name = False
        self._info_value = False
        self.info = {}

    def handle_starttag(self, tag, attrs):  # 开始标签
        if len(attrs) > 0:
            attr = attrs[0]
        else:
            return
        if tag == 'div' and 'lemma-summary' in attr:
            self._desc_flag = True
        elif tag == 'dt' and 'basicInfo-item name' in attr:
            self._info_name = True
        elif tag == 'dd' and 'basicInfo-item value' in attr:
            self._info_value = True
        elif tag == 'div' and 'configModuleBanner' in attr:
            self._desc_flag = False
        else:
            return
        self._data_flag = ''

    def handle_endtag(self, tag):  # 结束标签
        _data = self._data_flag.replace('\n', '').replace(u'\xa0', '')
        if tag == 'dt':
            self._info_name = False
            if _data:
                self.info_name.append(_data)
        elif tag == 'dd':
            self._info_value = False
            if _data:
                self.info_value.append(_data)

    def handle_data(self, data):  # 内容
        if self._desc_flag:
            self.desc += data
        elif self._info_name:
            self._data_flag += data
        elif self._info_value:
            self._data_flag += data

    def basic_info(self):  # 基本信息
        for k, v in zip(self.info_name, self.info_value):
            if k == v:
                continue
            self.info[k] = v
        return self.info

    def describe(self):  # 摘要
        return self.desc.replace('\n', '').replace(u'\xa0', '')


class BaiDuInfoSearch:
    """百度百科搜索基本信息

    >>> bd = BaiDuInfoSearch('玛卡')
    >>> print(bd.desc())
    >>> print(bd.info())
    """

    def __init__(self, data):
        if '<html>' not in data:
            data = Load_BaiDuBaiKe(data)
        self._BD = _InfoSearch()
        self._BD.feed(data)

    def info(self):
        """基本信息"""
        info = self._BD.basic_info()
        info = re.sub(r'\[\d*-?\d*\]', '', str(info))
        return eval(info)

    def desc(self):
        """描述信息"""
        return re.sub(r'\[\d*-?\d*\]', '', self._BD.describe())


def Load_BaiDuBaiKe(name):
    """下载百度百科里面的内容信息

    :param name: 百科百科名字
    :return: 百度百科的文本信息
    """
    url = F'https://baike.baidu.com/item/{quote(name)}'
    response = requests.get(url, headers=headers_ua())
    data = response.content.decode('utf-8')
    return data


if __name__ == '__main__':
    import pprint

    bd = BaiDuInfoSearch('玛卡')
    print(bd.desc())
    pprint.pprint(bd.info())
