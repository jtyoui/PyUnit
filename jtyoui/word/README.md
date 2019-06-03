# **Neologism** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]


## 这是一个无监督训练文本词库与分词
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()

## 安装
    pip install jtyoui

## 训练代码(文本是UTF-8格式)
```python
from jtyoui.word import analysis_single,thread_analysis
if __name__ == '__main__':
    neologism_words = analysis_single(file_str='小时代.txt') #单线程
    # neologism=thread_analysis(file='小时代.txt') #多线程,不建议使用
    for k, v in neologism_words.items():
        print('key:{0} count:{1} frequency:{2} cond:{3} free:{4}'.format(k, v[0], v[1], v[2], v[3]))
```
    


## 接口参数(也废除)
    def analysis(file, thread_num=10, split_num=4, frequency=0.0001, cond=10, free=0.1, flag=False)
       """
    :param file: 训练的文本
    :param thread_num: 线程数
    :param split_num: 匹配个数
    :param frequency: 频率
    :param cond: 凝聚度
    :param free: 自由度
    :param flag:是否是并且还是或者,默认是或者，满足一个就过滤
    :return: 分析完毕的字典
    """
    
   
![](https://gitee.com/tyoui/logo/raw/master/photo/snsg1.png)


## 爬虫的新闻数据一部分截图（大概100M纯文本）
![](https://gitee.com/tyoui/logo/raw/master/photo/snsg2.png)
       
## 训练政治新闻后的结果
![](https://gitee.com/tyoui/logo/raw/master/photo/snsg.png)


[1]: https://blog.jtyoui.com