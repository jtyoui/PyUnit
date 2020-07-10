#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 10:58
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from pyunit_address import *
from pyunit_calendar import *
from pyunit_color import *
from pyunit_gof import *
from pyunit_idcard import *
from pyunit_log import *
from pyunit_map import *
from pyunit_phone import *
from pyunit_phone import *
from pyunit_plate import *
from pyunit_prime import *
from pyunit_sogou import *
from pyunit_string import *
from pyunit_time import *
from pyunit_tool import *
from pyunit_weather import *

__all__ = [a for a in dir() if not a.startswith('_')]
__version__ = f'2020.7.8'
__author__ = 'Jtyoui'
__description__ = f'这是一个Python集合包,包含了:{len(__all__)}个模块。'
__email__ = 'jtyoui@qq.com'
__web__ = 'https://blog.jtyoui.com'
__blog__ = 'https://blog.csdn.net/qq_23985359'
