#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/28 14:58
# @Author: Jtyoui@qq.com
import json


def flask_content_type(requests):
    """根据不同的content_type来解析数据"""
    if requests.method == 'POST':
        if requests.content_type == 'application/x-www-form-urlencoded':
            data = requests.form
        elif requests.content_type == 'application/json':
            data = requests.json
        else:  # 无法被解析出来的数据
            data = json.loads(requests.data)
        return data
    elif requests.method == 'GET':
        return requests.args


if __name__ == '__main__':
    from flask import Flask, request, jsonify

    app = Flask(__name__)


    @app.route('/hi', methods=['POST', 'GET'])
    def hello():
        data = flask_content_type(request)  # 所有的请求信息
        return jsonify(data=data)
