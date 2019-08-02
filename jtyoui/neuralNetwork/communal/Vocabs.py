#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/1 15:53
# @Author: Jtyoui@qq.com
from collections import Counter
import json


# 没有在vocab是1
# 填充是0
# 结尾符是2
def read_test(path):
    vocab = json.load(fp=open('./vocab.json'))
    test = []
    with open(path) as fp:
        for line in fp:
            lines = line.strip().split('_')
            m = map(lambda x: vocab.get(x, 1), lines)
            test.append(list(m))
    return test


def read_train(tag, path):
    train = []
    test = []
    with open(path) as fp:
        data = fp.read().split('\n\n')[:-1]
        vocab = json.load(fp=open('./vocab.json'))
        for ds in data:
            d, t = [], []
            lines = ds.split('\n')
            for line in lines:
                k, v = line.split('\t')
                d.append(vocab.get(k, 1))
                t.append([tag[v]])
            train.append(d)
            test.append(t)
    return train, test


def get_vocab(path):
    v = []
    with open(path) as fp:
        for line in fp:
            data = line.strip().split('_')
            v.extend(data)
    c = Counter(v)
    f = filter(lambda x: x[1] >= 10, c.items())
    s = sorted(f, key=lambda x: x[1], reverse=True)
    vocab = {}
    for index, (k, _) in enumerate(s, start=3):
        vocab[k] = index
    json.dump(vocab, fp=open('./vocab.json', 'w'))
    return vocab


if __name__ == '__main__':
    get_vocab(path=None)
    tags = {'O': 0,
            'B-a': 1, 'I-a': 2,
            'B-b': 3, 'I-b': 4,
            'B-c': 5, 'I-c': 6
            }
    trains, tests = read_train(tags, path=None)
    print(trains)
    print(tests)
    print(read_test(path=None))
