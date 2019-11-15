#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/9/25 10:12
# @Author: Jtyoui@qq.com
import jtyoui
import click
import os
import pprint

DESC = jtyoui.__description__ + '更新时间为20' + jtyoui.__version__.replace('.', '-') + '。'
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help', '--h'])


def split_doc(func, name):
    f = getattr(jtyoui, func)
    doc = f.__doc__
    docs = doc.strip().split('\n')
    for x in docs:
        if ':param ' + name in x:
            return x
    return '联系作者写注释！'


@click.group(context_settings=CONTEXT_SETTINGS, help=DESC)
@click.version_option(version='1.0.0', help='当前版本')
def main(): ...


@main.add_command
@click.command(help='成词发现')
@click.option('-f', type=str, help='文本地址')
@click.option('-n', type=int, help='成词最大粒度')
@click.option('-t', type=int, help='key出现的次数')
@click.option('-q', type=float, help='过滤的频率')
@click.option('-c', type=float, help='过滤凝聚度')
@click.option('-r', type=float, help='过滤自由度')
def neologism(f, n, t, q, c, r):
    print('等待中，正在训练数据.......')
    from jtyoui.word.neologism import mains as m
    m(f, n, t, q, c, r)
    print('训练完毕！')


@main.add_command
@click.command(help='创建Flask Docker项目文件')
@click.option('-f', type=str, help='创建Flask Docker项目的路径')
def docker_file(f):
    print('等待中.......')
    fp = os.path.abspath(f)
    jtyoui.create_docker_project(fp)
    print('创建成功！')


@main.add_command
@click.command(help='查询天气预报')
@click.option('-name', type=str, help='城市名字')
@click.option('-day', type=int, default=1, help='查询的天数：【1,7,15】、默认是当天。')
def weather(name, day):
    w = jtyoui.WeatherForecast()
    w.set_city(name)
    if day == 15:
        days = w.get_15day_weather()  # 获得当天 天气预报
    elif day == 7:
        days = w.get_7day_weather()  # 获得7天天气预报
    else:
        days = w.get_today_weather()  # 获得15天天气预报
    pprint.pprint(days)


@main.add_command
@click.command(help='更新pip包')
def upload():
    os.system('python setup.py sdist bdist_wheel')
    os.system('python -m twine upload dist/*')
    print('更新完毕！')


if __name__ == "__main__":
    main()
