# **Flasks** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 对flask框架的补充模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()


### 安装
    pip install jtyoui

### flask解析请求头信息
```python
from jtyoui.flasks import content_type
if __name__ == '__main__':
    from flask import Flask, request, jsonify

    app = Flask(__name__)


    @app.route('/hi', methods=['POST', 'GET'])
    def hello():
        data = content_type(request)  # 所有的请求信息
        return jsonify(data=data)
```

### flask自动异常处理器
```python
from jtyoui.flasks import flask_register_errors,flask_abort
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
```


***
[1]: https://blog.jtyoui.com