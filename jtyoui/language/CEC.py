#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/29 17:44
# @Author: Jtyoui@qq.com

"""汉语纠错（Chinese error correction）"""
from jtyoui.language.PinYin import load_pin_yin, chinese_to_pin_yin
from collections import Iterable
import os


class ChineseError:
    def __init__(self, words_or_file):
        self.model = load_pin_yin(False)
        self._words = {}
        if (not isinstance(words_or_file, str)) and isinstance(words_or_file, Iterable):
            for word in words_or_file:
                ls = chinese_to_pin_yin(self.model, word)
                self._words[word] = ' '.join(ls)
        elif os.path.exists(words_or_file):
            with open(words_or_file, encoding='utf-8') as f:
                for line in f:
                    ls = chinese_to_pin_yin(self.model, line)
                    self._words[line] = ' '.join(ls)
        else:
            raise TypeError('输入一个纠错列表或者文件地址')

    def set_word(self, word):
        total = []
        ls = chinese_to_pin_yin(self.model, word)
        value = ' '.join(ls)
        for k, v in self._words.items():
            if v == value:
                total.append(k)
        return total

    def fuzzy_tone(self):
        pass


if __name__ == '__main__':
    ce = ChineseError(['北京', '上海'])
    print(ce.set_word('北经'))
