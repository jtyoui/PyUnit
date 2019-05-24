# **Web** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 网页模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-网页-black.svg)]()


### 安装
    pip install jtyoui

### 使用header
```python
from jtyoui.web import header

if __name__ == '__main__':
    h = """
        Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Accept-Encoding:gzip, deflate, br
        Accept-Language:zh-CN,zh;q=0.9
        Cache-Control:max-age=0
        Connection:keep-alive
        Cookie:UM_distinctid=168ff800e18655-08f0ece15a2295-4c277913-100200-168ff800e1b4b9; ASPSESSIONIDAZBYCXDW=1622273B73A768F308474040; Hm_lvt_353f6f980a356b6f65e5a65aad50c98e=1550208747,1550474802,1550474812,1550558911; Hm_lpvt_353f6f980a356b6f65e5a65aad50c98e=1550558911
        Host:www.xunleige.com
        If-Modified-Since:Tue, 19 Feb 2019 05:13:00 GMT
        If-None-Match:"e02c95c811c8d41:0"
        Upgrade-Insecure-Requests:1
        User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6815.400 QQBrowser/10.3.3006.400
    """
    print(header(h))
    # {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': 'UM_distinctid=168ff800e18655-08f0ece15a2295-4c277913-100200-168ff800e1b4b9; ASPSESSIONIDAZBYCXDW=1622273B73A768F308474040; Hm_lvt_353f6f980a356b6f65e5a65aad50c98e=1550208747,1550474802,1550474812,1550558911; Hm_lpvt_353f6f980a356b6f65e5a65aad50c98e=1550558911', 'Host': 'www.xunleige.com', 'If-Modified-Since': 'Tue, 19 Feb 2019 05:13:00 GMT', 'If-None-Match': '"e02c95c811c8d41:0"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6815.400 QQBrowser/10.3.3006.400'}
```

#### 使用代理UA
```python
from jtyoui.web import random,headers_ua
if __name__ == '__main__':
        print(random()) #Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36
        print(headers_ua)#{'user-agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36'}
```

### 增加HTML解析
```python
from jtyoui.web import ParseHtml
if __name__ == '__main__':
    html = '<div class="declare" id="J-declare">声明：百科词条人人可编辑。<a class="declare-details"></a>'
    p = ParseHtml(start_tag='div',start_attr= ['class="declare"'], end_tag='a', end_attr=['class="declare-details"'])
    p.feed(html)
    print(p.get_data())  # 声明：百科词条人人可编辑。
```

***
[1]: https://blog.jtyoui.com