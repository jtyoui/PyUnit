#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/13 10:55
# @Author: Jtyoui@qq.com
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor

"""
KNN分类算法例子
"""


def knn_class_fit(train, label):
    """训练数据模型"""
    binary = LabelBinarizer()  # 二值化
    y_ = binary.fit_transform(label)
    clf = KNeighborsClassifier()
    clf.fit(train, np.ravel(y_))
    return clf, binary


def knn_class_predict(models, predict_value):
    """预测模型"""
    predict = models[0].predict(predict_value)
    return models[1].inverse_transform(predict)


def knn_regress_fit(train, label):
    clf = KNeighborsRegressor()
    clf.fit(train, label)
    return clf


def knn_regress_predict(models, predict_value):
    return models.predict(predict_value)


if __name__ == '__main__':
    # 身高和体重去预测性别
    x = np.array([
        [156, 64],
        [170, 86],
        [183, 84],
        [191, 80],
        [155, 49],
        [163, 59],
        [180, 67],
        [158, 54],
        [170, 67]
    ])
    y = np.array(['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female'])
    test = np.array([[155, 70]])

    model = knn_class_fit(x, y)
    print(knn_class_predict(model, test))  # 预测：['female']，正确：['female']

if __name__ == '__main__':
    # 利用身高和性别来预测体重
    x = np.array([
        [158, 1],
        [170, 1],
        [183, 1],
        [191, 1],
        [155, 0],
        [163, 0],
        [180, 0],
        [158, 0],
        [170, 0],
        [168, 1],
        [180, 1],
        [160, 0]
    ])
    y = np.array([64, 86, 84, 80, 49, 59, 67, 54, 67, 65, 96, 52])
    test = np.array([[169, 0]])

    model = knn_regress_fit(x, y)
    print(knn_regress_predict(model, test))  # 预测：[65.8]，正确：[67]
