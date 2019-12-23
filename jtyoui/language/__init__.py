#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/4 0004
# @Email : jtyoui@qq.com
# @Software : PyCharm
from .han import j_to_f, f_to_j  # 增加简体字互转繁体字
from .PinYin import load_pin_yin, chinese_to_pin_yin  # 增加拼音
from .Translates import translate_to_chinese  # 增加翻译到中文
from .CEC import ChineseError  # 汉语纠错
from .BaiDuTranslate import bai_du_translate, BaiDuLanguage  # 百度翻译
