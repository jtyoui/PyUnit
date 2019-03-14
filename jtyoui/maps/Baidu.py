#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/14 9:06
# @Author: Jtyoui
from jtyoui.web import random
from jtyoui.error import BaiDuMapError
import requests
from random import choice
from math import ceil

_total_data = []
AK = ['8R82NkA5j2YzCO1hG2grXUxdLQnnHdVA', 'mSYhaXLLGXffSkkgkalK84RV0Aof22vA', 'OpYA7uSs7czqHw68w07ZzE9t08RQWrfO',
      'Tffez86k4u6rwGmE3MPR2N3XtUUNbZ7H', 'rINxBQe6h4OGbmrLiImffAj96ZlhxCY8', 'V6QYkOxaGwvU3WDVZKBdNUVjVvLcwQpH']


class Data:
    def __init__(self, name, location, address):
        self.name = name
        self.location = location
        self.address = address

    def __repr__(self):
        return '名字:' + self.name + '\t坐标:' + self.location + '\t地址:' + self.address

    def __str__(self):
        return '名字:' + self.name + '\t坐标:' + self.location + '\t地址:' + self.address


def get_data(title, scope, page_size=20, page_num=0):
    global _total_data
    ak = choice(AK)
    address = f'http://api.map.baidu.com/place/v2/search?query={title}&region={scope}&output=json&ak={ak}&page_size=' \
        f'{page_size}&page_num={page_num}'
    r = requests.get(address, headers={'User-Agent': random()})
    json = r.json()
    print(json)
    status = json.get('status')
    if status == 401:
        get_data(title, scope, page_num=page_num)
        return None
    elif str(status).startswith('3'):
        raise BaiDuMapError('该模块已经废弃不可用')
    results = json['results']
    total = json['total']
    page = ceil(total / page_size)
    current_page = page_num + 1
    for result in results:
        name = result['name']
        locations = result['location']
        location = str(locations['lng']) + '|' + str(locations['lat'])
        address = result.get('province') + result.get('city') + result.get('area') + result.get('address')
        _total_data.append(Data(name, location, address))
    if current_page < page:
        get_data(title, scope, page_num=current_page)


def bd_map(title, scope, page_size=20, page_num=0):
    get_data(title, scope, page_size, page_num)
    return _total_data


def save_txt(file):
    with open(file, encoding='utf-8', mode='a') as f:
        for d in _total_data:
            f.write(str(d) + '\n')


def save_csv(file):
    with open(file, encoding='GBK', mode='w') as f:
        for d in _total_data:
            d = str(d).replace('\t', ',')
            f.write(d + '\n')


if __name__ == '__main__':
    bd = bd_map('景区', '黔东南苗族侗族自治州')
    # save_txt('./景区.txt')
    save_csv('./景区.csv')
