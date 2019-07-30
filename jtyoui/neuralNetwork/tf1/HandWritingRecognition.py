#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/7/28 0:51
# @Author: jtyoui@qq.com
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib.layers import l2_regularizer
import tensorflow as tf
from PIL import Image
import numpy as np
import os

input_node = 784  # 输入节点
output_node = 10  # 输出节点
layer_node = 500  # 隐藏层节点
regularization = 0.001  # 正则值
bitch_size = 200  # 批量大小
learning_rates = 0.1  # 初始学习率
learning_rate_decay = 0.99  # 学习衰减率
steps = 50000  # 训练步数
moving_average_decay = 0.99  # 滑动平均衰减值
model_save_path = './model/'  # 保存文件夹
model_name = 'mist_model'  # 保存名字


def get_w(shape, regular):
    """获得w权重"""
    w = tf.Variable(tf.random.truncated_normal(shape=shape, stddev=0.1))
    if regular:
        tf.compat.v1.add_to_collection(name='losses', value=l2_regularizer(regular)(w))
    return w


def get_b(shape):
    """获得b权重"""
    b = tf.Variable(tf.zeros(shape=shape))
    return b


def forward(x, regular):
    """前向传播"""
    w1 = get_w(shape=(input_node, layer_node), regular=regular)
    b1 = get_b(shape=[layer_node])
    h1 = tf.nn.relu(tf.matmul(x, w1) + b1)
    w2 = get_w(shape=(layer_node, output_node), regular=regular)
    b2 = get_b(shape=[output_node])
    y = tf.matmul(h1, w2) + b2
    return y


def get_pic(photo):
    """将照片转为输入格式"""
    img = Image.open(photo).convert('L')  # 进行转灰度
    img_array = img.resize((28, 28), Image.ANTIALIAS)  # 压缩高质量照片
    img_array = 255 - np.array(img_array)  # 将黑变白。白变黑
    img_array[img_array < 50] = 0  # 小于50转为黑色
    img_array[img_array >= 50] = 255  # 大于50转为纯白色
    nm_array = img_array.reshape((1, 784)).astype(np.float32)
    return nm_array


def backward():
    """后向传播"""
    mist = input_data.read_data_sets(train_dir='./data/', one_hot=True)
    train_data = tf.compat.v1.placeholder(tf.float32, shape=(None, input_node))
    label = tf.compat.v1.placeholder(tf.float32, shape=(None, output_node))
    y = forward(train_data, regular=regularization)
    global_step = tf.Variable(initial_value=0, trainable=False)  # 定义一个计数器，不参与训练

    # 交叉熵
    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(label, 1))
    cem = tf.reduce_mean(ce)

    # 正则化
    loss = cem + tf.add_n(tf.compat.v1.get_collection('losses'))

    # 验证正确率
    correct_predict = tf.equal(tf.argmax(input=y, axis=1), tf.argmax(input=label, axis=1))
    accuracy = tf.reduce_mean(tf.cast(x=correct_predict, dtype=tf.float32))

    # 指数衰减学习率
    learning_rate = tf.compat.v1.train.exponential_decay(learning_rate=learning_rates,
                                                         global_step=global_step,
                                                         decay_steps=mist.train.num_examples / bitch_size,
                                                         decay_rate=learning_rate_decay,
                                                         staircase=True)
    train_step = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(loss=loss, global_step=global_step)

    # 滑动平均
    ema = tf.train.ExponentialMovingAverage(moving_average_decay, global_step)
    ema_op = ema.apply(var_list=tf.compat.v1.trainable_variables())
    with tf.control_dependencies(control_inputs=[train_step, ema_op]):
        train_op = tf.no_op(name='train')

    saver = tf.compat.v1.train.Saver()
    with tf.compat.v1.Session() as sess:
        sess.run(tf.compat.v1.global_variables_initializer())
        for i in range(steps):
            xs, ys = mist.train.next_batch(bitch_size)
            _, loss_val, step, acc = sess.run(fetches=[train_op, loss, global_step, accuracy],
                                              feed_dict={train_data: xs, label: ys})
            if i % 1000 == 0:
                print(f'loss:{loss_val},accuracy:{acc}')

        saver.save(sess, os.path.join(model_save_path, model_name), global_step=step)


def train():
    backward()


def restore_model(pic):
    with tf.Graph().as_default():
        x = tf.compat.v1.placeholder(tf.float32, shape=(None, input_node))
        y = forward(x, None)
        pre_value = tf.argmax(input=y, axis=1)

        v = tf.train.ExponentialMovingAverage(moving_average_decay).variables_to_restore()
        saves = tf.compat.v1.train.Saver(var_list=v)
        with tf.compat.v1.Session() as sess:
            cp = tf.train.get_checkpoint_state(checkpoint_dir=model_save_path)
            if cp and cp.model_checkpoint_path:
                saves.restore(sess=sess, save_path=cp.model_checkpoint_path)
                pre_value = sess.run(fetches=pre_value, feed_dict={x: pic})
                return pre_value
            else:
                print('NO Model file found!')
    return -1


def test(photo_path):
    pic = get_pic(photo_path)
    # Image.fromarray(pic.reshape((28, 28))).show()  # 展示图画数字
    return restore_model(pic / 255.0)


if __name__ == '__main__':
    # 先训练在测试
    train()  # 训练
    # value = test('./5.jpg')  # 测试
    # print(value)
