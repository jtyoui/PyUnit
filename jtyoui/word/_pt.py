#!/usr/bin/python3.7
# -*-coding:utf-8-*-
# @Time:2019/6/2115:40
# @Author:Jtyoui@qq.com
import re

# 介词常修饰名词，代词或名词性质的短语前面，和这些词合起来组成介词结构，以表示所处、时间、状态、方式、原因、目的、比较对象等的词。
prep_time = '自、自从、于、打、到、往、在、当、朝、向、顺着、沿着、随着'.split('、')  # 表示时间方向的介词
prep_mode = '照、按照、依、依照、本着、经过、通过、根据、以、凭'.split('、')  # 表示方式的介词
prep_objective = '为了、为着'.split('、')  # 表示目的的介词
prep_Reason = '因为'.split('、')  # 表示原因的介词
prep_Range = '对于、把、向、跟、与、同、给、关于'.split('、')  # 表示对象、范围的介词
prep_Exclude = '除了、除去、除非'.split('、')  # 表示排除的介词
prep_passive = '叫、让、给'.split('、')  # 表示被动的介词
prep_compare = '和、同、着、了、过'.split('、')  # 表示比较的介词
prep_verb = '在、为、比、到、给、朝、通过'.split('、')  # 表示动介词

# 副词常修饰、限制动词或形容词性词语，表示程度、范围、时间等意义
adv_method = '大肆、肆意、特意、猛然、忽然、公然、连忙、赶紧、悄悄、暗'.split('、')  # 方式副词
adv_rep = '又、再、还、仍'.split('、')  # 重复副词
adv_deg = '很、非常、极、十分、最、顶、太、更、挺、极其、格外、分外、更加、越、越发、有点'.split('、')  # 表示程度
adv_range = '都、全、总、总共、共、统统、仅仅、只、光、净、一概、一律、一齐、单、单单、处处'.split('、')  # 表示范围
adv_time = '已经、曾经、早已、刚刚、正、正在、就、就要、将、将要、曾、刚、才、在、马、渐渐、早晚'.split('、')  # 表示时间
adv_freq = '从来、终于、一向、向来、从来、总是、始终、往往、永、赶紧、仍然、还是'.split('、')  # 表示频率
adv_neg = '不、没、没有、不用、甭、必、必须、必定、准、的确、未、别、莫、勿、是否'.split('、')  # 表示肯定、否定
adv_emotion = '忽然、猛然、公然、特意、亲自、大肆、肆意、悄悄、连忙、赶紧、暗暗'.split('、')  # 表示情态、方式
adv_tone = '难道、决、岂、反正、也许、大约、大概、果然、居然、竟然、究竟、幸而、幸亏、偏偏'.split('、')  # 表示语气

# 助词若位于句子的前、中、后，通常表示某种语气；若用于句子中间或词与词之间，则表示提示某种结构上的关系。
aw_structure = '的、了、着、吧、啊、之、者、所、然、夫、所以、乎、焉、等、且、地、得、似'.split('、')  # 结构助词
aw_tone = '也、者、乎、哉、与、欤、邪、耶、为、吧、罢、呀、啊、啦、啊、呀、哇、哪、的、了、嘛、呢、啦、罢了、而已、呢、么'.split('、')  # 语气助词
aw_tense = '着、了、过'.split('、')  # 时态助词


def continuous_pause(sentence: str) -> str:
    """去除多重断句符号"""
    return re.sub('[，。,.]{2,}', '，', sentence)


def punctuate(sentence):
    """根据词性进行简单校验断句"""
    p = continuous_pause(sentence)
    sent = ''
    for index, word in enumerate(p):
        if word in '，。,.':
            if p[index - 1] in aw_tone:
                continue
            elif p[index + 1] in aw_structure:
                continue
        sent += word
    return sent


if __name__ == '__main__':
    print(punctuate('你在哪.,里。.，我在天安门。.，'))
