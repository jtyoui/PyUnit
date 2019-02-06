# **安装步骤** [![](https://github.com/zhangwei0530/logo/blob/master/logo/photolog.png)][1]


## 上传命令
    打包
    python setup.py bdist_wheel
    安装在本机测试
    pip install --upgrade dist\* 
    上传到pipy
    twine upload dist\*

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