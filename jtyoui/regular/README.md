# **Regular** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 常用的正则表达式模块
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/regular-正则-black.svg)]()


#### 安装
    pip install jtyoui


#### 使用

```python
from jtyoui.regular import Non_Chinese
print(Non_Chinese)
```

## 正则解析器的标准XML格式
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <!--必须包含root根目录-->
    <!--在root根目录下写正则表达式-->
</root>
```

## 使用
![流程图](https://github.com/jtyoui/RegularResolver/blob/master/%E5%90%88%E5%B9%B6.png) 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <!--车牌号提取，其中CAR_PLATE是正则表达式的名字，part参数是必须的。默认是True，表示：是否要返回匹配到的正则名字-->
    <CAR_PLATE part="False"> 
        
        <!--车牌号匹配必须满足车牌号的前缀，must参数是必须的，默认值是False，表示：（True）一定满足才能满足车牌号匹配，类似于and-->
        <CAR_PREFIX must="True">
            [京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z][A-Z]
        </CAR_PREFIX>
        
        <!--车牌号匹配必须满足车牌号的后缀，must=True。表示：一定满足才能满足车牌号匹配-->
        <CAR_SUFFIX must="True">
            <ORDINARY_CAR must="False">
                [A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9挂学警港澳]
            </ORDINARY_CAR>

            <NEW_ENERGY_VEHICLE must="False">
                [0-9]{5}[DF]|[DF][A-HJ-NP-Z0-9][0-9]{4}
            </NEW_ENERGY_VEHICLE>
        </CAR_SUFFIX>
    </CAR_PLATE>
</root>
```

### 代码
```python
from jtyoui.regular import RegexEngine

if __name__ == '__main__':
    rr = RegexEngine('re.xml', '车牌号是贵AU8888')
    print(rr.select('CAR_PLATE'))  # ['贵AU8888']

    rr.string = '我的电话号码是：15180864933'
    print(rr.select('ALL_Mobile_Data_Network_Card'))  # [('MOVE_Card', ['15180864933'])]

    rr.string = '在来一个电话：18185787861吗？'
    print(rr.select('ALL_Mobile_Data_Network_Card'))  # [('TELECOM_Card', ['18185787861'])]

    rr.string = '我的身份证是：52212119950530704x'
    print(rr.select('ID_CARD'))  # ['52212119950530704x']
```
***
[1]: https://blog.jtyoui.com