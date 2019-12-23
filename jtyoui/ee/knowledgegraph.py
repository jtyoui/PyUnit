#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/26 18:03
# @Author: Jtyoui@qq.com
from jtyoui.web import get


def mention_to_entity(mention):
    """输入名称->实体

    :param mention: 输入名称
    :return: 根据名称获取歧义关系
    """
    url = f'https://api.ownthink.com/kg/ambiguous?mention={mention}'  # 知识图谱API，歧义关系
    return get(url).text


def entity_to_knowledge(entity):
    """ 实体->知识

    :param entity: 实体名
    :return: 根据实体获取实体知识
    """
    url = f'https://api.ownthink.com/kg/knowledge?entity={entity}'  # 知识图谱API，实体知识
    return get(url).text


def entity_attribute_value(entity, attribute):
    """实体&属性->属性值

    :param entity: 实体名
    :param attribute: 属性名
    :return: 根据实体、属性获取属性值
    """
    url = f'https://api.ownthink.com/kg/eav?entity={entity}&attribute={attribute}'  # 知识图谱API，属性值
    return get(url).text


if __name__ == '__main__':
    print(mention_to_entity('红楼梦'))

    print(entity_to_knowledge('刘德华'))

    print(entity_attribute_value('苹果', '颜色'))
