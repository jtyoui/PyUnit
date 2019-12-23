#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 23:10
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from abc import ABC
from html.parser import HTMLParser


class ParseHtml(HTMLParser, ABC):
    """基类"""

    def __init__(self, start_tag, start_attr, end_tag, end_attr):
        """使用相当简单

        html = '<div class="declare" id="J-declare">声明：百科词条人人可编辑。<a class="declare-details"></a>'
        p = ParseHtml('div', ['class="declare"'], 'a', ['class="declare-details"'])
        p.feed(html)
        print(p.get_data())  # 声明：百科词条人人可编辑。

        :param start_tag: 开始标签，必须填写
        :param start_attr: 开始标签里面的属性，切记一定是列表[]类型。如果没有，传入空列表[]
        :param end_tag: 结束标签，必须填写
        :param end_attr: 结束标签里面的属性，切记一定是列表[]类型。如果没有，传入空列表[]
        """
        HTMLParser.__init__(self)
        self._data = ''
        self._flag = False
        self._start_tag = start_tag
        self._start_attr = self._split(start_attr)
        self._end_tag = end_tag
        self._end_attr = self._split(end_attr)

    def handle_starttag(self, tag, attrs):  # 开始标签
        for attr in self._start_attr:
            if attr not in attrs:
                break
        else:
            if tag == self._start_tag:
                self._flag = True
                return

        for att in self._end_attr:
            if att not in attrs:
                break
        else:
            if tag == self._end_tag:
                self._flag = False
                return

    def handle_endtag(self, tag):
        if not self._end_attr:
            if tag == self._end_tag:
                self._flag = False

    def handle_data(self, data):  # 内容
        if self._flag:
            self._data += data

    def get_data(self):
        """得到数据"""
        return self._data.strip()

    @staticmethod
    def _split(words):
        total = []
        for word in words:
            tag, attr = word.split('=', 1)
            total.append((tag, attr.replace('"', '')))
        return total


if __name__ == '__main__':
    html = '<div class="declare" id="J-declare">声明：百科词条人人可编辑。<a class="declare-details"></a>'
    p = ParseHtml('div', ['class="declare"'], 'a', ['class="declare-details"'])
    p.feed(html)
    print(p.get_data())  # 声明：百科词条人人可编辑。
