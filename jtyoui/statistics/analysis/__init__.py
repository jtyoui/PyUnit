#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/21 14:59
# @Author: Jtyoui@qq.com

"""
平均值,中位数,众数,分位数,极差,方差,标准差,偏度,峰度
"""


class AnalysisMath:

    def __init__(self, data):
        if not isinstance(data, (set, list, tuple)):
            raise TypeError("传入一个可替代对象.比如list,set,tuple类型")
        self.data = data
        self.length = len(data)

    def average(self, flag=0):
        """平均数"""
        """
        flag=0 算术平均值
        flag=1 几何平均值
        flag=2 平方平均值(均方根)
        flag=3 调和平均值
        :param flag:根据不同的数值,进行不同的平均值
        """
        if flag == 0:
            return sum(self.data) / self.length
        elif flag == 1:
            all_ = 1
            for data in self.data:
                all_ *= abs(data)
            return pow(all_, self.length)
        elif flag == 2:
            all_ = [data ** 2 for data in self.data]
            return pow(sum(all_) / self.length, 0.5)
        elif flag == 3:
            all_ = [1 / data for data in self.data]
            return self.length / sum(all_)

    def median(self):
        """中位数"""
        return self.quantile(2)

    def mode_number(self):
        """众数"""
        data = {}
        for d in self.data:
            data[d] = data.get(d, 0) + 1
        max_ = sorted(data.items(), key=lambda x: x[1], reverse=True)
        return max_[0][0]

    def quantile(self, position=1):
        """分位数"""
        """
        position=1: 第一四分位数 (Q1)，又称“较小四分位数”，等于该样本中所有数值由小到大排列后第25%的数字。
        position=2: 第二四分位数 (Q2)，又称“中位数”，等于该样本中所有数值由小到大排列后第50%的数字。
        position=3: 第三四分位数 (Q3)，又称“较大四分位数”，等于该样本中所有数值由小到大排列后第75%的数字。
        :param position:根据不同的数值计算不同的分位数
        """
        if position > 3:
            raise ValueError("position的取值范围是[1,2,3]整数")

        data = sorted(self.data)
        middle, mod = divmod(self.length * position, 4)
        if mod == 0:
            return (data[middle - 1] + data[middle]) / 2
        else:
            return data[middle]

    def range(self):
        """极差"""
        return max(self.data) - min(self.data)

    def variance(self):
        """方差"""
        average = self.average(0)
        all_ = [(data - average) ** 2 for data in self.data]
        return sum(all_) / self.length

    def standard(self):
        """标准差"""
        return pow(self.variance(), 0.5)

    def skewness(self):
        """偏度(偏态系数)"""
        x_3 = [data ** 3 for data in self.data]
        x_2 = [data ** 2 for data in self.data]

        expect_1 = self.average(0)  # x的数学期望
        expect_3 = sum(x_3) / self.length  # x**3的数学期望
        expect_2 = sum(x_2) / self.length  # x**2的数学期望

        numerator = expect_3 - 3 * expect_1 * (expect_2 - expect_1 ** 2) - expect_1 ** 3  # 分子
        denominator = pow(expect_2 - expect_1 ** 2, 1.5)  # 分母
        return numerator / denominator

    def kurtosis(self):
        """峰度"""
        """
        如果超值峰度为正，称为尖峰态
        如果超值峰度为负，称为低峰态
        """
        average = self.average(0)  # 数学期望
        all_4 = [(data - average) ** 4 for data in self.data]
        numerator = sum(all_4) / self.length  # 四阶样本中心矩

        denominator = self.standard() ** 4  # 标准差**4

        return numerator / denominator - 3  # 通常将峰度值做减3处理，使得正态分布的峰度0


if __name__ == '__main__':
    analysis = AnalysisMath(data=[1, 2, 3, 5, 7, 2, 4, 2, 8, 9])
    print(analysis.average(3))
    print(analysis.median())
    print(analysis.mode_number())
    print(analysis.quantile(2))
    print(analysis.range())
    print(analysis.variance())
    print(analysis.standard())
    print(analysis.skewness())
    print(analysis.kurtosis())
