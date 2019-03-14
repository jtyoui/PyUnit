# **Maps** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 地图模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/地图-Maps-black.svg)]()


#### 安装
    pip install jtyoui

#### 使用百度地图获取信息
```python
from jtyoui.maps import bd_map,save_txt,save_csv
if __name__ == '__main__':
    bd = bd_map('景区', '黔东南苗族侗族自治州')
    # save_txt('./景区.txt')  #保存文本
    save_csv('./景区.csv')    #保存cvs文件
```

#### 下载每一个省下面所有的景区,比如贵州省
```python
from jtyoui.data import GuiZhou
from jtyoui.maps import bd_map,save_csv
if __name__ == '__main__':
    for gz in GuiZhou:
        bd_map('景区', gz)
    save_csv('./贵州下所有的景区.csv')
```

### 下载全国(中国)下面的所有景区
```python
from jtyoui.data import Whole_Country
from jtyoui.maps import bd_map,save_csv
if __name__ == '__main__':
    for province in Whole_Country:
        for city in province:
            bd_map('景区', city)
    save_csv('./全国下面所有的景区.csv')
```

#### 文本结果
    名字:西江千户苗寨	坐标:108.179706,26.500228	地址:贵州省黔东南苗族侗族自治州雷山县黔东南苗族侗族自治州雷山县西江镇南贵村
    名字:镇远古城水上游	坐标:108.436202,27.054738	地址:贵州省黔东南苗族侗族自治州镇远县贵州省黔东南苗族侗族自治州舞阳镇步行街县委对面禹门码头
    名字:镇远古城	坐标:108.434873,27.056047	地址:贵州省黔东南苗族侗族自治州镇远县兴隆街21号
    名字:肇兴侗寨	坐标:109.173823,25.912452	地址:贵州省黔东南苗族侗族自治州黎平县黔东南苗族侗族自治州黎平县202省道肇兴侗寨景区
    名字:远古城旅游景区	坐标:108.424327,27.056491	地址:贵州省黔东南苗族侗族自治州镇远县贵州省黔东南苗族侗族自治州镇远县民主街196附近
    名字:丹寨万达小镇	坐标:107.813295,26.204159	地址:贵州省黔东南苗族侗族自治州丹寨县丹寨县东湖湖畔
    名字:加榜梯田	坐标:108.593352,25.608761	地址:贵州省黔东南苗族侗族自治州从江县从江县加榜乡加车村
    名字:岜沙苗寨	坐标:108.874765,25.72667	地址:贵州省黔东南苗族侗族自治州从江县贵州省黔东南从江县岜沙苗寨
    名字:凯里苗侗风情园	坐标:107.982339,26.56171	地址:贵州省黔东南苗族侗族自治州凯里市黔东南苗族侗族自治州凯里市风情大道
    名字:青龙洞	坐标:108.440116,27.055628	地址:贵州省黔东南苗族侗族自治州镇远县黔东南苗族侗族自治州镇远县周大街
    名字:黔东南旧州古镇	坐标:107.78954,26.991758	地址:贵州省黔东南苗族侗族自治州黄平县西北部

***
[1]: https://blog.jtyoui.com