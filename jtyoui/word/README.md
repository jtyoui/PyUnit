# **Neologism** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]


## 这是一个无监督训练文本词库与分词
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()

## 安装
    pip install jtyoui

## 训练代码(文本是UTF-8格式)
```python
from jtyoui.word import Neologism
if __name__ == '__main__':
    n = Neologism()
    n.read_file(r'D:\data.txt', 6)
    n.statistics()
    n.handle()
    for k, v in n.filter_words(count=10, frequency=0.0001, cond=84, free=0.7):
        print(F'关键字:{k} 次数:{v[0]} 频率:{v[1]} 凝聚度:{v[2]} 自由度:{v[3]}')

```

![](https://gitee.com/tyoui/logo/raw/master/photo/snsg1.png)


## 爬虫的新闻数据一部分截图（大概100M纯文本）
![](https://gitee.com/tyoui/logo/raw/master/photo/snsg2.png)
       
## 训练政治新闻后的结果
![](https://gitee.com/tyoui/logo/raw/master/photo/snsg.png)

## 摘要算法
```python
from jtyoui.word import TextSummary
if __name__ == '__main__':
    data = """6月17日22时55分，四川长宁县发生6.0级地震，震源深度16千米。地震发生两个小时后，离震中较近的四川省宜宾市珙县
    巡场镇宜宾市矿山急救医院迎来第一个新生儿。医生在余震和医院房屋出现损毁的情况下顶住压力和风险，为产妇接生，母子平安。"""
    ts = TextSummary(data, title='长宁县地震')
    print(ts.calc_summary())
    # ['6月17日22时55分，四川长宁县发生6.0级地震，震源深度16千米。']
```

[1]: https://blog.jtyoui.com