# **Decorator** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 常见的装饰器模块
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/Decorator-装饰器-black.svg)]()


#### 安装
    pip install jtyoui


#### 使用
```python

from jtyoui.regular import Non_Chinese
from jtyoui.decorators import replace_regular,parameter_set_length


@replace_regular(' ', '')
def remove_blank(a, b):
    print(a, b)


@replace_regular(Non_Chinese, '')
def remove_non_chinese(a, b):
    print(a, b)

@parameter_set_length
def set_length(x,y):
    print(x,y)

if __name__ == '__main__':
    remove_blank('你好  吗?', b='我  很好!')
    remove_non_chinese('你好#$%76#%吗wore?', b='我$%^787word很好!')
    set_length(x=[3,4],y=[1,2])
```

### 单身模式修饰器
```python
from jtyoui.decorators import singleton

@singleton
class A:
    pass
    
if __name__ == '__main__':
    a = A()
    b = A()
    print(id(a) == id(b))  # True
```

### 自动激活协程装饰器
```python
from jtyoui.decorators import coroutine
if __name__ == '__main__':
    @coroutine
    def receiver():
        n = 0
        while True:
            n = yield n + n
    
    
    print(receiver().send(10))
```

### 警告装饰器
```python
from jtyoui.decorators import warns
if __name__ == '__main__':
    @warns('该函数已废弃!',DeprecationWarning)
    def w(): ...

    w()
```


***
[1]: https://blog.jtyoui.com