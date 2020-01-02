# **paddle** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## paddle模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()

### 安装
    pip install jtyoui
    pip install paddlepaddle==1.6.1
    
### 默认官方数据集训练的模型（只能识别：人名、地名、机构名）
[点击下载模型](http://oss.tyoui.cn/model.zip)

### docker安装
[点击查看](https://github.com/jtyoui/eboby)


### 默认的参数和映射表
```python
from jtyoui.neuralNetwork import ernie_st,ernie_match,ERNIE_MODEL_PARAMETER,ERNIE_LABEL_MAP
ERNIE_MODEL_PATH = 'D://model' #解压的文件夹的地址
s = ernie_st(ERNIE_MODEL_PATH, ERNIE_MODEL_PARAMETER, ERNIE_LABEL_MAP)
print(ernie_match('我叫刘万光我是贵阳市南明村永乐乡水塘村的村民', s))
```


### 其他模型实体识别
```python
from jtyoui.neuralNetwork import ernie_st,ernie_match
if __name__ == '__main__':
    ERNIE_MODEL_PATH = 'D://modelBS'

    ERNIE_CONFIG = {
        "attention_probs_dropout_prob": 0.1,
        "hidden_act": "relu",
        "hidden_dropout_prob": 0.1,
        "hidden_size": 768,
        "initializer_range": 0.02,
        "max_position_embeddings": 513,
        "num_attention_heads": 12,
        "num_hidden_layers": 12,
        "type_vocab_size": 2,
        "vocab_size": 18000
    }

    ERNIE_LABEL_MAP = {
        "B-PER": 0,  # 人名
        "I-PER": 1,
        "B-ORG": 2,  # 机构名
        "I-ORG": 3,
        "B-LOC": 4,  # 地名
        "I-LOC": 5,
        "B-GUE": 6,  # 办事指南
        "I-GUE": 7,
        "O": 8
    }
    s = ernie_st(ERNIE_MODEL_PATH, ERNIE_CONFIG, ERNIE_LABEL_MAP)
    print(ernie_match('我叫刘万光我是贵阳市南明村永乐乡水塘村的村民', s))
    # [8, 8, 0, 1, 1, 8, 8, 4, 5, 5, 4, 5, 5, 4, 5, 5, 4, 5, 5, 8, 8, 8]
```

### 需要三个条件
    第一个是模型的位置：ERNIE_MODEL_PATH
    第二个是模型的参数：ERNIE_CONFIG
    第三个是模型训练时候的IBO对应的标签和数字映射表：ERNIE_LABEL_MAP
    其中，如果模型的参数没有改变，如果用官网的模型参数，from jtyoui.neuralNetwork import ERNIE_MODEL_PARAMETER
    
### 官网地址
[点击ERNIE查看地址](https://github.com/PaddlePaddle/ERNIE)  


***


[1]: https://blog.jtyoui.com