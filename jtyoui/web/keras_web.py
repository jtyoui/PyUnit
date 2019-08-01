#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 13:10
# @Email  : jtyoui@qq.com
# @Software: PyCharm
import time
from flask import Flask, Response, send_file, request
import gevent
from gevent.pywsgi import WSGIServer
from gevent.queue import Queue

app = Flask(__name__)
subscriptions = []


@app.route('/health/', methods=['GET'])
def health():
    return '200 OK'


@app.route('/', methods=['GET'])
def home():
    return send_file('./test.html')


class ServerSentEvent(object):

    def __init__(self, data):
        self.data = data
        self.event = None
        self.id = None
        self.desc_map = {
            self.data: "data",
            self.event: "event",
            self.id: "id"
        }

    def encode(self):
        if not self.data:
            return ""
        lines = ["%s: %s" % (v, k) for k, v in self.desc_map.items() if k]
        return "%s\n\n" % "\n".join(lines)


@app.route("/publish/epoch/end/", methods=['POST'])
def publish():
    payload = request.form.get('data')

    def notify():
        msg = str(time.time())
        for sub in subscriptions[:]:
            sub.put(payload)

    gevent.spawn(notify)
    return "OK"


@app.route("/subscribe/epoch/end/")
def subscribe():
    def gen():
        q = Queue()
        subscriptions.append(q)
        try:
            while True:
                result = q.get()
                event = ServerSentEvent(str(result))
                yield event.encode()
        except GeneratorExit:
            subscriptions.remove(q)

    return Response(gen(), mimetype="text/event-stream")


def remote_monitor(listener='localhost', port=9000):
    print(f'点击链接：http://{listener}:{port}\t')
    server = WSGIServer((listener, port), app)
    server.serve_forever()


if __name__ == '__main__':
    remote_monitor(listener='127.0.0.1')
