#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 21:44
# @Email  : jtyoui@qq.com
# @Software: PyCharm
"""声明：该函数是爬取造句网（http://zaojv.com/）句子，仅仅用于学习交流。"""
import requests
from jtyoui.web import headers_ua
import re


class Sentence:
    """造句函数，输入一个词语，造出一些句子

    >>> s = Sentence()
    >>> data = s['我爱你']
    >>> for jz in data:print(jz)

    """

    def __init__(self):
        self.url = 'http://zaojv.com/wordQueryDo.php'
        from bs4 import BeautifulSoup  # 安装bs4: pip install bs4
        self._BeautifulSoup = BeautifulSoup
        self.total = 1
        self.page = 1

    def _not_included_data(self, word):
        """未录取句子提取"""
        data_ls = []
        response = requests.post(self.url, headers=headers_ua(), data={'wo': word, 'directGo': 1, 'nsid': 0})
        text = response.text
        soup = self._BeautifulSoup(text, features="lxml")
        ls = soup.find('div', id='content').contents
        for d in ls:
            if not isinstance(d, str) and ('function' not in d.text):
                t = d.text.replace('\xa0', '').strip()
                if '造句' in t:
                    t = re.sub('[(（\\[【].*[^造]*造句.*[)】\\]）]', '', t)
                data_ls.append(t)
        return data_ls

    def _analysis_data(self, text):
        """录用句子提取"""
        data_ls = []
        soup = self._BeautifulSoup(text, features="lxml")
        page = soup.find('div', style='text-align:center;margin-top:10px;').text.strip().split('\xa0')
        self.page, self.total = page[7].split(r'/')
        ls = soup.find('div', id='all').contents
        for d in ls:
            if not isinstance(d, str) and ('function' not in d.text):
                t = d.text.replace('\xa0', '').strip()
                if '造句' in t:
                    t = re.sub('[(（\\[【].*[^造]*造句.*[)】\\]）]', '', t)
                data_ls.append(t)
        return data_ls

    def _redirect_link(self, word):
        """获得重定向的链接"""
        response = requests.post(self.url, headers=headers_ua(), data={'wo': word, 'directGo': 1, 'nsid': 0})
        return response.url

    @staticmethod
    def _get_page_data(url):
        """获得链接中的数据"""
        response = requests.get(url, headers=headers_ua())
        return response.text

    def make_sentence(self, word):
        """制造句子

        :param word: 输入一个词语:比如:刘德华、万绮雯、宇宙等
        """
        data_ls = []
        url_ = self._redirect_link(word)
        if url_ == self.url:
            d = self._not_included_data(word)
        else:
            text = self._get_page_data(url_)
            d = self._analysis_data(text)
        data_ls.extend(d)
        while self.total != self.page:
            page = int(self.page) + 1
            u = url_[:-5] + '_' + str(page) + '.html'
            text = self._get_page_data(u)
            data_ls.extend(self._analysis_data(text))
        return data_ls

    def __getitem__(self, item):
        return self.make_sentence(item)


if __name__ == '__main__':
    s = Sentence()
    data = s['我爱你']
    for jz in data:
        print(jz)
