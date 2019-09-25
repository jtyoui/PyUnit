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
@click.option('--sort', type=bool, default=False, help=split_doc('binary_search', 'sort'))
@click.option('--x', type=int, help=split_doc('binary_search', 'x'))
@click.option('--ls', type=str, help=split_doc('binary_search', 'ls'))
def binary_search(ls, x, sort):
    click.echo(jtyoui.binary_search(eval(ls), x, sort))


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0', help='当前版本')
def main(): ...


main.add_command(binary_search)

if __name__ == "__main__":
    main()
