#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/23 16:33
# @Author: Jtyoui@qq.com


class BayesProbability:
    """贝叶斯

    >>> bp = BayesProbability()
    >>> bp['bowl_one'] = 1 / 2
    >>> bp['bowl_two'] = 1 / 2
    >>> bp.prior_probability('bowl_one', 3 / 4)
    >>> bp.prior_probability('bowl_two', 1 / 2)
    >>> print(bp.posterior_probability('bowl_one'))
    """

    def __init__(self):
        self.name_prob = dict()
        self.name_prior_prob = dict()

    def __setitem__(self, name, prob):
        """初始化name的概率

        :param name: 名字
        :param prob: 独立概率
        """
        self.name_prob.setdefault(name, prob)

    def prior_probability(self, name, prob):
        """先验概率

        :param name: 名字
        :param prob: 先验概率
        """
        self.name_prior_prob[name] = prob

    def posterior_probability(self, name):
        """后验概率"""
        h = 0
        for _, prob in self.name_prior_prob.items():
            h += prob
        h /= len(self.name_prior_prob)
        return (self.name_prob[name] * self.name_prior_prob[name]) / h


if __name__ == '__main__':
    bp = BayesProbability()
    bp['bowl_one'] = 1 / 2
    bp['bowl_two'] = 1 / 2
    bp.prior_probability('bowl_one', 3 / 4)
    bp.prior_probability('bowl_two', 1 / 2)
    print(bp.posterior_probability('bowl_one'))
