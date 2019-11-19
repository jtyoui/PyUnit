# **Reptile** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 爬虫模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/爬虫-Reptile-black.svg)]()


### 安装
    pip install jtyoui

### 爬取双色球数据
```python
from jtyoui.reptile import double_data_chart
if __name__ == '__main__':
    # 从2003年2月23日开始爬到现在
    print(double_data_chart(1000, 19131))

    """
    [['期号' '红球1' '红球2' ... '二等奖奖金' '总投注额' '开奖日期']
    ['19131' '9' '17' ... '150488' '413548024' '2019-11-14']
    ['19130' '1' '7' ... '222487' '418172282' '2019-11-12']
    ...
    ['3003' '1' '7' ... '332369' '8917960' '2003-03-02']
    ['3002' '4' '9' ... '264332' '7398870' '2003-02-27']
    ['3001' '10' '11' ... '898744' '10307806' '2003-02-23']]
    """
```


***
[1]: https://blog.jtyoui.com