#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/14 13:59
# @Author: Jtyoui@qq.com
from jtyoui.web import get
from urllib.parse import quote


def math_tex(tex, file_path=None):
    """根据Tex语言生成数学公式矢量图

    关于Tex语法参考：https://blog.csdn.net/qfire/article/details/81382048

    :param tex: Tex语言
    :param file_path: 保存矢量图的地址，后缀名一定是: xxx.svg
    :return: 默认返回SVG数据。有地址保存到地址，返回True
    """
    u = quote(tex)
    name = hash(tex)
    s = get(f'https://math.jianshu.com/math?formula={u}')
    data = s.text
    if not file_path:
        file_path = './' + str(name) + '.svg'
    w = open(file_path, 'w')
    w.write(data)
    w.flush()
    w.close()
    return True


if __name__ == '__main__':
    Tex = r"""\begin{bmatrix}
    0 & \cdots & 0 \\
    \vdots & \ddots & \vdots \\
    0 & \cdots & 0
    \end{bmatrix}"""
    d = math_tex(Tex)
