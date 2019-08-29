#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/29 9:11
# @Author: Jtyoui@qq.com
import functools
import logging
from jtyoui.logger.Log import set_log_file_config, get_log_config
import os


def log(log_file, config_file=None):
    def inner(fun):
        set_log_file_config(get_log_config(config_path=config_file, custom_dir=log_file))

        @functools.wraps(fun)
        def wraps(*args, **kwargs):
            try:
                logging.getLogger('info').info(f'正在执行：{fun.__name__}函数')
                f = fun(*args, **kwargs)
                logging.getLogger('info').info(f'执行完毕：{fun.__name__}函数')
                return f
            except Exception as e:
                logging.getLogger('info').error(f'执行：{fun.__name__}函数异常，异常信息:{str(e)}')
                with open(log_file + os.sep + 'error.log', 'a', newline='\n')as f:
                    f.write('+' * 70 + os.linesep)
                logging.getLogger('error').exception(e)
                with open(log_file + os.sep + 'error.log', 'a', newline='\n')as f:
                    f.write('#' * 70 + os.linesep + os.linesep)
            return False

        return wraps

    return inner


if __name__ == '__main__':
    @log('./ger')
    def division():
        s = 1 / 0
        return s


    division()
