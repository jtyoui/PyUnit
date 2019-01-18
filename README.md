# **安装步骤** [![tyoui](https://github.com/zhangwei0530/logo/blob/master/logo/photolog.png?raw=true)][1]

[![](https://github.com/zhangwei0530/logo/blob/master/logo/logo.png?raw=true)][1]

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

### .pypirc 放在 C:\Users\Administrator
    [distutils]
    index-servers=pypi
    
    [pypi]
    repository = https://upload.pypi.org/legacy/
    username: xxxxxxxx
    password: yyyyyyyy



[1]: https://www.jtyoui.com