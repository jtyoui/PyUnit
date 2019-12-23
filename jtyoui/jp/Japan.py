#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 19:48
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from urllib.parse import quote
from jtyoui.error import LibraryNotInstallError
from jtyoui.decorators import replace_regular
from jtyoui.web import header
import requests

# 记住下次换缓存
Response_Headers = """cookie: HJ_UID=a0752831-ba30-9486-ddc8-66bcbb7f303a; _REF=https://www.baidu.com/link?url%3DTvv2c125EbCEB2T5xBtSlQeMb4zSO1v2ZkeB8uvhFXacQdks-Z0OXCabLXXX-Wpa&wd%3D&eqid%3D9cbe02970005752c000000025cd1684b; _REG=www.baidu.com|; _SREG_3=www.baidu.com|; HJ_CST=0; HJ_CSST_3=0; _SREF_3=https://www.baidu.com/link?url%3DTvv2c125EbCEB2T5xBtSlQeMb4zSO1v2ZkeB8uvhFXacQdks-Z0OXCabLXXX-Wpa&wd%3D&eqid%3D9cbe02970005752c000000025cd1684b; TRACKSITEMAP=3%2C6%2C; HJ_SID=5b45f4b2-9ae1-4a93-803b-7e2d08faba78; HJ_SSID_3=e959e1f7-6b25-4c49-a26d-a914297c0f32
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"""

word = {
    '自动词・五段/一类': '自Ⅰ',
    '形容动词/ナ形容词': '形Ⅱ',
    '他动词・一段/二类': '他Ⅱ',
    '他动词・五段/一类': '他Ⅰ',
    '自动词・一段/二类': '自Ⅱ',
    '形容词/イ形容词': '形Ⅰ',
    '自动词・サ变/三类': '自Ⅲ',
    '他动词・サ变/三类': '他Ⅲ',
    '他・サ变/三类': '他Ⅲ',
    '他・一段/二类': '他Ⅱ',
    '他・五段/一类': '他Ⅰ',
}


@replace_regular(r'（(.+)）|《(.+)》|[0-9].', '')
def sub_names(names):
    return names


def analysis(data_name, response_headers=Response_Headers):
    """分析单词、爬去小D网站：https://dict.hjenglish.com/jp/jc/%E3%81%AB%E3%81%8E%E3%82%8F%E3%81%86"""
    try:
        from bs4 import BeautifulSoup  # pip install bs4
    except Exception as _:
        raise LibraryNotInstallError('安装 pip install bs4')
    total = []
    ws = open(data_name + '.data', 'w', encoding='utf8')
    with open(data_name, encoding='utf8') as f:
        for line in f:
            lines = line[:-1]
            if len(lines) > 1 and (lines not in total):
                total.append(lines)
                name = lines
                url = F'https://dict.hjenglish.com/jp/jc/{quote(name)}'
                response = requests.get(url=url, headers=header(response_headers))
                data = response.text
                sp = BeautifulSoup(data, 'html.parser')
                pjm = sp.find(class_='pronounces')
                if pjm:
                    pjm = pjm.span.text[1:-1]
                else:
                    continue
                cx = sp.find(class_='simple')
                x = cx.h2
                if x:
                    x = x.text[1:-1]
                else:
                    continue
                m = cx.ul.text.replace('\n', '')
                m = sub_names(m).replace('。', '；')[:-1]
                if len(m) > 40:
                    continue
                if name != pjm:
                    name = "(" + name + ")"
                else:
                    name = None
                x = '<' + x + '>'
                for k, v in word.items():
                    x = x.replace(k, v)
                x = x.replace('词', '')
                if len(m) <= 1:
                    continue
                if name:
                    string = F'{pjm}{name}\t{x}\t{m}'
                else:
                    string = F'{pjm}\t{x}\t{m}'
                print(string)
                ws.write(string + '\n')
                ws.flush()


def cut(text_name):
    """从原始数据里面提取日语单词

    :param text_name: 原始数据的文件地址
    :return: 返回提取数据文本的地址
    """
    try:
        from janome.tokenizer import Tokenizer  # pip install janome
    except Exception as _:
        raise LibraryNotInstallError('安装 pip install janome')

    w = open(text_name + '.jp', 'w', encoding='utf8')
    t = Tokenizer()
    fp = open(text_name, encoding='utf-8')
    for token in t.tokenize(fp.read()):
        words = token.base_form
        words = words.replace(' ', '')
        if len(words) > 1:
            w.write(words + '\n')
    return text_name + '.jp'


if __name__ == '__main__':
    c = cut('2011年日语高考真题.txt')
    analysis(c)
