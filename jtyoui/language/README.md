# **Language** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 处理语言的模块
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-语言-black.svg)]()


#### 安装
    pip install jtyoui

#### 处理汉语中的简体字与繁体字
```python
from jtyoui.language import han
if __name__ == '__main__':
    j = han.j_to_f('千载正字一夕改,如今吾辈来重光!')
    print(''.join(j))
    f = han.f_to_j('千載正字一夕改,如今吾輩來重光!')
    print(''.join(f))
```
***
[1]: https://blog.jtyoui.com