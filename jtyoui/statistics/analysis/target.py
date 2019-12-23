#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/6 10:24
# @Author: Jtyoui@qq.com

"""统计指标：混淆矩阵
True Positive(真正，TP)：将正类预测为正类数
True Negative(真负，TN)：将负类预测为负类数
False Positive(假正，FP)：将负类预测为正类数
False Negative(假负，FN)：将正类预测为负类数
P=TP+FP 预测对的
N=FN+TN 预测错的
PP=TP+FN 实际上是对的
NN=FP+TN 实际上是错误的
ALL=P+N=PP+NN=所有
"""


def confusion_matrix(simple, pred):
    """混淆矩阵

    :param simple: 实际样本分类列表
    :param pred: 预测样本分类列表
    :return: TP,TN,FP,FN
    """
    tp, tn, fp, fn = 0, 0, 0, 0
    for s, p in zip(simple, pred):
        if s == p == 1:  # 将正类预测为正类数
            tp += 1
        elif s == p == 0:  # 将负类预测为负类数
            tn += 1
        elif s == 1 and p == 0:  # 将正类预测为负类数
            fn += 1
        else:  # 将负类预测为正类数
            fp += 1
    return tp, tn, fp, fn


def precision(tp, tn, fp, fn):
    """精确率=(TP+TN)/(TP+TN+FP+FN)"""
    return (tp + tn) / (tp + tn + fp + fn)


def recall(tp, tn, fp, fn):
    """召回率=TP/(TP+FN)"""
    return tp / (tp + fn)


def f_measure(tp, tn, fp, fn):
    """综合评价指标=(2*P*R)/(P+R)"""
    p = precision(tp, tn, fp, fn)
    r = recall(tp, tn, fp, fn)
    return (2 * p * r) / (p + r)


if __name__ == '__main__':
    simples = [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]  # 实际分类的值
    prediction = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]  # 预测分类的值
    m = confusion_matrix(simple=simples, pred=prediction)  # 混淆矩阵
    p_ = precision(*m)  # 准确率
    r_ = recall(*m)  # 召回率
    f_ = f_measure(*m)  # f值
    print(p_, r_, f_)  # 0.6 0.75 0.6666666666666665
