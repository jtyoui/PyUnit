# **Logger** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 日志处理模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/日志-logger-black.svg)]()


## 安装
    pip install jtyoui

### 加载日志配置
```python
from jtyoui.logger import log_file_config
import logging

if __name__ == '__main__':
    log_file_config()  # 加载默认配置文件，如果要自定义，流程如下：c = get_log_config() 先对c对象进行修改，set_log_file_config(c)
    logging.info('默认加载到root下')

    info = logging.getLogger('info')
    info.info('日志文件写道info.log文件下')

    error = logging.getLogger('error')
    error.error('日志文件写道error.log文件下')
```

### 修改日志文件夹路径
```python
from jtyoui.logger import set_log_file_config,get_log_config
import logging

if __name__ == '__main__':
    g=get_log_config(custom_dir='/temp/logs') 
    set_log_file_config(g)

    info = logging.getLogger('info')
    info.info('日志文件写道info.log文件下')

    error = logging.getLogger('error')
    error.error('日志文件写道error.log文件下')

```
##日志装饰器
```python
from jtyoui.logger import log
if __name__ == '__main__':
    #config_file是日志模板地址
    @log('./ger',config_file=None) #日志保存的目录
    def division():
        s = 1 / 0
        return s


    division()
```

### 日志模块
```log
[loggers]
keys = root,info,error

[handlers]
keys = console,info,error

[formatters]
keys = simpleFormatter

[formatter_simpleFormatter]
format = %(asctime)s - %(module)s - %(thread)d - %(levelname)s : %(message)s
datefmt = %Y-%m-%d %H:%M:%S

[logger_root]
level = INFO
handlers = info,console

[handler_console]
class = StreamHandler
level = INFO
formatter = simpleFormatter
args = (sys.stdout,)

[logger_info]
level = INFO
handlers = info
qualname = info
propagate = 0

[handler_info]
class = FileHandler
formatter = simpleFormatter
args = ('logs/info.log', 'a')
when : D
backupCount = 30

[logger_error]
level = ERROR
handlers = error
qualname = error
propagate = 0

[handler_error]
class = handlers.RotatingFileHandler
formatter = simpleFormatter
args = ('logs/error.log', 'a')
when : D
backupCount = 30
```

***
[1]: https://blog.jtyoui.com