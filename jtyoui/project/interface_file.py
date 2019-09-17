#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/9/17 10:49
# @Author: Jtyoui@qq.com
import os


def create_flaskenv(project_address):
    project_name = os.path.basename(project_address)
    with open(project_address + os.sep + '.flaskenv', 'w', encoding='utf-8', newline='\n') as f:
        f.write(f'FLASK_APP = {project_name}.app\n')
        f.write('FLASK_ENV = development\n')
        f.write('FLASK_DEBUG = 0')


def create_app_sh(project_address):
    project_name = os.path.basename(project_address)
    with open(project_address + os.sep + 'app.sh', 'w', encoding='utf-8', newline='\n') as f:
        f.write('#!/bin/bash\n')
        f.write(f'uwsgi --http :5000 --ini /mnt/{project_name}/uwsgi.ini')


def create_config(project_address):
    with open(project_address + os.sep + 'config.py', 'w', encoding='utf-8', newline='\n') as f:
        import time
        t = time.strftime('%Y/%m/%d %H:%M:%S')
        text = f"""#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : {t}
# @Author: Jtyoui@qq.com
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 当前文档地址
Log = BASE_DIR + os.sep + 'logs'  # 日志存放地址


# 数据库，app配置
class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_RECYCLE = 10 * 60

    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gzxiaoi@222.85.230.14:13218/xfj_final?charset=utf8'

  
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gzxiaoi@222.85.230.14:13218/xfj_final?charset=utf8'


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gzxiaoi@222.85.230.14:13218/xfj_final?charset=utf8'


CONFIG = {{
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}}
"""
        f.write(text)


def create_dockerfile(project_address):
    with open(project_address + os.sep + 'Dockerfile', 'w', encoding='utf-8', newline='\n') as f:
        f.write('FROM python:3.7\n')
        f.write('COPY requirements.txt /tmp/\n')
        f.write('RUN pip install --no-cache-dir -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple\n')
        f.write('RUN pip install --no-cache-dir uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple\n')
        f.write('CMD [ "python" ]\n')


def create_uwsgi(project_address):
    project_name = os.path.basename(project_address)
    with open(project_address + os.sep + 'uwsgi.ini', 'w', encoding='utf-8', newline='\n') as f:
        text = f"""[uwsgi]
project = {project_name}
base = /mnt
chdir = %(base)/%(project)
module = %(project).app:app
master = true
processes = 10
cheaper = 2
cheaper-initial = 5
cheaper-step = 1
cheaper-algo = spare
cheaper-overload = 5
        """
        f.write(text)


def create_requirements(project_address):
    with open(project_address + os.sep + 'requirements.txt', 'w', encoding='utf-8', newline='\n') as f:
        text = """Flask
PyMySQL
jtyoui
flask_sqlalchemy"""
        f.write(text)


def create_all(project_address):
    create_flaskenv(project_address)
    create_app_sh(project_address)
    create_config(project_address)
    create_dockerfile(project_address)
    create_requirements(project_address)
    create_uwsgi(project_address)


if __name__ == '__main__':
    create_all(os.path.dirname(__file__))
