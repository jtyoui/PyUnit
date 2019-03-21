# **Similarity** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 距离模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui.statistics-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/文本相似度-Similarity-black.svg)]()

### 安装
    pip install jtyoui

#### 模块介绍
```python
from jtyoui.statistics import chebyshev_distance  # 切比雪夫距离
from jtyoui.statistics import cosine_distance  # 余弦距离
from jtyoui.statistics import edit_distance  # 编辑距离
from jtyoui.statistics import euclidean_distance  # 欧氏距离
from jtyoui.statistics import ham_distance  # 海明距离
from jtyoui.statistics import mahalanobis_distance  # 马氏距离
from jtyoui.statistics import manhattan_distance  # 曼哈顿距离
from jtyoui.statistics import minkowski_distance  # 闵可夫斯基距离
from jtyoui.statistics import jaccard_set_distance, jaccard_distance  # 杰卡德距离
from jtyoui.statistics import bray_curtis_distance  # 布雷柯蒂斯距离

point_x=[1,2,4,5]#定义一个四维的坐标点
point_y=[3,5,6,7]#定义一个四维的坐标点


"""
切比雪夫距离(棋盘距离)
在数学中，切比雪夫距离或是L∞度量，是向量空间中的一种度量，
二个点之间的距离定义是其各坐标数值差绝对值的最大值。以数学的观点来看，切比雪夫距离是由一致范数（uniform norm）
所衍生的度量，也是超凸度量的一种。
国际象棋中，国王可以直行、横行、斜行，所以国王走一步可以移动到相邻8个方格中的任意一个。
国王从格子(x1,y1)走到格子(x2,y2)最少需要多少步？这个距离就叫切比雪夫距离。
"""
value=chebyshev_distance(point_x,point_y)
print(value)


"""
余弦距离
几何中，夹角余弦可用来衡量两个向量方向的差异；
机器学习中，借用这一概念来衡量样本向量之间的差异。
余弦相似度用向量空间中两个向量夹角的余弦值作为衡量两个个体间差异的大小。
相比距离度量，余弦相似度更加注重两个向量在方向上的差异，而非距离或长度上
"""
value=cosine_distance(point_x,point_y)
print(value)


"""
编辑距离
编辑距离又称Levenshtein距离，是指两个字串之间，由一个转成另一个所需的最少编辑操作次数。
许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。一般来说，
编辑距离越小，两个串的相似度越大。
"""
value=edit_distance('我吃饭了', '我正在吃饭')
print(value)


"""
欧氏距离
欧氏距离是最容易直观理解的距离度量方法，
我们小学、初中和高中接触到的两个点在空间中的距离一般都是指欧氏距离。
"""
value=euclidean_distance(point_x,point_y)
print(value)


"""
海明距离
在信息编码中，两个合法代码对应位上编码不同的位数称为码距，又称海明距离。
举例如下：10101和00110从第一位开始依次有第一位、第四、第五位不同，则海明距离为3。
"""
value=ham_distance('我吃饭了,明天去看电影', '我在吃饭了,马上去看电影', weight={"电影": 3})
print(value)



"""
马氏距离
马氏距离是由印度统计学家马哈拉诺比斯提出的，
表示数据的协方差距离。它是一种有效的计算两个未知样本集的相似度的方法。与欧氏距离不同的是，
它考虑到各种特性之间的联系（例如：一条关于身高的信息会带来一条关于体重的信息，因为两者是有关联的），
并且是尺度无关的(scale-invariant)，即独立于测量尺度。对于一个均值为μ，协方差矩阵为Σ的多变量向量，
其马氏距离为sqrt( (x-μ)'Σ^(-1)(x-μ) )。
"""
value=mahalanobis_distance(point_x,point_y)
print(value)


"""
曼哈顿距离
顾名思义，在曼哈顿街区要从一个十字路口开车到另一个十字路口
，驾驶距离显然不是两点间的直线距离。这个实际驾驶距离就是“曼哈顿距离”。
曼哈顿距离也称为“城市街区距离”(City Block distance)。
"""
value=manhattan_distance(point_x,point_y)
print(value)


"""
闵可夫斯基距离
闵氏空间指狭义相对论中由一个时间维和三个空间维组成的时空，
为俄裔德国数学家闵可夫斯基(1864-1909)最先表述。
他的平坦空间的概念以及表示为特殊距离量的几何学是与狭义相对论的要求相一致的。
闵可夫斯基空间不同于牛顿力学的平坦空间
当dimension=1时，得到绝对值距离，也叫曼哈顿距离
当dimension=2时，得到欧几里德距离
令dimension=无穷大(math.inf)，得到切比雪夫距离
"""
value=minkowski_distance(point_x,point_y, 3)
print(value)


"""
杰卡德距离
杰卡德距离是用来衡量两个集合差异性的一种指标，它是杰卡德相似系数的补集，
被定义为1减去杰卡德相似系数。而杰卡德相似系数，
也称杰卡德指数,是用来衡量两个集合相似度的一种指标
"""
value=jaccard_distance([0, 1, 1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1, 1, 0, 0])
print(value)
value=jaccard_set_distance({1, 10, 31, 2, 13, 26, 43}, {21, 52, 31, 43, 6, 12, 31})
print(value)



"""
布雷柯蒂斯距离
Bray Curtis距离主要用于生态学和环境科学，计算坐标之间的距离。
该距离取值在[0,1]之间。它也可以用来计算样本之间的差异。
"""
value=bray_curtis_distance(point_x,point_y)
print(value)

```

***
[1]: https://blog.jtyoui.statistics.com