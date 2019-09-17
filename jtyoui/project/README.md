# **project** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 这是一个简单的生产接口文件的项目
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/project-接口文件-black.svg)]()


### 安装
    pip install jtyoui

### 创建docker接口文件
```python
from jtyoui.project import create_flaskenv,create_app_sh,create_config,create_dockerfile,create_requirements,create_uwsgi
import os
if __name__ == '__main__':
    project_address=os.path.basename(__file__)
    create_flaskenv(project_address)
    create_app_sh(project_address)
    create_config(project_address)
    create_dockerfile(project_address)
    create_requirements(project_address)
    create_uwsgi(project_address)
```

### 一步添加
```python
from jtyoui.project import create_all
import os
if __name__ == '__main__':
    project_address=os.path.basename(__file__)
    create_all(project_address)
```
***
[1]: https://blog.jtyoui.com