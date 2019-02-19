# **Web** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 邮箱模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-网页-black.svg)]()


### 安装
    pip install jtyoui

### 使用header
```python
from jtyoui.web import header

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
    # {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': 'UM_distinctid=168ff800e18655-08f0ece15a2295-4c277913-100200-168ff800e1b4b9; ASPSESSIONIDAZBYCXDW=1622273B73A768F308474040; Hm_lvt_353f6f980a356b6f65e5a65aad50c98e=1550208747,1550474802,1550474812,1550558911; Hm_lpvt_353f6f980a356b6f65e5a65aad50c98e=1550558911', 'Host': 'www.xunleige.com', 'If-Modified-Since': 'Tue, 19 Feb 2019 05:13:00 GMT', 'If-None-Match': '"e02c95c811c8d41:0"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6815.400 QQBrowser/10.3.3006.400'}
```
***
[1]: https://blog.jtyoui.com