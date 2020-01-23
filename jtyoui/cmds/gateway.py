#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/9/9 17:16
# @Author: Jtyoui@qq.com
from jtyoui.error import NotLinuxSystemError
import uuid
import socket
import struct
import os


def get_mac_address() -> str:
    """获得本机MAC地址"""
    u = uuid.uuid1().hex[-12:]
    return ':'.join(u[i:i + 2] for i in range(0, len(u), 2))


def get_window_ip():
    """在window下获取ip"""
    name = get_window_name()
    return window_name_get_ip(name)


def get_linux_ip(eth):
    """在Linux下获取IP"""
    assert os.name == 'posix', NotLinuxSystemError('不是Linux系统')
    import fcntl
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', eth[:15])))
    return ip[20:24]


def auto_get_ip(eth=None):
    """自动获取ip地址

    :param eth: window下eth默认是None。在Linux下，eth对应着不同的网卡
    """
    if os.name == 'nt':
        return get_window_ip()
    elif os.name == 'posix':
        return get_linux_ip(eth)
    else:
        raise Exception('暂时支持Linux和window系统')


def window_name_get_ip(window_name):
    """根据window的名字来获取ip地址

    :param window_name: window的名字
    :return: 返回当前计算机的ip地址
    """
    return socket.gethostbyname(window_name)


def get_window_name():
    """获取window系统名"""
    return socket.getfqdn(socket.gethostname())


if __name__ == '__main__':
    print(get_window_name())
    print(get_mac_address())
    print(get_window_ip())
    if os.name == 'posix':
        print(get_linux_ip('ens192'))
    print(auto_get_ip())
    print(window_name_get_ip('tyoui-zhang'))
