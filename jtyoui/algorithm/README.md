# **Algorithm** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 算法模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/算法-algorithm-black.svg)]()


### 安装
    pip install jtyoui



## 二分搜索
```python
from jtyoui.algorithm import binary_search
if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6, 10, 7]
    print(binary_search(s, 7, True))
```

## 分词匹配
```python
from jtyoui.algorithm import RMMA,FMMA
if __name__ == '__main__':
    r = RMMA(ls=['我们', '野生', '动物园'], sort=True) # 逆向最大匹配算法
    print(r.cut('我们在野生动物园玩', 3)) #['我们', '在', '野生', '动物园', '玩']
    print('-----------------------------------------')
    r = FMMA(ls=['我们', '野生', '动物园'], sort=True) # 正向最大匹配算法
    print(r.cut('我们在野生动物园玩', 3)) #['我们', '在', '野生', '动物园', '玩']
```

## 字符串匹配(KMP算法)
```python
from jtyoui.algorithm import kmp
if __name__ == '__main__':
   print(kmp('我们在野生动物园玩', '动物园')) # 5
```

## 映射替换
```python
from jtyoui.algorithm import map_replace
if __name__ == '__main__':
    print(map_replace('[中国]', '[]', '【】'))
    print(map_replace('[中国]', maps={'[': '【', ']': '】'}))
    # 【中国】
```

## 创建树
```python
from jtyoui.algorithm import dict_create_tree

if __name__ == '__main__':
    """创建下面的树结构
            a
        b   c   d
    e f g |g h| k m
    """
    print('----------------------创建树-------------------------------')
    ds = {'a': {'b': ['e', 'f', 'g'], 'c': ['g', 'h'], 'd': ['k', 'm']}}
    ts = dict_create_tree(ds)
    print(ts)

    print('--------------------搜索树对象---------------------------------')
    tree_object = []
    ts.search_tree('g', tree_object)
    print(tree_object)

    print('-----------------------搜索树的路径-------------------------')
    for i in ts.search_tree_value('g'):
        print(i)

```




***
[1]: https://blog.jtyoui.com