# **PySet** [![tyoui](https://github.com/zhangwei0530/logo/blob/master/logo/photolog.png?raw=true)][1]

[![](https://github.com/zhangwei0530/logo/blob/master/logo/logo.png?raw=true)][1]

## 这是一个Python模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()


#### 安装
    pip install jtyoui

## 上传命令
    python setup.py bdist_wheel
    twine upload dist/*

## setup.py配置
    from setuptools import setup, find_packages
    setup(
    name='jtyoui',
    version='19.1.16',
    description='This is my collection bag.',
    url='https://github.com/jtyoui',
    author='jtyoui',
    author_email='jtyoui@qq.com',
    license='MIT Licence',
    packages=find_packages(),
    platforms="window",
    package_data={'': ['*']},
    install_requires=['PyQt5', 'PyMuPDF', 'requests', 'pygame'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
    )
    
***
[1]: https://www.jtyoui.com