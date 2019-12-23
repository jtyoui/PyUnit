#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 16:16
# @Email  : jtyoui@qq.com
# @Software: PyCharm

from jtyoui.file_zip import load_zip
from jtyoui.web import random
import requests
import re
from html.parser import HTMLParser


class _GetData(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.weather_7d = False
        self.name = False
        self.addr = ''
        self.data_7d = []
        self.string = ''

    def handle_starttag(self, tag, attrs):
        if len(attrs) > 0:
            attr = attrs[0]
        else:
            return
        if tag == 'ul' and 't clearfix' in attr:
            self.weather_7d = True
        elif tag == 'div' and 'crumbs fl' in attr:
            self.name = True

    def handle_endtag(self, tag):
        if tag == 'ul':
            self.weather_7d = False
            if self.string:
                self.data_7d.append(self.string[:-1] + '风力')
                self.string = ''
        elif tag == 'div':
            self.name = False

    def handle_data(self, data):
        if self.weather_7d:
            data = data.replace('\n', '').replace(u'\xa0', '')
            if data:
                if '（' in data:
                    if self.string:
                        self.data_7d.append(self.string[:-1] + '风力')
                    self.string = data
                else:
                    self.string += data + ' '
        elif self.name:
            data = re.sub(r'[\r\n \t\xa0>]', '', data)
            self.addr += data


class WeatherForecast:
    def __init__(self):
        """天气预报，使用方法
        >>>import jtyoui
        >>>import pprint
        >>>w = jtyoui.WeatherForecast()
        >>>w.set_city('九龙')
        >>>pprint.pprint(w.get_today_weather())  # 获得当天 天气预报
        >>>pprint.pprint(w.get_7day_weather())  # 获得7天天气预报
        >>>pprint.pprint(w.get_15day_weather())  # 获得15天天气预报
        """
        self.weather = load_zip('city.zip', 'city.txt')
        self.codes = []

    def set_city(self, city):
        """输入一个城市名字

        :param city: 城市名字
        """
        if self.codes:
            self.codes.clear()
        for names in self.weather:
            code, city_ = names.split(',')
            if city_ in city:
                self.codes.append(code)

    def get_today_weather(self):
        """获得当天 天气预报"""
        total = []
        for code in self.codes:
            url = F'http://www.weather.com.cn/weather1d/{code}.shtml'
            response = requests.get(url, headers={'User-Agent': random()})
            response.encoding = 'utf-8'
            data = response.text
            d = re.findall(r'<input type="hidden" id="hidden_title" value="(.+)" />', data)
            gd = _GetData()
            gd.feed(data)
            total.append({gd.addr: d})
        return total

    def get_7day_weather(self):
        """获得7天 天气预报"""
        total = []
        for code in self.codes:
            url = F'http://www.weather.com.cn/weather/{code}.shtml'
            response = requests.get(url, headers={'User-Agent': random()})
            response.encoding = 'utf-8'
            gd = _GetData()
            gd.feed(response.text)
            total.append({gd.addr: gd.data_7d})
        return total

    def get_15day_weather(self):
        """获得15天 天气预报"""
        t_7d = self.get_7day_weather()
        for code in self.codes:
            url = F'http://www.weather.com.cn/weather15d/{code}.shtml'
            response = requests.get(url, headers={'User-Agent': random()})
            response.encoding = 'utf-8'
            gd = _GetData()
            gd.feed(response.text)
            for t in t_7d:
                if gd.addr in t:
                    t[gd.addr].extend(gd.data_7d)
        return t_7d


if __name__ == '__main__':
    import pprint

    w = WeatherForecast()
    w.set_city('九龙')
    pprint.pprint(w.get_today_weather())  # 获得当天 天气预报
    pprint.pprint(w.get_7day_weather())  # 获得7天天气预报
    pprint.pprint(w.get_15day_weather())  # 获得15天天气预报
