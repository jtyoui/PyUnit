#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/9/25 10:12
# @Author: Jtyoui@qq.com
import jtyoui
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help', '--h'])


def split_doc(func, name):
    f = getattr(jtyoui, func)
    doc = f.__doc__
    docs = doc.strip().split('\n')
    for x in docs:
        if ':param ' + name in x:
            return x
    return '联系作者写注释！'


@click.command()
@click.option('-f', type=str, help='文本地址')
@click.option('-n', type=int, help='成词最大粒度')
@click.option('-t', type=int, help='key出现的次数')
@click.option('-q', type=float, help='过滤的频率')
@click.option('-c', type=float, help='过滤凝聚度')
@click.option('-r', type=float, help='过滤自由度')
def neologism(f, n, t, q, c, r):
    from jtyoui.word.neologism import mains as m
    m(f, n, t, q, c, r)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0', help='当前版本')
def main(): ...


main.add_command(neologism)

if __name__ == "__main__":
    main()
