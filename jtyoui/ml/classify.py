#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/13 17:48
# @Author: Jtyoui@qq.com
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

"""
三种分类算法示意图展示
"""

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

x, y = load_breast_cancer(return_X_y=True)
length = len(x) - 100
print(x)
print(y)
lr_scores, nb_scores, knn_scores = [], [], []
sizes = range(100, length, 30)
for size in sizes:
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=size, random_state=31)
    print(len(x_train), size)
    lr = LogisticRegression()
    lr.fit(x_train, y_train)
    lr_score = lr.score(x_test, y_test)
    lr_scores.append(lr_score)

    nb = GaussianNB()
    nb.fit(x_train, y_train)
    nb_score = nb.score(x_test, y_test)
    nb_scores.append(nb_score)

    knn = KNeighborsClassifier()
    knn.fit(x_train, y_train)
    knn_score = knn.score(x_test, y_test)
    knn_scores.append(knn_score)

plt.plot(sizes, lr_scores, label='逻辑回归', linestyle='--')

plt.plot(sizes, nb_scores, label='朴素贝叶斯', linestyle=':')

plt.plot(sizes, knn_scores, label='KNN近邻')

plt.xlabel('训练的数据量')
plt.ylabel('预测的准确度')
plt.legend()
plt.show()
