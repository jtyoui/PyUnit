#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/19 0019
# @Email : jtyoui@qq.com


def header(request_headers):
    """
    将浏览器中的Request Headers头复制过来.进行改装成字典类型
    :param request_headers:  浏览器中的Request Headers头信息
    :return: 分割Headers头信息的键值对
    """
    headers = dict()
    for head in request_headers.rsplit('\n'):
        name, values = head.split(':', 1)
        headers[name] = values
    return headers


if __name__ == '__main__':
    h = """Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.9
Cache-Control:max-age=0
Connection:keep-alive
Cookie:UM_distinctid=168ff800e18655-08f0ece15a2295-4c277913-100200-168ff800e1b4b9; ASPSESSIONIDAZBYCXDW=1622273B73A768F308474040; Hm_lvt_353f6f980a356b6f65e5a65aad50c98e=1550208747,1550474802,1550474812,1550558911; Hm_lpvt_353f6f980a356b6f65e5a65aad50c98e=1550558911
Host:www.xunleige.com
If-Modified-Since:Tue, 19 Feb 2019 05:13:00 GMT
If-None-Match:"e02c95c811c8d41:0"
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6815.400 QQBrowser/10.3.3006.400"""
    print(header(h))
