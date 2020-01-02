#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/11 11:44
# @Author: Jtyoui@qq.com
from jtyoui.neuralNetwork.paddle.ernie.transformer_encoder import encoder, pre_process_layer
from jtyoui.neuralNetwork.paddle.ernie.vocab import vocal
import os
import numpy as np
from paddle import fluid  # pip install paddlepaddle==1.6.1

ERNIE_MODEL_PARAMETER = {
    "attention_probs_dropout_prob": 0.1,
    "hidden_act": "relu",
    "hidden_dropout_prob": 0.1,
    "hidden_size": 768,
    "initializer_range": 0.02,
    "max_position_embeddings": 513,
    "num_attention_heads": 12,
    "num_hidden_layers": 12,
    "type_vocab_size": 2,
    "vocab_size": 18000
}
ERNIE_LABEL_MAP = {
    "B-PER": 0,  # 人名
    "I-PER": 1,
    "B-ORG": 2,  # 机构名
    "I-ORG": 3,
    "B-LOC": 4,  # 地名
    "I-LOC": 5,
    "O": 6
}

# 需要自己更改
model_path, config, label_map_config = None, ERNIE_MODEL_PARAMETER, ERNIE_LABEL_MAP
examples = ''


def pad_batch_data(inst, pad_idx=0, input_mask=False):
    return_list = []
    max_len = max(len(inst) for inst in inst)
    inst_data = np.array([inst + list([pad_idx] * (max_len - len(inst))) for inst in inst])
    return_list += [inst_data.astype("int64").reshape([-1, max_len, 1])]
    if input_mask:
        input_mask_data = np.array([[1] * len(inst) + [0] * (max_len - len(inst)) for inst in inst])
        input_mask_data = np.expand_dims(input_mask_data, axis=-1)
        return_list += [input_mask_data.astype("float32")]
    return return_list if len(return_list) > 1 else return_list[0]


def prepare_batch_data(example):
    examples = ''
    words = [1]
    for word in example:
        if word in vocal:
            words.append(vocal[word])
            examples += word
    else:
        words.append(2)
    padded_token_ids, input_mask = pad_batch_data([words], 0, True)
    padded_text_type_ids = pad_batch_data([[0] * len(words)])
    padded_position_ids = pad_batch_data([list(range(len(words)))])
    padded_label_ids = pad_batch_data([[8] * len(words)], len(label_map_config) - 1)
    return_list = [padded_token_ids, padded_text_type_ids, padded_position_ids, input_mask, padded_label_ids]
    return return_list, examples


def data_generator(input_str):
    def wrapper():
        global examples
        return_list, examples = prepare_batch_data(input_str)
        yield return_list

    return wrapper


def init_checkpoint(exe, init_checkpoint_path, main_program):
    def existed(var):
        if not fluid.io.is_persistable(var):
            return False
        return os.path.exists(os.path.join(init_checkpoint_path, var.name))

    fluid.io.load_vars(exe, init_checkpoint_path, main_program=main_program, predicate=existed)


def evaluate(exe, program, reader, graph_vars):
    fetch_list = [graph_vars["labels"].name, graph_vars["infers"].name]
    total_number = None
    while True:
        reader.start()
        try:
            _, np_infers = exe.run(program=program, fetch_list=fetch_list)
            total_number = [ls[0] for ls in np_infers[1:-1]]
        except Exception as e:
            assert 'There is no next data' in e.__str__(), Exception('非正常停止。')
            reader.reset()
            break
    return total_number


