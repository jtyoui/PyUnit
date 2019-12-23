#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/12/2 10:17
# @Author: Jtyoui@qq.com

"""
正则解析器
"""
try:
    import xml.etree.cElementTree as et
except ModuleNotFoundError:
    import xml.etree.ElementTree as et
import re


class RegexEngine:
    def __init__(self, xml, str_):
        """加载正则表。正则表为xml

        :param xml: 正则表的位置
        :param str_: 要匹配的字符串
        """
        self._string = str_
        self._root = et.parse(xml).getroot()
        self.re = ''
        self.data = []

    def select(self, tag):
        """根据xml的tag来实现不同的正则提取

        :param tag: xml的tag标签
        :return: 正则提取的数据
        """
        root = self._root.find(tag)
        attrib = root.attrib
        if attrib.get('part', 'False').lower() == 'true':
            self._part_tag(root)
            return list(filter(lambda x: x[1], self.data))
        else:
            sf = self._no_part(root)
            self.re = ''.join(self.data) + sf
            return re.findall(self.re, self._string)

    def _no_part(self, tags):
        """tag标签不分开抽取"""
        for tag in tags:
            if tag:
                if tag.attrib.get('must', 'true').lower() == 'true':
                    self.data.append(self.re)
                    self.re = ''
                    self.re = '(?:' + self._no_part(tag) + ')'
                else:
                    self.re = self._no_part(tag)
            else:
                attrib = tag.attrib
                text = tag.text.strip()
                if attrib.get('must', 'true').lower() == 'true':
                    self.re = '(?:' + text + ')'
                else:
                    self.re += '(?:' + text + ')?'
        return self.re

    def _part_tag(self, tags):
        """tag标签分开提取"""
        for tag in tags:
            if tag:
                self._part_tag(tag)
            else:
                self.data.append((tag.tag, re.findall(tag.text.strip(), self._string)))

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, str_):
        self._string = str_
        self.re, self.data = '', []
