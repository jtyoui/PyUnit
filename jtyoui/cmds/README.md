# **CMD** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## CMD/Shell命令模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/命令-CMD-black.svg)]()


## 安装
    pip install jtyoui

### 高级隐藏window系统下的文件夹或者文件
```python
from jtyoui.cmds import hide_file,display_file
if __name__ == '__main__':
    print(hide_file(r'D:/1/2.txt')) #隐藏
    print(display_file(r'D:/1/2.txt'))#显示
```

### 获取MAC、IP等信息
```python
from jtyoui.cmds import get_mac_address,get_window_ip,get_linux_ip
if __name__ == '__main__':
    print(get_mac_address()) #获取window下的MAC地址
    print(get_window_ip())#获取window下的ip地址
    print(get_linux_ip('ens192'))#获取Linux下的IP地址
```

### 获取window系统名
```python
from jtyoui.cmds import get_window_name
if __name__ == '__main__':
    print(get_window_name())
```

***
[1]: https://blog.jtyoui.com