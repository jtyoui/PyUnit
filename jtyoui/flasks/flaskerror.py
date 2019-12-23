#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/11/28 10:51
# @Author: Jtyoui@qq.com
from jtyoui.data.constant import http_status_code


def flask_error_abort(code, jsonify, error, message=None, **kwargs):
    """手动抛出flask异常、并且增加error详细异常"""
    return flask_abort(code=code, jsonify=jsonify, message=message, error=error, **kwargs)


def flask_abort(code, jsonify, message=None, **kwargs):
    """手动抛出flask异常

    :param code: 状态码
    :param jsonify: 传入flask里面的jsonify对象。from flask import jsonify
    :param message: 返回的msg异常信息
    :param kwargs: 其他jsonify参数
    :return: 异常状态信息
    """
    if message is None:
        message = http_status_code.get(str(code), '')
    response = jsonify(msg=message, code=code, **kwargs)
    return response, code


def flask_register_errors(app, jsonify):
    """app启动处注册一个错误处理器

    from flask import jsonify,Flask
    app = Flask(__name__)
    register_errors(app, jsonify) #注册异常解析器

    :param app: app对象
    :param jsonify: jsonify对象
    """

    @app.errorhandler(400)
    def bad_request(e):
        return flask_abort(400, jsonify)

    @app.errorhandler(401)
    def verify_id(e):
        return flask_abort(401, jsonify)

    @app.errorhandler(403)
    def forbidden(e):
        return flask_abort(403, jsonify)

    @app.errorhandler(404)
    def database_not_found_error_handler(e):
        return flask_abort(404, jsonify)

    @app.errorhandler(405)
    def method_not_allowed(e):
        return flask_abort(405, jsonify)

    @app.errorhandler(500)
    def internal_server_error(e):
        return flask_abort(500, jsonify)

    @app.errorhandler(Exception)
    def default_error_handler(e):
        message = f'发生未处理的异常 -> {e}'
        return flask_abort(0, jsonify, message=message)


if __name__ == '__main__':
    from flask import Flask, jsonify, abort

    app = Flask(__name__)
    flask_register_errors(app, jsonify)  # 注册错误异常处理器


    @app.route('/hi', methods=['POST'])
    def hello():
        try:
            value = 1 / 0
            return jsonify(msg='请求成功！', data=value, code=200)  # 正常信息
        except ValueError:
            return flask_abort(600, jsonify, message='被除数不能为0')  # 有自定义的处理器来处理
        except KeyError:
            code = 400
        except Exception:  # 其他错误
            code = 500
        return abort(code)  # 由错误异常处理器来处理
