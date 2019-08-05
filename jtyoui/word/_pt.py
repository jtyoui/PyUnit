#!/usr/bin/python3.7
# -*-coding:utf-8-*-
# @Time:2019/6/2115:40
# @Author:Jtyoui@qq.com
from jtyoui.data.wordNature import word_nature
import re

_wn = word_nature()


def continuous_pause(sentence: str) -> str:
    """去除多重断句符号"""
    return re.sub('[，。,.]{2,}', '，', sentence)


def punctuate(sentence):
    """根据词性进行简单校验断句"""
    p = continuous_pause(sentence)
    sent = ''
    max_len = len(p)
    for index, word in enumerate(p):
        if word in '，。,.':
            if index == 0:
                continue
            elif p[index - 1] in _wn['aw_tone']:
                continue
            elif max_len == index + 1:
                if p[index] in _wn['aw_structure']:
                    continue
            elif p[index + 1] in _wn['aw_structure']:
                continue
        sent += word
    return sent


if __name__ == '__main__':
    print(punctuate('你在哪.,里。.，我在天安门。.，'))
