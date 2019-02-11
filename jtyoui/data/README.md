# **Data** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 这是一个数据集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-数据-black.svg)]()


#### 安装
    pip install jtyoui

### 使用
```python
from jtyoui.data import *
if __name__ == '__main__':
    download_gitee('logo', 'logo.png', address='D:\\')  # 将照片logo.png下载到D盘
    pillow = fetch_gitee('logo', 'logo.png', pil=True)  # 返回PIL.image类型数据
```


***
[1]: https://blog.jtyoui.com