# **Tools** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 这是一个工具模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/工具-Tools-black.svg)]()


#### 安装
    pip install jtyoui


### 使用
```python
from jtyoui.tools import *
if __name__ == '__main__':
    s = index_select_string('01056666600000056', '我家在贵州省遵义县的一个地方是虾子', '56+')
    print(s)
# ['贵州省遵义县', '虾子']
```

***
[1]: https://blog.jtyoui.com