#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/11 11:33
# @Author: Jtyoui@qq.com
from .regexengine import RegexEngine  # 正则解析器

Non_Chinese = r'[^\u4e00-\u9fa5]+'  # 匹配中文字符
Chinese = r'[\u4e00-\u9fa5]'  # 匹配非中文字符

# 邮箱
E_mail = r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
Blank = r'\n\s*\r'  # 空白字符
URL = r'[a-zA-z]+://[^\s]*'  # URL链接
Chinese_Telephone = r'\d{3}-\d{8}|\d{4}-\{7,8}'  # 中国电话号码
QQ = r'[1-9][0-9]{4,}'  # 腾讯qq号
Post_Office = r'[1-9]\d{5}(?!\d)'  # 邮编
Id_Card = r'^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$'  # 身份证
Digit = '[0-9]'
# 匹配(年-月-日)格式日期
Year_Month_Day = r'([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-' \
                 r'(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))'
whitespace_re = '[ \t\n\r\v\f]'
punctuation_re = r"""[!"#$%&'()*+，。？|！@#￥%&（）——+,-./:;<=>?@、^_`{|}~【】\[{\]}]"""

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

if __name__ == '__main__':
    import re

    print(re.findall(punctuation_re, '我是。[谁你是谁]}，'))
