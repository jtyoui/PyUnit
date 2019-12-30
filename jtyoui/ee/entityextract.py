#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/25 14:19
# @Author: Jtyoui@qq.com
import jtyoui
import re
import os


class EntityExtraction:
    """信息抽取"""

    def __init__(self, sentence: str, model_path: str = None):
        self.sentence = sentence
        self.num = None
        self.model_path = model_path
        if self.model_path and os.path.exists(self.model_path):
            self._st = self._load_model()
            self._load()

    def _load_model(self):
        from jtyoui.neuralNetwork import ernie_st, ernie_match
        self.ernie_match = ernie_match
        return ernie_st(self.model_path)

    def _nn(self, r):
        """根据正则去获取实体"""
        ls = self.num
        word = []
        if ls:
            ls = jtyoui.join('', ls)
            for index in re.finditer(r, ls):
                word.append(self.sentence[index.start():index.end()])
        return word

    @property
    def people(self):
        """提取人名"""
        return self._nn('[01]+')

    @property
    def address(self):
        """提取地址"""
        return self._nn('[45]+')

    @property
    def org(self):
        """提取机构名"""
        return self._nn('[23]+')

    def _load(self):
        """抽取信息"""
        self.num = self.ernie_match(self.sentence, self._st)

    @property
    def time(self):
        """提取时间"""
        p = jtyoui.ParseTime(self.sentence)
        return p.find_times()

    @property
    def re_num(self):
        """提取数字"""
        return re.findall(r'\d+', self.sentence)

    @property
    def car_plate(self):
        """提取车牌号码"""
        return jtyoui.plate_number(self.sentence)

    @property
    def phone(self):
        """提取手机号码"""
        t = jtyoui.telephone_number_matching_verification(jtyoui.ALL_Mobile_Data_Network_Card_RE, self.sentence)
        return [i for i in t]

    @property
    def re_card(self):
        """提取身份证号码"""
        cards = []
        for i in re.findall(r'\d{18}|\d{17}[Xx]|\d{15}', self.sentence):
            try:
                jtyoui.check_id_card(i)
                cards.append(i)
            except jtyoui.IdCardCheckError:
                ...
            except AssertionError:
                ...
        return cards

    def set_sentence(self, sentence):
        """从定义语句"""
        self.sentence = sentence
        if self.model_path:
            self._load()

    @property
    def sentences(self):
        return self.sentence

    @sentences.setter
    def sentences(self, sentence):
        self.set_sentence(sentence)


if __name__ == '__main__':
    ee = EntityExtraction(
        '李斯从金阳世纪城打到中天铭廷，他的车牌是：贵AU8080。并且他的电话是：15180864970，身份证号码是：522121193702157024，时间是昨天下午2点半，他在花溪公园玩耍',
        model_path='D://model')
    print(ee.time)
    print(ee.address)
    print(ee.car_plate)
    print(ee.org)
    print(ee.people)
    print(ee.phone)
    print(ee.re_card)
    print(ee.re_num)
    ee.sentence = '今天'
    print(ee.time)
