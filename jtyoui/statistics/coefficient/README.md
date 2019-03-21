# **Coefficient** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 相关系数模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/相关系数-coefficient-black.svg)]()


#### 安装
    pip install jtyoui

#### 使用
```python
from jtyoui import pearson_coefficient  # 皮尔森相关性系数
from jtyoui import spear_man_coefficient  # 斯皮尔曼相关系数
from jtyoui import kendall_coefficient  # 肯德尔相关性系数

x,y=[1, 2, 3, 4, 5, 6], [0.3, 0.9, 2.7, 2, 3.5, 5]

"""
皮尔森相关性系数
Pearson相关系数是用来衡量两个数据集合是否在一条线上面，它用来衡量定距变量间的线性关系。
相关系数 0.8-1.0 极强相关
0.6-0.8 强相关
0.4-0.6 中等程度相关
0.2-0.4 弱相关
0.0-0.2 极弱相关或无相关
就好比我们想研究人跑步的速度与心脏跳动的相关性，如果你无论跑多快，
心跳都不变（即心跳这个变量的标准差为0），或者你心跳忽快忽慢的，
却一直保持一个速度在跑（即跑步速度这个变量的标准差为0），
那我们都无法通过皮尔森相关性系数的计算来判断心跳与跑步速度到底相不相关。
"""
value=pearson_coefficient(x,y)
print(value)



"""
斯皮尔曼相关系数
在统计学中, 以查尔斯·斯皮尔曼命名的斯皮尔曼等级相关系数，即SpearMan相关系数。
经常用希腊字母ρ表示。 它是衡量两个变量的依赖性的 非参数 指标。
它利用单调方程评价两个统计变量的相关性。 如果数据中没有重复值，
并且当两个变量完全单调相关时，斯皮尔曼相关系数则为+1或−1。
"""
value=spear_man_coefficient(x,y)
print(value)


"""
肯德尔相关性系数
肯德尔相关系数是以Maurice Kendall命名的，并经常用希腊字母τ（tau）表示其值。
肯德尔相关系数是一个用来测量两个随机变量相关性的统计值。
一个肯德尔检验是一个无参数假设检验，它使用计算而得的相关系数去检验两个随机变量的统计依赖性。
肯德尔相关系数的取值范围在-1到1之间，当τ为1时，表示两个随机变量拥有一致的等级相关性；
当τ为-1时，表示两个随机变量拥有完全相反的等级相关性；当τ为0时，表示两个随机变量是相互独立的

举个例子。比如评委对选手的评分（优、中、差等），我们想看两个（或者多个）评委对几位选手的评价标准是否一致；
或者医院的尿糖化验报告，想检验各个医院对尿糖的化验结果是否一致，这时候就可以使用肯德尔相关性系数进行衡量。
"""
value=kendall_coefficient(x,y)
print(value)

```

#### 参考资料
[相关系数](http://blog.sina.com.cn/s/blog_69e75efd0102wmd2.html)
[肯德尔相关系数](https://blog.csdn.net/wsywl/article/details/5889419)

***
[1]: https://blog.jtyoui.com