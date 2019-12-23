#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/23 17:16
# @Author: Jtyoui@qq.com
import logging.config
import os
import configparser


# 参考文档：https://docs.python.org/zh-cn/3.7/library/logging.handlers.html?highlight=timedrotatingfilehandler


def get_log_config(config_path=None, custom_dir=None) -> configparser:
    """加载当前文件下的log.ini文件

    默认日志文件夹在当前运训目录的logs下
    如果要自定义文件夹，只需要将custom_dir定义该目录即可，修改目录下的日志文件夹只需要定义handlers即可，程序会自动寻找handlers下的args的值。
    [handlers]
    keys = consoleHandler,fileHandler,errorHandler

    :param config_path: 日志文件配置
    :param custom_dir: 自定义日志文件夹
    :return: 日志文件配置对象
    """
    import sys  # 不能删除，程序会自动加载，勿删除
    cfg = configparser.RawConfigParser()
    if not config_path:
        config_path = os.path.dirname(__file__) + os.sep + 'log.ini'
    cfg.read(config_path)
    if custom_dir:
        if not os.path.exists(custom_dir):
            os.mkdir(custom_dir)
        handle = cfg.items('handlers')
        for _, v in handle:
            for vs in v.split(','):
                for key, value in cfg.items('handler_' + vs):
                    if key == 'args':
                        e = eval(value)
                        if isinstance(e[0], str):
                            es = custom_dir + os.sep + os.path.basename(e[0])
                            value = str((es, *e[1:]))
                            cfg.set('handler_' + vs, 'args', value)
    else:
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
    return cfg


def set_log_file_config(config: configparser):
    """加载配置文件到内存"""
    logging.config.fileConfig(config)


def log_file_config():
    """默认加载配置文件"""
    c = get_log_config()
    set_log_file_config(c)


if __name__ == '__main__':
    log_file_config()  # 加载默认配置文件，如果要自定义，流程如下：c = get_log_config() 先对c对象进行修改，set_log_file_config(c)
    logging.info('默认加载到root下')

    info = logging.getLogger('info')
    info.info('日志文件写道info.log文件下')

    error = logging.getLogger('error')
    error.error('日志文件写道error.log文件下')
