#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/4 0:06
# @Author: jtyoui@qq.com
from collections import Counter
import pickle


def analysis_vocab(vocab_path, save_vocab_model_path, frequency=10):
    """根据已知文本统计词向量，取频率大于10的文字，词索引根据频率大小进行排序"""
    v = []
    with open(file=vocab_path) as fp:
        for line in fp:
            data = line.strip().split('_')
            v.extend(data)
    c = Counter(v)
    f = filter(lambda x: x[1] >= frequency, c.items())
    s = sorted(f, key=lambda x: x[1], reverse=True)
    # 填充是0、开始是1、结束是2、掩码是3、未知是UNK
    vocab = {'[PAD]': 0, '[UNK]': 1}
    for index, (k, _) in enumerate(iterable=s, start=len(vocab)):
        vocab[k] = index
    with open(file=save_vocab_model_path, mode='wb') as fp:
        pickle.dump(obj=vocab, file=fp)


def load_vocab(load_vocab_model_path):
    """加载模型"""
    with open(file=load_vocab_model_path, mode='rb') as fp:
        return pickle.load(file=fp)


def vocab_test(test_path, vocab, max_chunk_length):
    test, original = [], []
    with open(test_path)as fp:
        for line in fp:
            line = line.strip().split('_')
            original.append(line)
            m = list(map(lambda x: vocab.get(x, vocab['[UNK]']), line))
            if len(m) <= max_chunk_length:
                data = [vocab['[PAD]']] * (max_chunk_length - len(m)) + m
            else:
                data = m[:max_chunk_length]
            test.append(data)
    return test, original


def analysis_rational_len(train_or_dev_path, percent=0.9):
    """分析文本之间的长度分布，percent表示分布率"""
    length = []
    with open(file=train_or_dev_path)as fp:
        for lines in fp:
            lines = lines.replace('  ', '_')
            length.append(lines.count('_') + 1)
    rational_len = min(length)
    while True:
        f = filter(lambda x: rational_len - x >= 0, length)
        t = tuple(f)
        if len(t) / len(length) >= percent:
            return rational_len
        else:
            rational_len += 1


def vocab_train_label(train_or_dev_path, vocab, tags, max_chunk_length):
    """将训练数据转为格式化

    :param train_or_dev_path: 训练数据路径
    :param vocab: 词向量
    :param tags: 序列标签
    :param max_chunk_length: 最大序列词语长度
    :return: 训练格式和测试格式
    """
    trains, labels = [], []
    with open(file=train_or_dev_path)as fp:
        for lines in fp:
            data, sequence = [], []
            line = lines.strip().split('  ')
            ms = map(lambda x: (x[:-2].split('_'), x[-1]), line)
            for v, k in ms:
                data.extend(map(lambda x: vocab.get(x, vocab['[UNK]']), v))
                if k != 'o':
                    m = map(lambda x: tags[x], ['B-' + k] + [('I-' + k)] * (len(v) - 1))
                else:
                    m = [tags['O']] * len(v)
                sequence.extend(m)
            data_len = len(data)
            if data_len <= max_chunk_length:
                data = [vocab['[PAD]']] * (max_chunk_length - data_len) + data
                sequence = [-1] * (max_chunk_length - data_len) + sequence
            else:
                data = data[:max_chunk_length]
                sequence = sequence[:max_chunk_length]
            trains.append(data)
            labels.append(sequence)
    return trains, labels


def restore_format(crf_path, standard_path):
    f_write = open(standard_path, 'w', newline='\n')
    with open(crf_path, 'r', newline='\n') as fp:
        lines = fp.read().split('\n\n')
    for line in lines:
        if line == '':
            continue
        tokens = line.split('\n')
        features = []
        tags = []
        for token in tokens:
            feature_tag = token.split()
            features.append(feature_tag[0])
            tags.append(feature_tag[-1])
        samples = []
        i = 0
        while i < len(features):
            sample = []
            if tags[i] == 'O':
                sample.append(features[i])
                j = i + 1
                while j < len(features) and tags[j] == 'O':
                    sample.append(features[j])
                    j += 1
                samples.append('_'.join(sample) + '/o')
            else:
                if tags[i][0] != 'B':
                    print(tags[i][0] + ' error start')
                    j = i + 1
                else:
                    sample.append(features[i])
                    j = i + 1
                    while j < len(features) and tags[j][0] == 'I' and tags[j][-1] == tags[i][-1]:
                        sample.append(features[j])
                        j += 1
                    samples.append('_'.join(sample) + '/' + tags[i][-1])
            i = j
        f_write.write('  '.join(samples) + '\n')
    f_write.close()

# if __name__ == '__main__':
#     analysis_vocab('./data/corpus.txt', './vocab.pkl')
#     tag = {'O': 0, 'B-a': 1, 'I-a': 2, 'B-b': 3, 'I-b': 4, 'B-c': 5, 'I-c': 6}
#     vocabs = load_vocab('vocab.pkl')
#     leg = analysis_rational_len('./data/train.txt', 0.95)
#     train, label = vocab_train_label('./data/train.txt', vocab=vocabs, tags=tag, max_chunk_length=leg)
