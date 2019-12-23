#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/21 14:59
# @Author: Jtyoui@qq.com
from jtyoui.decorators import parameter_set_length

"""
平均值,中位数,众数,分位数,极差,方差,标准差,偏度,峰度
"""


class AnalysisMath:

    def __init__(self, data=()):
        if not isinstance(data, (set, list, tuple)):
            raise TypeError("传入一个可替代对象.比如list,set,tuple类型")
        self.__data = data
        self.__length = len(data)

    def average(self, flag=0):
        """平均数

        flag=0 算术平均值
        flag=1 几何平均值
        flag=2 平方平均值(均方根)
        flag=3 调和平均值

        :param flag: 根据不同的数值,进行不同的平均值
        """
        if flag == 0:
            return sum(self.__data) / self.__length
        elif flag == 1:
            all_ = 1
            for data in self.__data:
                all_ *= abs(data)
            return pow(all_, self.__length)
        elif flag == 2:
            all_ = [data ** 2 for data in self.__data]
            return pow(sum(all_) / self.__length, 0.5)
        elif flag == 3:
            all_ = [1 / data for data in self.__data]
            return self.__length / sum(all_)

    def expect(self, data=None):
        """数学期望"""
        if data:
            self.__init__(data)
        return self.average(0)

    @property
    def median(self):
        """中位数"""
        return self.quantile(2)

    @property
    def mode_number(self):
        """众数"""
        data = {}
        for d in self.__data:
            data[d] = data.get(d, 0) + 1
        max_ = sorted(data.items(), key=lambda x: x[1], reverse=True)
        return max_[0][0]

    def quantile(self, position=1):
        """分位数

        position=1: 第一四分位数 (Q1)，又称“较小四分位数”，等于该样本中所有数值由小到大排列后第25%的数字。
        position=2: 第二四分位数 (Q2)，又称“中位数”，等于该样本中所有数值由小到大排列后第50%的数字。
        position=3: 第三四分位数 (Q3)，又称“较大四分位数”，等于该样本中所有数值由小到大排列后第75%的数字。

        :param position: 根据不同的数值计算不同的分位数
        """
        if position > 3:
            raise ValueError("position的取值范围是[1,2,3]整数")

        data = sorted(self.__data)
        middle, mod = divmod(self.__length * position, 4)
        if mod == 0:
            return (data[middle - 1] + data[middle]) / 2
        else:
            return data[middle]

    @property
    def range(self):
        """极差"""
        return max(self.__data) - min(self.__data)

    def variance(self, data=None):
        """方差"""
        if data:
            self.__init__(data)
        average = self.average(0)
        all_ = [(data - average) ** 2 for data in self.__data]
        return sum(all_) / self.__length

    def standard(self, data=None):
        """标准差"""
        if data:
            self.__init__(data)
        return pow(self.variance(), 0.5)

    @property
    def skewness(self):
        """偏度(偏态系数)"""
        x_3 = [data ** 3 for data in self.__data]
        x_2 = [data ** 2 for data in self.__data]

        expect_1 = self.average(0)  # x的数学期望
        expect_3 = sum(x_3) / self.__length  # x**3的数学期望
        expect_2 = sum(x_2) / self.__length  # x**2的数学期望

        numerator = expect_3 - 3 * expect_1 * (expect_2 - expect_1 ** 2) - expect_1 ** 3  # 分子
        denominator = pow(expect_2 - expect_1 ** 2, 1.5)  # 分母
        return numerator / denominator

    @property
    def kurtosis(self):
        """峰度

        如果超值峰度为正，称为尖峰态
        如果超值峰度为负，称为低峰态
        """
        average = self.average(0)  # 数学期望
        all_4 = [(data - average) ** 4 for data in self.__data]
        numerator = sum(all_4) / self.__length  # 四阶样本中心矩

        denominator = self.standard() ** 4  # 标准差**4

        return numerator / denominator - 3  # 通常将峰度值做减3处理，使得正态分布的峰度0


@parameter_set_length
def cov(x, y):
    """协方差

    :return: 表示x的数学期望
    """
    if isinstance(x, (set, list, tuple)) and isinstance(y, (set, list, tuple)):
        ana = AnalysisMath()
        expect_x = ana.expect(x)
        expect_y = ana.expect(y)
        xy = [x_ * y_ for x_, y_ in zip(x, y)]
        expect_xy = ana.expect(xy)
        return expect_xy - expect_x * expect_y
    else:
        raise TypeError("x,y类型必须满足其中一个(set, list, tuple)")


if __name__ == '__main__':
    analysis = AnalysisMath(data=[1, 2, 3, 5, 7, 2, 4, 2, 8, 9])
    print(analysis.average(3))
    print(analysis.median)
    print(analysis.mode_number)
    print(analysis.quantile(2))
    print(analysis.range)
    print(analysis.variance())
    print(analysis.standard())
    print(analysis.skewness)
    print(analysis.kurtosis)
