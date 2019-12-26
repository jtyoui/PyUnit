#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/5/10 9:15
# @Author: Jtyoui@qq.com
import jtyoui
import os

"""
该方法属于大量日期转化。消耗内存为代价提高速度。该类只能查询1901-2099年。
"""
_CTC = {}
_TIANGAN_DIZHI = {}
_SC = {}


def load_date(load_date_dir):
    global _CTC, _TIANGAN_DIZHI, _SC
    if not os.path.exists(load_date_dir + os.sep + 'date.zip'):
        jtyoui.download_dev_tencent('date.zip', 'zhangwei0530', 'logo', load_date_dir,
                                    '79A5A43F33CA300CD2671DF1168B24E5')
    uz = jtyoui.unzip(load_date_dir + os.sep + 'date.zip', 'date.txt')
    ls = uz.split('\r\n')
    for line in ls[:-1]:
        ctc, cs, td = line.split('\t')
        _CTC[ctc] = cs
        _SC[cs] = ctc
        if _TIANGAN_DIZHI.get(td):
            _TIANGAN_DIZHI[td].append(ctc)
        else:
            _TIANGAN_DIZHI[td] = [ctc]


def td_to_ctc(td):
    """天干地支纪年转农历

    :param td: 输入一个天干地支纪年
    :return: 农历
    """
    return _TIANGAN_DIZHI.get(td)


def td_to_sc(td):
    """天干地支纪年转阳历

    :param td: 输入一个天干地支纪年
    :return: 阳历
    """
    ctc = td_to_ctc(td)
    return [ctc_to_sc(c) for c in ctc]


def ctc_to_sc(ctc):
    """农历转阳历

    :param ctc: 农历
    :return: 阳历
    """
    return _CTC.get(ctc)


def ctc_to_td(ctc):
    """农历转天干地支

    :param ctc: 农历
    :return: 天干地支,找不到返回空
    """
    for td_, ctc_ in _TIANGAN_DIZHI.items():
        if ctc in ctc_:
            return td_
    return ''


def sc_to_ctc(sc):
    """阳历转农历

    :param sc: 阳历
    :return: 农历
    """
    return _SC.get(sc)


def sc_to_td(sc):
    """阳历转天干地支纪年

    :param sc: 阳历
    :return: 天干地支纪年
    """
    ctc = sc_to_ctc(sc)
    return ctc_to_td(ctc)


if __name__ == '__main__':
    load_date('D://')
    print('-----------------------------')
    # 农历
    print(ctc_to_sc('1984年闰十月初三'))  # 农历转阳历 1984年11月25日
    print(ctc_to_td('1984年闰十月初三'))  # 农历转天干地支 甲子年乙亥月癸亥日
    print('-----------------------------')
    # 阳历
    print(sc_to_ctc('1984年11月25日'))  # 阳历转农历 1984年闰十月初三
    print(sc_to_td('1984年11月25日'))  # 阳历转天干地支 甲子年乙亥月癸亥日
    print('-----------------------------')
    # 天干地支
    print(td_to_ctc('甲子年乙亥月癸亥日'))  # 天干地支转农历:['1984年闰十月初三', '2044年九月廿一']
    print(td_to_sc('甲子年乙亥月癸亥日'))  # 天干地支转阳历:['1984年11月25日', '2044年11月10日']