def create_model():
    reader = fluid.layers.py_reader(capacity=50, shapes=[[-1, 256, 1]] * 5, lod_levels=[0] * 5, use_double_buffer=True,
                                    dtypes=['int64'] * 3 + ['float32', 'int64'])

    src_ids, sent_ids, pos_ids, input_mask, labels = fluid.layers.read_file(reader)
    self_attn_mask = fluid.layers.matmul(x=input_mask, y=input_mask, transpose_y=True)
    self_attn_mask = fluid.layers.scale(x=self_attn_mask, scale=10000.0, bias=-1.0, bias_after_scale=False)
    n_head_self_attn_mask = fluid.layers.stack(x=[self_attn_mask] * config['num_attention_heads'], axis=1)
    n_head_self_attn_mask.stop_gradient = True
    param_initializer = fluid.initializer.TruncatedNormal(config['initializer_range'])
    emb_out = fluid.layers.embedding(
        input=src_ids,
        size=[config['vocab_size'], config['hidden_size']],
        dtype="float32",
        param_attr=fluid.ParamAttr(name="word_embedding", initializer=param_initializer), is_sparse=False)

    position_emb_out = fluid.layers.embedding(
        input=pos_ids,
        size=[config['max_position_embeddings'], config['hidden_size']],
        dtype="float32",
        param_attr=fluid.ParamAttr(name="pos_embedding", initializer=param_initializer))

    sent_emb_out = fluid.layers.embedding(
        sent_ids,
        size=[config['type_vocab_size'], config['hidden_size']],
        dtype="float32",
        param_attr=fluid.ParamAttr(name="sent_embedding", initializer=param_initializer))

    emb_out += position_emb_out + sent_emb_out
    emb_out = pre_process_layer(emb_out, 'nd', config['hidden_dropout_prob'], name='pre_encoder')

    enc_out = encoder(
        n_layer=config['num_hidden_layers'],
        enc_input=emb_out,
        attn_bias=n_head_self_attn_mask,
        n_head=config['num_attention_heads'],
        d_key=config['hidden_size'] // config['num_attention_heads'],
        d_value=config['hidden_size'] // config['num_attention_heads'],
        d_model=config['hidden_size'],
        d_inner_hid=config['hidden_size'] * 4,
        prepostprocess_dropout=config['hidden_dropout_prob'],
        attention_dropout=config['attention_probs_dropout_prob'],
        relu_dropout=0,
        hidden_act=config['hidden_act'],
        preprocess_cmd="",
        postprocess_cmd="dan",
        param_initializer=param_initializer,
        name='encoder')

    log = fluid.layers.fc(input=enc_out, size=len(label_map_config), num_flatten_dims=2,
                          param_attr=fluid.ParamAttr(name="cls_seq_label_out_w",
                                                     initializer=fluid.initializer.TruncatedNormal(scale=0.02)),
                          bias_attr=fluid.ParamAttr(name="cls_seq_label_out_b",
                                                    initializer=fluid.initializer.Constant(0.)))

    ret_labels = fluid.layers.reshape(x=labels, shape=[-1, 1])
    ret_infers = fluid.layers.reshape(x=fluid.layers.argmax(log, axis=2), shape=[-1, 1])

    graph_vars = {"labels": ret_labels, "infers": ret_infers}
    for v in graph_vars.values():
        v.persistable = True

    return reader, graph_vars


def match(words, init_st: list):
    """抽取实体函数

    :param words: 需要抽取的文字
    :param init_st: 初始化参数。st()
    :return: 数字列表，这些数字是在label_map_config中配置的
    """
    global examples
    examples = ''
    data = data_generator(words)
    init_st[2].decorate_tensor_provider(data)
    number = evaluate(*init_st)
    return number, examples


def st(new_model_path=None, new_config=None, new_label_map_config=None) -> list:
    """初始化模型，只需要加载一次即可

    :param new_model_path: 模型路径
    :param new_config: 模型配置参数
    :param new_label_map_config: 模型实体映射
    """
    global model_path, config, label_map_config

    if new_model_path:
        model_path = new_model_path

    if new_config:
        config = new_config

    if new_label_map_config:
        label_map_config = new_label_map_config

    exe = fluid.Executor(fluid.CPUPlace())
    startup_program = fluid.Program()
    test_program = fluid.Program()
    with fluid.program_guard(test_program, startup_program):
        with fluid.unique_name.guard():
            test_reader, graph_vars = create_model()
    test_program = test_program.clone(for_test=True)
    exe.run(startup_program)
    init_checkpoint(exe, model_path, main_program=startup_program)
    return [exe, test_program, test_reader, graph_vars]


if __name__ == '__main__':
    # 默认的模型参数和映射表
    ERNIE_MODEL_PATH = 'D://model'
    s = st(ERNIE_MODEL_PATH)
    print(match('我叫刘万光我是贵阳       市南明叇村永乐乡水塘村的村民', s))
