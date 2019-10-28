#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/10/28 15:27
# @Author: Jtyoui@qq.com


class Tree:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.node = []
        self.parent = parent

    def add_child(self, node):
        self.node.append(node)


def dict_create_tree(data: dict, tree: Tree = Tree(value='Root')):
    """创建下面的树结构
                a
            b   c   d
        e f g |g h| k m
    :param data: 创建树型结构，对照上面，例如：ds = {'a': {'b': ['e', 'f', 'g'], 'c': ['g', 'h'], 'd': ['k', 'm']}}
    :param tree: 默认为上一层树结构，不需要传入
    :return: 一颗自动带有root根目录的树结构
    """
    for d in data:
        t = Tree(value=d, parent=tree)
        tree.add_child(t)
        if isinstance(data, dict):
            dict_create_tree(data[d], t)
    return tree


def search_tree(tree: Tree, value: str, ls):
    """多叉搜索树
    :param tree:一颗多叉树
    :param value: 树上一个值
    :param ls:树集合
    :return: 返回树集合，ls
    """
    if value in tree.value:
        ls.append(tree)
    else:
        for t in tree.node:
            search_tree(t, value, ls)


def search_tree_value(tree: Tree, value: str):
    """搜索树的路径
    :param tree:一颗树
    :param value:树上的一个值
    :return:树支的路径
    """
    ls = []
    search_tree(tree, value, ls)
    for trees in ls:
        values = []
        while trees.parent is not None:
            values.append(trees.value)
            trees = trees.parent
        yield '-'.join(reversed(values))


if __name__ == '__main__':
    """创建下面的树结构
            a
        b   c   d
    e f g |g h| k m
    """
    print('----------------------创建树-------------------------------')
    ds = {'a': {'b': ['e', 'f', 'g'], 'c': ['g', 'h'], 'd': ['k', 'm']}}
    ts = dict_create_tree(ds)
    print(ts)

    print('--------------------搜索树对象---------------------------------')
    tree_object = []
    search_tree(ts, 'g', tree_object)
    print(tree_object)

    print('-----------------------搜索树的路径-------------------------')
    for i in search_tree_value(ts, 'g'):
        print(i)
