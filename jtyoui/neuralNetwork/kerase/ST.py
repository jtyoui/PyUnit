#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/1 14:49
# @Author: Jtyoui@qq.com
from keras.models import Sequential, load_model
from keras.layers import Embedding, Bidirectional, LSTM
from keras_contrib.layers import CRF, crf
from keras.optimizers import RMSprop
from jtyoui.neuralNetwork.communal.Vocabs import read_train, read_test
import json
import numpy

tags = {'O': 0,
        'B-a': 1, 'I-a': 2,
        'B-b': 3, 'I-b': 4,
        'B-c': 5, 'I-c': 6
        }

vocab = json.load(open('./vocab.json'))


def train(path, model_path):
    x_train, y_train = read_train(tag=tags, path=path)
    length = len(x_train)

    def get_generator(batch):
        while True:
            for i in range(0, length, batch):
                x_train_bitch = x_train[i:i + batch]
                y_train_bitch = y_train[i:i + batch]
                max_len = max(len(s) for s in x_train_bitch)
                for x, y in zip(x_train_bitch, y_train_bitch):
                    if max_len > len(x):
                        x.extend([0] * (max_len - len(x)))
                        y.extend([[-1]] * (max_len - len(y)))

                yield numpy.array(x_train_bitch), numpy.array(y_train_bitch)

    model = Sequential([
        Embedding(input_dim=len(vocab), output_dim=600, mask_zero=True),
        Bidirectional(layer=LSTM(units=600 // 2, return_sequences=True))
    ])
    crf_ = CRF(units=len(tags), sparse_target=True)
    model.add(crf_)
    model.compile(optimizer=RMSprop(), loss=crf_.loss_function, metrics=[crf_.accuracy])
    model.fit_generator(generator=get_generator(64), steps_per_epoch=length // 64, epochs=4)
    model.save(model_path)


def test(path, model_path):
    x_test = read_test(path)
    tag = dict(zip(tags.values(), tags.keys()))
    custom_objects = {'CRF': CRF, 'crf_loss': crf.crf_loss, 'crf_viterbi_accuracy': crf.crf_viterbi_accuracy}
    model = load_model(model_path, custom_objects=custom_objects)
    for tests in x_test:
        raw = model.predict([[tests]])[0][-len(tests):]
        result = [numpy.argmax(row) for row in raw]
        result_tags = tuple(map(lambda x: tag[x], result))
        print(result_tags)


if __name__ == '__main__':
    train(None, model_path=None)
