# **Analysis** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 数学分析统计模块
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/分析-analysis-black.svg)]()


#### 安装
    pip install jtyoui

#### 使用
```python
import jtyoui

if __name__ == '__main__':
    """
    平均值,中位数,众数,分位数,极差,方差,标准差,偏度,峰度
    """
    analysis = jtyoui.AnalysisMath(data=[1, 2, 3, 5, 7, 2, 4, 2, 8, 9])
    print(analysis.average(3)) # 平均值  2.7305233503088093
    print(analysis.median) # 中位数   3.5
    print(analysis.mode_number) # 众数  2
    print(analysis.quantile(2)) # 分位数  3.5
    print(analysis.range)# 极差   8
    print(analysis.variance()) # 方差 7.209999999999999
    print(analysis.standard()) # 标准差 2.6851443164195103
    print(analysis.skewness) # 偏度  0.5157053955946609
    print(analysis.kurtosis)  # 峰度   -1.2029562885574623
    
```

## 统计分类指标
```python
from jtyoui.statistics import confusion_matrix,precision,recall,f_measure
if __name__ == '__main__':
    simples = [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]  # 实际分类的值
    prediction = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]  # 预测分类的值
    m = confusion_matrix(simple=simples, pred=prediction)  # 混淆矩阵
    p_ = precision(*m)  # 准确率
    r_ = recall(*m)  # 召回率
    f_ = f_measure(*m)  # f值
    print(p_, r_, f_)  # 0.6 0.75 0.6666666666666665

```

## 矩阵的四则运算
```python
from jtyoui.statistics.analysis import Matrix
if __name__ == '__main__':
    d = [
        [1, 2, 3],
        [1, 0, -1],
        [0, 1, 1]
    ]
    m1 = Matrix(d)
    m2 = Matrix(d)
    print(m1 * m2)
    print(m1 + m2)
    print(m1 - m2)
```

***
[1]: https://blog.jtyoui.com