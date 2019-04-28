#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 21:56
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from html.parser import HTMLParser


class _InfoSearch(HTMLParser):
    """基类"""

    def __init__(self):
        HTMLParser.__init__(self)
        self._data_flag = ''
        self.desc = ''
        self._desc_flag = False
        self.info_name = []
        self.info_value = []
        self._info_name = False
        self._info_value = False
        self.info = {}

    def handle_starttag(self, tag, attrs):  # 开始标签
        if len(attrs) > 0:
            attr = attrs[0]
        else:
            return
        if tag == 'div' and 'lemma-summary' in attr:
            self._desc_flag = True
        elif tag == 'dt' and 'basicInfo-item name' in attr:
            self._info_name = True
        elif tag == 'dd' and 'basicInfo-item value' in attr:
            self._info_value = True
        else:
            return
        self._data_flag = ''

    def handle_endtag(self, tag):  # 结束标签
        _data = self._data_flag.replace('\n', '').replace(u'\xa0', '')
        if tag == 'div':
            self._desc_flag = False
        elif tag == 'dt':
            self._info_name = False
            if _data:
                self.info_name.append(_data)
        elif tag == 'dd':
            self._info_value = False
            if _data:
                self.info_value.append(_data)

    def handle_data(self, data):  # 内容
        if self._desc_flag:
            self.desc += data
        elif self._info_name:
            self._data_flag += data
        elif self._info_value:
            self._data_flag += data

    def basic_info(self):  # 基本信息
        for k, v in zip(self.info_name, self.info_value):
            self.info[k] = v
        return self.info

    def describe(self):  # 摘要
        return self.desc.replace('\n', '').replace(u'\xa0', '')


class BaiDuInfoSearch:
    """百度百科搜索基本信息"""

    def __init__(self, data):
        self.BD = _InfoSearch()
        self.BD.feed(data)

    def info(self):
        """基本信息"""
        return self.BD.basic_info()

    def desc(self):
        """描述信息"""
        return self.BD.describe()

    def close(self):
        return self.BD.close()


if __name__ == '__main__':
    text = """</div><div class="lemma-summary" label-module="lemmaSummary">
<div class="para" label-module="para">遵义，简称“遵”，位于<a target=_blank href="/item/%E8%B4%B5%E5%B7%9E">贵州</a>省北部，黔川渝三省市结合部中心城市，是国家全域旅游示范区。南临<a target=_blank href="/item/%E8%B4%B5%E9%98%B3%E5%B8%82/6085276" data-lemmaid="6085276">贵阳市</a>，北倚<a target=_blank href="/item/%E9%87%8D%E5%BA%86%E5%B8%82/436625" data-lemmaid="436625">重庆市</a>，西接<a target=_blank href="/item/%E5%9B%9B%E5%B7%9D%E7%9C%81/15626925" data-lemmaid="15626925">四川省</a><a target=_blank href="/item/%E6%B3%B8%E5%B7%9E%E5%B8%82/2930134" data-lemmaid="2930134">泸州市</a>。处于成渝—黔中<a target=_blank href="/item/%E7%BB%8F%E6%B5%8E%E5%8C%BA/2528042" data-lemmaid="2528042">经济区</a>走廊的核心区和主廊道，黔渝合作的桥头堡、主阵地和先行区。是西南地区承接南北、连接东西、通江达海的重要交通枢纽。全市辖3个区、9个县、2个县级市，属亚热带季风气候，终年温凉湿润，冬无严寒，夏无酷暑，雨量充沛，日照充足。</div><div class="para" label-module="para">遵义是首批国家历史文化名城，拥有<a target=_blank href="/item/%E4%B8%96%E7%95%8C%E6%96%87%E5%8C%96%E9%81%97%E4%BA%A7/290153" data-lemmaid="290153">世界文化遗产</a><a target=_blank href="/item/%E6%B5%B7%E9%BE%99%E5%B1%AF/2814846" data-lemmaid="2814846">海龙屯</a>、<a target=_blank href="/item/%E4%B8%96%E7%95%8C%E8%87%AA%E7%84%B6%E9%81%97%E4%BA%A7/6505343" data-lemmaid="6505343">世界自然遗产</a><a target=_blank href="/item/%E8%B5%A4%E6%B0%B4%E4%B8%B9%E9%9C%9E/3571978" data-lemmaid="3571978">赤水丹霞</a>。享有中国长寿之乡、中国厚朴之乡、中国金银花之乡、中国高品质绿茶产区、<a target=_blank href="/item/%E4%B8%AD%E5%9B%BD%E5%90%8D%E8%8C%B6%E4%B9%8B%E4%B9%A1/13389579" data-lemmaid="13389579">中国名茶之乡</a>、中国吉他制造之乡等称号。曾获得<a target=_blank href="/item/%E5%85%A8%E5%9B%BD%E6%96%87%E6%98%8E%E5%9F%8E%E5%B8%82/1669848" data-lemmaid="1669848">全国文明城市</a>、国家森林城市、国家卫生城市、双拥模范城市、中国优秀<a target=_blank href="/item/%E6%97%85%E6%B8%B8">旅游</a>城市、国家园林城市等多项殊荣。同时也是中国三大名酒<sup class="sup--normal" data-sup="1" data-ctrmap=":1,">
[1]</sup><a class="sup-anchor" name="ref_[1]_11847612">&nbsp;</a></div>
<dt class="basicInfo-item name">中文名称</dt>
<dd class="basicInfo-item value">遵义市</dd>
<dt class="basicInfo-item name">外文名称</dt>
<dd class="basicInfo-item value">Zunyi City</dd>
"""
    bd = BaiDuInfoSearch(text)
    print(bd.desc())
    print(bd.info())
