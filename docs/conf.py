import sphinx_rtd_theme
import os
import sys
import time

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
project = 'jtyoui'
copyright = '2019, 张伟'
author = '张伟'
NOW_TIME = time.localtime(time.time())
release = f'{NOW_TIME.tm_year}.{NOW_TIME.tm_mon:0>2}.{NOW_TIME.tm_mday:0>2}'
templates_path = ['_templates']
language = 'zh_cn'
exclude_patterns = []
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
html_static_path = ['_static']
sys.path.insert(0, os.path.abspath('../../Jtyoui'))
