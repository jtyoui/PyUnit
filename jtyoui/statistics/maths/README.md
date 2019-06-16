# **maths** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 数学模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/数学-maths-black.svg)]()


### 安装
    pip install jtyoui


## 判断一个是否为质数
```python
from jtyoui.statistics.maths import is_prime
if __name__ == '__main__':
    print(is_prime(915453))
```

## 查询1-n的质数(查询1亿耗时5秒，内存4G，i5-8500CPU，联想笔记本)
```python
from jtyoui.statistics.maths import primes
if __name__ == '__main__':
    print(len(primes(1_0000_0000)))  # 时间5.5541136264801025秒
```

## 利用Tex生成数学公式照片
![Tex](https://gitee.com/tyoui/logo/raw/master/packet/math.svg)
```python
from jtyoui.statistics import math_tex
if __name__ == '__main__':
    Tex = r"""\begin{bmatrix}
    0 & \cdots & 0 \\
    \vdots & \ddots & \vdots \\
    0 & \cdots & 0
    \end{bmatrix}"""
    math_tex(Tex)
```
## 高精度计算π（能精确到：15万6千位）
```python
import jtyoui
if __name__ == '__main__':
    print(jtyoui.pi(10_0000)) # 计算10万位PI
```
***
[1]: https://blog.jtyoui.com