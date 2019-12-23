#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/18 9:32
# @Author: Jtyoui@qq.com
from .ChebyshevDistance import chebyshev_distance  # 切比雪夫距离
from .CosineDistance import cosine_distance, cosine  # 余弦距离
from .EditDistance import edit_distance  # 编辑距离
from .EuclideanDistance import euclidean_distance  # 欧氏距离
from .HammingDistance import ham_distance, simHash_similarity  # 海明距离
from .MahalanobisDistance import mahalanobis_distance  # 马氏距离
from .ManhattanDistance import manhattan_distance  # 曼哈顿距离
from .MinkowskiDistance import minkowski_distance  # 闵可夫斯基距离
from .JaccardDistance import jaccard_set_distance, jaccard_distance  # 杰卡德距离
from .BrayCurtisDistance import bray_curtis_distance  # 布雷柯蒂斯距离
