#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/7/30 10:33
# @Author: Jtyoui@qq.com
import tensorflow
from tensorflow.contrib.rnn import LSTMCell
from tensorflow.contrib.crf import crf_log_likelihood, viterbi_decode


class NerCRF:
    batch_size = 64
    epoch_num = 20
    hidden_dim = 300
    embeddings = 300
    dropout_keep_prob = 0.5
    lr = 0.001
    clip_grad = 5.0
    model_path = './model/'
    tag2label = {"O": 0, "B-a": 1, "I-a": 2, "B-b": 3, "I-b": 4, "B-c": 5, "I-c": 6}
    num_tags = len(tag2label)
    vocab = {}  # 5000为映射表大小，记得更改

    def get_feed_dict(self, seq_, label_):
        max_len = max(map(lambda x: len(x), seq_))
        seq_list, seq_len_list, label_list = [], [], []
        for seq, label in zip(seq_, label_):
            bu = [0] * max(max_len - len(seq), 0)
            seq_list.append(seq[:max_len] + bu)
            label_list.append(label[:max_len] + bu)
            seq_len_list.append(min(len(seq), max_len))
        feed_dict = {word_ids: seq_list, seq_length: seq_len_list, labels: label_list, lr_pl: self.lr,
                     dropout_pl: self.dropout_keep_prob}
        return feed_dict

    def read_data(self):
        """需要重新该方法，格式要保证一致"""
        word = [[1, 2, 3], [2, 3, 4, 5], [5, 6, 7, 3, 5, 2]]
        word_label = [[0, 5, 6], [3, 4, 0, 0], [1, 2, 0, 0, 3, 4]]
        return word, word_label

    def train(self):
        saver = tensorflow.train.Saver()
        with tensorflow.Session() as sess:
            sess.run(tensorflow.global_variables_initializer())
            for epoch in range(self.epoch_num):
                for _ in range(self.batch_size):
                    feed = self.get_feed_dict(*self.read_data())
                    _, loss_train, step_num_ = sess.run(fetches=[train_op, loss, global_step], feed_dict=feed)
                    print('loss', loss_train)
            saver.save(sess, self.model_path, global_step=step_num_)

    def test(self, sentence):
        feed_dict = dict()
        saver = tensorflow.train.Saver()
        with tensorflow.Session() as sess:
            cp = tensorflow.train.get_checkpoint_state(checkpoint_dir=self.model_path)
            saver.restore(sess, save_path=cp.model_checkpoint_path)
            label = [0.0] * len(sentence)
            feed_dict[word_ids] = sentence
            feed_dict[seq_length] = [len(sentence)]
            feed_dict[labels] = [label]
            feed_dict[lr_pl] = self.lr
            feed_dict[dropout_pl] = self.dropout_keep_prob
            tag, transition = sess.run(fetches=[logic, transition_params], feed_dict=feed_dict)
            tags = []
            for t in tag[0]:
                [vite], _ = viterbi_decode(t[:len(sentence)], transition_params)
                tags.append(vite)
            print(tags)
        return tags


word_ids = tensorflow.placeholder(dtype=tensorflow.int32, shape=[None, None])
labels = tensorflow.placeholder(dtype=tensorflow.int32, shape=[None, None])
seq_length = tensorflow.placeholder(dtype=tensorflow.int32, shape=[None])
dropout_pl = tensorflow.placeholder(dtype=tensorflow.float32, shape=[])
lr_pl = tensorflow.placeholder(dtype=tensorflow.float32, shape=[])

embedding_mat = tensorflow.random.uniform(shape=(len(NerCRF.vocab), NerCRF.embeddings), minval=-0.25, maxval=0.25)

with tensorflow.variable_scope("words"):
    _word_embeddings = tensorflow.Variable(embedding_mat, dtype=tensorflow.float32, trainable=True)
    word_embeddings = tensorflow.nn.embedding_lookup(params=_word_embeddings, ids=word_ids, name="word_embeddings")
    word_embeddings = tensorflow.nn.dropout(word_embeddings, dropout_pl)

with tensorflow.variable_scope("bi-lstm"):
    cell_fw = LSTMCell(NerCRF.hidden_dim)
    cell_bw = LSTMCell(NerCRF.hidden_dim)
    (output_fw, output_bw), _ = tensorflow.nn.bidirectional_dynamic_rnn(cell_fw=cell_fw, cell_bw=cell_bw,
                                                                        inputs=word_embeddings,
                                                                        sequence_length=seq_length,
                                                                        dtype=tensorflow.float32)
    output = tensorflow.concat([output_fw, output_bw], axis=-1)
    output = tensorflow.nn.dropout(output, dropout_pl)

with tensorflow.variable_scope("project"):
    W = tensorflow.get_variable(name="W", shape=[2 * NerCRF.hidden_dim, NerCRF.num_tags],
                                initializer=tensorflow.contrib.layers.xavier_initializer(),
                                dtype=tensorflow.float32)
    b = tensorflow.get_variable(name="b", shape=[NerCRF.num_tags], initializer=tensorflow.zeros_initializer(),
                                dtype=tensorflow.float32)
    s = tensorflow.shape(output)
    output = tensorflow.reshape(output, [-1, 2 * NerCRF.hidden_dim])
    pred = tensorflow.matmul(output, W) + b
    logic = tensorflow.reshape(pred, [-1, s[1], NerCRF.num_tags])

log_likelihood, transition_params = crf_log_likelihood(inputs=logic, tag_indices=labels,
                                                       sequence_lengths=seq_length)
loss = -tensorflow.reduce_mean(log_likelihood)

with tensorflow.variable_scope("train_step"):
    global_step = tensorflow.Variable(initial_value=0, trainable=False)
    optimizer = tensorflow.train.AdamOptimizer(learning_rate=lr_pl)
    grads_and_vars = optimizer.compute_gradients(loss)
    grads_and_vars_clip = [[tensorflow.clip_by_value(g, -NerCRF.clip_grad, NerCRF.clip_grad), v] for g, v in
                           grads_and_vars]
    train_op = optimizer.apply_gradients(grads_and_vars_clip, global_step=global_step)

if __name__ == '__main__':
    ner = NerCRF()
    ner.train()
