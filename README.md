# pyset

#### 介绍
这是一个Python模块集合

## 上传命令
    python setup.py bdist_wheel
    twine upload dist/*

## setup配置
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
        platforms="any",
        package_data={'': ['*']},
        classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        zip_safe=False
    )
