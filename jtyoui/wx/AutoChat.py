#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/2 0002
# @Email : jtyoui@qq.com
# @Software : PyCharm
import requests
from fake_useragent import UserAgent
import json
import itchat
import os

# 全局请求头
files = {}
headers = {}
body = {}
timeouts = {}
resHeader = {}
app_id = '86760'
app_secret = 'ccece9bc703d4064b95f31ced8f84c42'
rec_tmp_dir = os.path.join(os.getcwd(), 'tmp/')
if not os.path.exists(rec_tmp_dir):
    os.mkdir(rec_tmp_dir)
oneself_name = None
one_run, run = False, True


class ShowApiRequest:
    def __init__(self, url, my_app_id, my_app_secret):
        self.url = url
        self.my_appId = my_app_id
        self.my_appSecret = my_app_secret
        body["showapi_appid"] = my_app_id
        body["showapi_sign"] = my_app_secret
        headers["User-Agent"] = UserAgent().random

    @staticmethod
    def add_file(key, value_url):
        with open("{}".format(value_url), 'rb')as f:
            files[key] = f.read()

    @staticmethod
    def add_body(key, value):
        body[key] = value

    # 设置连接时间和读取时间
    @staticmethod
    def set_timeout(connect_timout, read_timeout):
        timeouts["connect_timout"] = connect_timout
        timeouts["read_timeout"] = read_timeout

    def post(self):
        if not timeouts:
            res = requests.post(self.url, files=files, data=body, headers=headers)
        else:
            timeout = (timeouts["connect_timout"], timeouts["read_timeout"])
            res = requests.post(self.url, files=files, data=body, headers=headers, timeout=timeout)
        return res


show_api = ShowApiRequest('http://route.showapi.com/60-27","my_appId', app_id, app_secret)


def show_robot(info, nick_name, img_dir):  # 调用图灵机器人的接口
    show_api.add_body('userid', nick_name)
    if info:
        show_api.add_body('info', info)
    if img_dir:
        show_api.add_file('img', img_dir)
    res = show_api.post()
    data = json.loads(res.text)
    text = data['showapi_res_body'].get('text')
    return data, text


def public_message(msg):  # 返回公用信息
    global run, one_run
    send_name = msg['FromUserName']
    if msg.text == '禁止回复':  # 对于其他人调用
        run = False
    if msg.text == '启动回复':
        run = True

    if send_name == oneself_name:
        if msg.text == '启动回复':  # 对于我来调用
            run = one_run = True
        if msg.text == '禁止回复':
            one_run = False
        if not one_run:
            return 0, 0
    if run:
        nick_name = msg['User']['NickName']
        remark_name = msg['User']['RemarkName']
        return send_name, nick_name or remark_name
    return 0, 0


@itchat.msg_register(itchat.content.TEXT)  # 获得文本信息
def text_reply(msg):
    send_name, call_name = public_message(msg)
    if send_name:
        _, text = show_robot(msg.text, call_name, None)
        if not text:
            text = '人工智障出现问题,等待主人抢修中!'
        text = '[自动回复]:' + text + '---------->>>[输入:禁止回复,就停止机器回复.输入:启动回复,就会启动机器回复]'
        itchat.send_msg(text, send_name)


@itchat.msg_register(itchat.content.PICTURE)  # 获得图片信息
def img_reply(msg):
    send_name, call_name = public_message(msg)
    if send_name:
        img_address = rec_tmp_dir + msg['FileName']
        msg.download(img_address)
        _, text = show_robot(None, call_name, img_address)
        if text:
            text = '[自动回复]:' + text
            itchat.send_msg(text, send_name)


def oneself(wx_name):  # 获得自己的信息
    global oneself_name
    one = itchat.search_friends(name=wx_name)
    oneself_name = one[0]['UserName']


def auto_start(wx_name):
    itchat.auto_login(hotReload=True)
    oneself(wx_name)  # 输入自己的微信名
    itchat.run()


if __name__ == '__main__':
    auto_start(wx_name='Jtyoui')  # 输入自己的微信名,这个是自己取的名字
