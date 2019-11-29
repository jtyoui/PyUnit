# **EE** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 实体抽取模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/EE-实体抽取-black.svg)]()


### 安装
    pip install jtyoui
    pip install paddlepaddle==1.6.1

### 模型（model）下载
[点击下载模型](http://oss.tyoui.cn/%E5%AE%9E%E4%BD%93%E6%8A%BD%E5%8F%96%E6%A8%A1%E5%9E%8B.rar?attname=)


### 实体抽取
```python
from jtyoui.ee import EntityExtraction
if __name__ == '__main__':
    ee = EntityExtraction(
        '李斯从金阳世纪城打到中天铭廷，他的车牌是：贵AU8080。并且他的电话是：15180864970，身份证号码是：522121193702157024，时间是昨天下午2点半，他在花溪公园玩耍',
        model_path='D://model')
    print(ee.time)        #抽取时间：['2019-11-28 14:30:00']
    print(ee.address)     #抽取地址：['金阳世纪城', '花溪公园']
    print(ee.car_plate)   #抽取车牌：['贵AU8080']
    print(ee.org)         #抽取机构名：['中天铭廷']
    print(ee.people)      #抽取人名：['李斯']
    print(ee.phone)       #抽取电话号码：['15180864970']
    print(ee.re_card)     #抽取身份证：['522121193702157024']
    print(ee.re_num)      #抽取数字：['8080', '15180864970', '522121193702157024', '2']
    
    # 从来数据，无需在加载
    ee.sentences='数据'
    print(ee.address)
    ...
    ...
```

***
[1]: https://blog.jtyoui.com