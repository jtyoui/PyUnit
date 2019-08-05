#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/1 14:49
# @Author: Jtyoui@qq.com
from keras.models import Model
from keras.layers import Embedding, Bidirectional, LSTM, TimeDistributed
from keras.layers import Input, Dropout, Conv1D, Dense, concatenate
from keras_contrib.layers.crf import CRF
from jtyoui.neuralNetwork.kerase.AnalyticalData import *
from keras.utils.np_utils import np
from keras.optimizers import Adam

chunk_tags = {'O': 0, 'B-a': 1, 'I-a': 2, 'B-b': 3, 'I-b': 4, 'B-c': 5, 'I-c': 6}
dirs = r'C:\Users\Xiaoi\Desktop\datagrand\datagrand'
vocab_path_model = dirs + '/vocab.pkl'
train_vocab_path = dirs + '/corpus.txt'
train_path = dirs + '/train.txt'
test_path = dirs + '/test.txt'
temp_path = dirs + '/crf.txt'
result_path = dirs + '/result.txt'
model_path = dirs + '/model-ner.h5'
vocab = load_vocab(vocab_path_model)
length = analysis_rational_len(train_path, percent=0.93)

EMBED_DIM = 300
HALF_WIN_SIZE = 2
DROPOUT_RATE = 0.1
FILTERS = 50
DENSE_DIM = 50


def create_model():
    inputs = Input(shape=(length,), dtype='int32', name='inputs')
    embedding_1 = Embedding(len(vocab), EMBED_DIM, input_length=length, mask_zero=True)(inputs)
    bilstm = Bidirectional(LSTM(EMBED_DIM // 2, return_sequences=True))(embedding_1)
    bilstm_dropout = Dropout(DROPOUT_RATE)(bilstm)
    embedding_2 = Embedding(len(vocab), EMBED_DIM, input_length=length)(inputs)
    con = Conv1D(filters=FILTERS, kernel_size=2 * HALF_WIN_SIZE + 1, padding='same')(embedding_2)
    con_d = Dropout(DROPOUT_RATE)(con)
    dense_con = TimeDistributed(Dense(DENSE_DIM))(con_d)
    rnn_cnn = concatenate([bilstm_dropout, dense_con], axis=2)
    dense = TimeDistributed(Dense(len(chunk_tags)))(rnn_cnn)
    crf = CRF(len(chunk_tags), sparse_target=True)
    crf_output = crf(dense)
    model = Model(input=[inputs], output=[crf_output])
    model.compile(loss=crf.loss_function, optimizer=Adam(), metrics=[crf.accuracy])
    return model


def train_model(model):
    train, label = vocab_train_label(train_path, vocab=vocab, tags=chunk_tags, max_chunk_length=length)
    n = np.array(label, dtype=np.float)
    label = n.reshape((n.shape[0], n.shape[1], 1))
    train = np.array(train)
    model.fit(x=train, y=label, batch_size=16, epochs=4)
    model.save(model_path)
    return True


def predict_model(model):
    x_test, original = vocab_test(test_path, vocab, length)
    ws = open(temp_path, mode='w', newline='\n')
    tags = dict(zip(chunk_tags.values(), chunk_tags.keys()))
    model.load_weights(model_path)
    for question, tests in zip(original, x_test):
        raw = model.predict([[tests]])[0][-len(question):]
        result = [np.argmax(row) for row in raw]
        answer = tuple(map(lambda x: tags[x], result))
        ma = map(lambda x: x[0] + '\t' + x[1] + '\n', zip(question, answer))
        ws.writelines(ma)
        ws.write('\n')
    ws.flush()
    ws.close()


if __name__ == '__main__':
    # m = create_model()
    # train_model(m)
    # predict_model(m)
    restore_format(crf_path=temp_path, standard_path=result_path)
