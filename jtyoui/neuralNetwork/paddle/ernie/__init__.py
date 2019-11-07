#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/7 10:26
# @Author: Jtyoui@qq.com
from .run_msra import st, match  # 实体识别

# 官网默认的参数,如果自己没有改变，可以使用
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
