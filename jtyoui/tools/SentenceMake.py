#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 21:44
# @Email  : jtyoui@qq.com
# @Software: PyCharm
import requests
from jtyoui.web import headers_ua, ParseHtml

url = 'http://zaojv.com/wordQueryDo.php'


class Sentence:
    def __init__(self):
        self._size = 0

    def get_size(self):
        return self._size

    def _get_sentence(self, word):
        response = requests.post(url, headers=headers_ua, data={'wo': word, 'directGo': 1, 'nsid': 0})
        text = response.text
        p = ParseHtml('div', ['class="info"'], 'div', [])
        p.feed(text)
        size = p.get_data()
        self._size = size[4:size.index('创建')]
        p.close()
        p = ParseHtml('div', ['id="all"'], 'span', ['style="font-weight:bold;"'])
        p.feed(text)
        content = p.get_data()
        print(content)
        if content:
            content = content.split('\r\n', 1)[0]
            content = content[:content.index('function') - 1] + content[content.index('();') + 3:]
            return content

    def __getitem__(self, item):
        return self._get_sentence(item)


if __name__ == '__main__':
    s = Sentence()
    data = s['好看']
    print(s.get_size())
    print(data)
