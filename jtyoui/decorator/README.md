# **Decorator** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 常见的装饰器模块
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/Decorator-装饰器-black.svg)]()


#### 安装
    pip install jtyoui


#### 使用
```python

from jtyoui.regular import Non_Chinese
from jtyoui.decorator import replace_regular


@replace_regular(' ', '')
def remove_blank(a, b):
    print(a, b)


@replace_regular(Non_Chinese, '')
def remove_non_chinese(a, b):
    print(a, b)

if __name__ == '__main__':
    remove_blank('你好  吗?', b='我  很好!')
    remove_non_chinese('你好#$%76#%吗wore?', b='我$%^787word很好!')

```

***
[1]: https://blog.jtyoui.com