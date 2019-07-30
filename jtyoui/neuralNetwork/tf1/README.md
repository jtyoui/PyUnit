# **TF1** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## tensorflow版本1.0项目集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()


### 安装
    pip install jtyoui

## 临时镜像源
    pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple

## 设置默认pip源
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

## 初始化第三方库
    tensorflow==1.14.0
    numpy
    pillow


## 手写数据训练和测试
```python
from jtyoui.neuralNetwork.tf1.HandWritingRecognition import train,test
if __name__ == '__main__':
    train()  # 训练
    test('./5.jpg')  # 测试

# 各参数调整
input_node = 784  # 输入节点
output_node = 10  # 输出节点
layer_node = 500  # 隐藏层节点
regularization = 0.001  # 正则值
bitch_size = 200  # 批量大小
learning_rates = 0.1  # 初始学习率
learning_rate_decay = 0.99  # 学习衰减率
steps = 50000  # 训练步数
moving_average_decay = 0.99  # 滑动平均衰减值
model_save_path = './model/'  # 保存文件夹
model_name = 'mist_model'  # 保存名字
```

## 实体识别
    需要修改训练数据，格式要保证一致，修改位置在train方法
```python
from jtyoui.neuralNetwork.tf1.LSTM_CRF import *

def read_data():#需要重新，保证格式一致
    pass
if __name__ == '__main__':
    train()
    # test([[1, 2, 3]])

# 各参数
batch_size = 64
epoch_num = 20
hidden_dim = 300
embeddings = 300
dropout_keep_prob = 0.5
lr = 0.001
clip_grad = 5.0
model_path = './model/'
tag2label = {"O": 0,
             "B-a": 1, "I-a": 2,
             "B-b": 3, "I-b": 4,
             "B-c": 5, "I-c": 6
             }
```

***
[1]: https://blog.jtyoui.com