#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/1 15:53
# @Author: Jtyoui@qq.com
import copy


def get_vocab(path, tags):
    data, label, vocab = [], [], {}
    # <PAD>：0, <UNK>：1, <END>：2
    i = 3
    with open(path, encoding='utf-8') as fp:
        ds, ls = [], []
        for line in fp:
            line = line.strip()
            if line:
                k, v = line.split()
                if k not in vocab:
                    vocab[k] = i
                    i += 1
                ds.append(vocab[k])
                ls.append([tags[v]])
            else:
                data.append(copy.deepcopy(ds + [2]))
                label.append(copy.deepcopy(ls + [2]))
                ds, ls = [], []

    return data, label, vocab


if __name__ == '__main__':
    tag = {'O': 0,
           'B-a': 1, 'I-a': 2,
           'B-b': 3, 'I-b': 4,
           'B-c': 5, 'I-c': 6
           }
    train, test, vocabs = get_vocab(r'train.txt', tag)
