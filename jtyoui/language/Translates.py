#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/29 14:58
# @Author: Jtyoui@qq.com
from urllib.parse import quote
import requests
from jtyoui.web import header
from html.parser import HTMLParser
from jtyoui.data import Languages

# 请求头数据
# https://dict.hjenglish.com/ 更新请求头cookie
_headers = header("""cookie: HJ_CST=1; HJ_CSST_3=1; HJ_SID=58dfee85-f85c-a234-f219-b79dcb7e1e9d; _REF=https://www.baidu.com/link?url%3D1PPFhXl2aDlh33a6R3XE_eUsUW7banuolBKo19dvNXD8eQK8Qf1vvpCORFg1ShyF&wd%3D&eqid%3D812dd4340002b121000000065cc69469; _REG=www.baidu.com|; HJ_SSID_3=ea24368a-e9e2-9b58-9b38-8a90fb70cbae; _SREF_3=https://www.baidu.com/link?url%3D1PPFhXl2aDlh33a6R3XE_eUsUW7banuolBKo19dvNXD8eQK8Qf1vvpCORFg1ShyF&wd%3D&eqid%3D812dd4340002b121000000065cc69469; _SREG_3=www.baidu.com|; HJ_UID=18a93035-bcf4-49bd-a944-1d64e9099ce5; TRACKSITEMAP=3%2C
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36""")


class _Html(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self._flag = False
        self.string = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and 'simple' in attrs[0]:
            self._flag = True

    def handle_endtag(self, tag):
        if tag == 'div':
            self._flag = False

    def handle_data(self, data):
        if self._flag:
            self.string += data


def translate_to_chinese(name, languages, headers=_headers):
    """将一种语言翻译成中文

    :param name: 单词
    :param languages: 语言、及包含：from jtyoui.data import Languages
    :param headers: 请求头。更新方法：https://dict.hjenglish.com/
    :return: 中文
    """
    names = quote(name)
    if isinstance(languages, Languages):
        languages = languages.value
    if languages == '英语':
        url = f'https://dict.hjenglish.com/w/{names}'
    elif languages == '日语':
        url = f'https://dict.hjenglish.com/jp/jc/{names}'
    elif languages == '韩语':
        url = f'https://dict.hjenglish.com/kr/{names}'
    elif languages == '法语':
        url = f'https://dict.hjenglish.com/fr/{names}'
    elif languages == '德语':
        url = f'https://dict.hjenglish.com/de/{names}'
    elif languages == '西班牙语':
        url = f'https://dict.hjenglish.com/es/{names}'
    else:
        return ''
    s = requests.get(url, headers=headers)
    date = s.text
    jp = _Html()
    jp.feed(date)
    jp.close()
    s = jp.string
    s = s.replace('\n', '').replace(' ', '')
    if '】' in s:
        index = s.find('】')
        s = s[index + 1:]
    return s


if __name__ == '__main__':
    print(translate_to_chinese('good', Languages.English))  # 英语
    print(translate_to_chinese('アベンジャーズ', Languages.Japanese))  # 日语
    print(translate_to_chinese('안녕하세요', Languages.Korean))  # 韩语
    print(translate_to_chinese('Bonjour', Languages.French))  # 法语
    print(translate_to_chinese('Hallo', Languages.German))  # 德语
    print(translate_to_chinese('Amor', Languages.Spanish))  # 西班牙语
