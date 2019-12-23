#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/2/9 17:56
# @Author: Jtyoui@qq.com
import json
import time
import requests


class CodeRecognition:

    def __init__(self, username, password, app_id, app_key):
        """初始化账号

        :param username: 用户账号，不是开发者账号
        :param password: 用户密码，不是开发者密码
        :param app_id: 软件ＩＤ，开发者分成必要参数。
        :param app_key: 软件密钥，开发者分成必要参数。
        """
        self.api_url = 'http://api.yundama.com/api.php'
        self.base = {
            'username': username,
            'password': password,
            'appid': str(app_id),
            'appkey': app_key,
        }

    def request(self, fields, files):
        for key, value in files.items():
            files[key] = open(file=value, mode='rb')
        res = requests.post(self.api_url, files=files, data=fields)
        response = res.text
        response = json.loads(response)
        return response

    def upload(self, filename, code_type, timeout):
        data = dict({'method': 'upload', 'codetype': str(code_type), 'timeout': str(timeout)}, **self.base)
        file = dict(file=filename)
        response = self.request(data, file)
        if response:
            return response['ret'] if response['ret'] and response['ret'] < 0 else response['cid']
        else:
            return -9001

    def result(self, cid):
        data = dict({'method': 'result', 'cid': str(cid)}, **self.base)
        response = self.request(data, {})
        return response and response['text'] or ''

    def decode(self, filename, code_type, timeout=60):
        """识别验证码

        :param filename:  图片文件
        :param code_type: 验证码类型
        :param timeout: 超时时间，秒
        :return: 超时时间（秒），识别结果
        """
        cid = self.upload(filename, code_type, timeout)
        if cid > 0:
            for i in range(timeout):
                r = self.result(cid)
                if r != '':
                    return r
                else:
                    time.sleep(1)
            return ''
        return ''


cr = CodeRecognition('tyoui', 'zw13312324165', 6533, '1928b28e4ce11c541695bbb4510a4c41')

if __name__ == '__main__':
    # 第一个参数是要识别图像的照片。第二参数是图片类型（看README.md文件中的code_type的说明）
    cr = cr.decode('code.png', 3006)
    print(cr)
