#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 13:17
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from jtyoui.web import get
from urllib.request import urlretrieve
import tempfile
import json
import re
import os
import shutil
import time


class BaiDuWenKu:
    """下载百度文库资料

    url是下载百度文库的文档链接

    >>> wk = BaiDuWenKu(url=r'https://wenku.baidu.com/view/f50def7c43323968001c924c.html?sxts=1563610333674')
    >>> wk.load('D:')
    """

    def __init__(self, url):
        """爬取百度文库：URL是文库资料地址"""
        self.url = url
        self.id = self.url[29:self.url.find('.html')]

    def load(self, save_path):
        """
        下载资料

        :param save_path: 保存文件地址
        :return: 成功返回True
        """
        dirs = tempfile.mkdtemp()
        print('创建临时文件夹：', dirs)
        types, title, date = self.get_title()
        if types == 'ppt':
            return self._ppt(dirs, save_path, title)
        elif types == 'doc':
            pass
        elif types == 'txt':
            return self._txt()
        elif types == 'pdf':
            return self._pdf(dirs, date)
        return False

    def get_title(self):
        """获得资料的标题和类型

        :return: 返回类型、标题、数据
        """
        data = get(self.url).content.decode('gbk')
        types = re.findall(r'\'docType\': \'\w+\'', data)[0][12:-1]
        title = re.findall(r'\'title\': \'.*\'', data)[0][10:-1]
        return types, title, data

    def _ppt(self, dirs, save_path, title):
        from jtyoui.imagepdf import image_pdf
        """下载带有ppt格式"""
        content_url = "https://wenku.baidu.com/browse/getbcsurl?doc_id=" + self.id + "&pn=1&rn=99999&type=ppt"
        print(content_url)
        content = get(content_url).content.decode('gbk')
        data = json.loads(content)
        start = time.time()
        for size, img in enumerate(data, 1):
            print('\r[下载进度]:%s%.2f%%' % ('>' * int((size * 50 / len(data))), float(size / len(data) * 100)))
            page, zoom = img['page'], img['zoom']
            urlretrieve(zoom, filename=dirs + os.sep + str(page) + '.jpg')
        image_pdf(file_dir=dirs, pdf_address=save_path + os.sep + title)
        shutil.rmtree(dirs)
        end = time.time()
        print('\n下载成功，保存地址：', save_path + os.sep + title + '.pdf', '一共耗时：', end - start, '秒')
        print('删除临时文件夹成功！')
        return True

    def _txt(self):
        url = "https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=" + self.id
        print(url)

    def _pdf(self, dirs, html):
        pass


if __name__ == '__main__':
    wk = BaiDuWenKu(url=r'https://wenku.baidu.com/view/f50def7c43323968001c924c.html?sxts=1563610333674')
    wk.load(r'D:')
