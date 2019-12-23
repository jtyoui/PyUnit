#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/9/23 16:20
# @Author: Jtyoui@qq.com
import os


def format_CRF_to_ERNIE(load_file, save_file, newline=os.linesep):
    """将CRF训练的格式转为ERNIE训练的格式

    [CRF]\n
    中	B-ORG\n
    共	I-ORG\n
    中	I-ORG\n
    央	I-ORG\n
    致	O\n
    中	B-ORG\n
    国	I-ORG\n
    致	I-ORG\n
    公	I-ORG\n
    党	I-ORG\n
    十	I-ORG\n
    一	I-ORG\n
    大	I-ORG\n
    的	O\n
    贺	O\n
    词	O\n

    [ERNIE]\n
    中\x02共\x02中\x02央\x02致\x02中\x02国\x02致\x02公\x02党\x02十\x02一\x02大\x02的\x02贺\x02词    B-ORG\x02I-ORG\x02I-ORG\x02I-ORG\x02O\x02B-ORG\x02I-ORG\x02I-ORG\x02I-ORG\x02I-ORG\x02I-ORG\x02I-ORG\x02I-ORG\x02O\x02O\x02O

    :param load_file: 加载数据的文件地址
    :param save_file: 保存数据的文件地址
    :param newline: 文件的换行符,默认是本机系统的换行符
    :return: 文件地址
    """
    ws = open(save_file, encoding='utf-8', mode='w', newline='\n')
    ws.write('text_a\tlabel\n')
    with open(load_file, encoding='utf-8', newline=newline)as fp:
        data = fp.read().strip().split(newline + newline)
        for line in data:
            chars, labels = [], []
            ls = line.split(newline)
            for c in ls:
                char, label = c.split()
                chars.append(char)
                labels.append(label)
            ws.write('\x02'.join(chars) + '\t' + '\x02'.join(labels) + '\n')
    ws.close()


if __name__ == '__main__':
    format_CRF_to_ERNIE('train_data.txt', 'train.tsv')
