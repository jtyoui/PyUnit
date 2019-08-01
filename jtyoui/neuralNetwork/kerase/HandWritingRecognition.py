#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/7/31 15:26
# @Author: Jtyoui@qq.com
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential, load_model
from keras.layers import Dense, Convolution2D, MaxPool2D, Flatten, Dropout
from keras.optimizers import SGD, Adam, RMSprop
from keras.layers.recurrent import SimpleRNN
from keras.losses import categorical_crossentropy


def nn_model():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # 归一化
    x_train = x_train.reshape(x_train.shape[0], -1) / 255.
    x_test = x_test.reshape(x_test.shape[0], -1) / 255.
    # one-hot
    y_train = np_utils.to_categorical(y=y_train, num_classes=10)
    y_test = np_utils.to_categorical(y=y_test, num_classes=10)

    # 创建模型:输入784个神经元，输出10个神经元
    model = Sequential([
        Dense(units=200, input_dim=784, bias_initializer='one', activation='tanh'),
        Dense(units=100, bias_initializer='one', activation='tanh'),
        Dense(units=10, bias_initializer='one', activation='softmax'),
    ])

    # loss='mse' 均方差
    opt = SGD(lr=0.2)  # 优化器
    model.compile(optimizer=opt, loss=categorical_crossentropy, metrics=['accuracy'])  # 编译
    model.fit(x_train, y_train, batch_size=64, epochs=20)
    model_save(model, './model.h5')


def cnn_model():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # 归一化
    x_train = x_train.reshape(-1, 28, 28, 1) / 255.
    x_test = x_test.reshape(-1, 28, 28, 1) / 255.
    # one-hot
    y_train = np_utils.to_categorical(y=y_train, num_classes=10)
    y_test = np_utils.to_categorical(y=y_test, num_classes=10)

    model = Sequential([
        # input_shape:输入平面，就在第一个位置设置
        # filters：卷积核、滤波器
        # kernel_size：卷积核大小
        # strides：步长
        # padding有两种方式：same/valid
        # activation：激活函数
        Convolution2D(input_shape=(28, 28, 1), filters=32, kernel_size=5, strides=1, padding='same', activation='relu'),
        MaxPool2D(pool_size=2, strides=2, padding='same'),
        Convolution2D(filters=64, kernel_size=5, padding='same', activation='relu'),
        MaxPool2D(pool_size=2, trainable=2, padding='same'),
        Flatten(),  # 扁平化
        Dense(units=1024, activation='relu'),
        Dropout(0.5),
        Dense(units=10, activation='softmax'),
    ])
    opt = Adam(lr=1e-4)
    model.compile(optimizer=opt, loss=categorical_crossentropy, metrics=['accuracy'])
    model.fit(x=x_train, y=y_train, batch_size=64, epochs=20)
    model_save(model, './model.h5')


def rnn_model():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # 归一化
    x_train = x_train / 255.
    x_test = x_test / 255.
    # one-hot
    y_train = np_utils.to_categorical(y=y_train, num_classes=10)
    y_test = np_utils.to_categorical(y=y_test, num_classes=10)

    model = Sequential([
        SimpleRNN(units=50, input_shape=(28, 28)),
        Dense(units=10, activation='softmax'),
    ])
    opt = RMSprop(lr=1e-4)
    model.compile(optimizer=opt, loss=categorical_crossentropy, metrics=['accuracy'])
    model.fit(x=x_train, y=y_train, batch_size=64, epochs=20)
    model_save(model, './model.h5')


def model_save(model, path):
    model.save(path)


def model_load(path='./model.h5'):
    model = load_model(path)
    return model


if __name__ == '__main__':
    nn_model()  # 神经网络
    # cnn_model()  # 卷积神经网络
    # rnn_model()  # 循环神经网络

    # # 加载模型
    # _, (x_test, y_test) = mnist.load_data()
    # x_test = x_test.reshape(x_test.shape[0], -1) / 255.
    # y_test = np_utils.to_categorical(y=y_test, num_classes=10)
    # data = x_test[0:10]  # 预测10张
    # label = y_test[0:10]
    # models = model_load()
    # pre = models.predict(x=data, batch_size=10)
    # print('实际：', np_utils.np.argmax(label, axis=1), '\t预测：', np_utils.np.argmax(pre, axis=1))

    # 创建模型图画
    # from keras.utils.vis_utils import plot_model
    # plot_model(model=model, to_file='rnn_model.png', show_shapes=True, rankdir='TB', show_layer_names='False')
