# **SoGou** [![](https://github.com/zhangwei0530/logo/blob/master/logo/photolog.png)][1]


## 搜狗下载词库
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-搜狗库爬取-black.svg)]()

## 安装
    pip install jtyoui

## 运行代码
```python
    from jtyoui.sogou import SoGou
    
     # 下载具体的一个
    if __name__ == '__main__':
        sg = SoGou('动物词汇大全【官方推荐】')  # 获取搜索关键字下的词库
        for s in sg.load_url:  # 遍历关键字下的URL
            txt = sg.load_word(s)  # s就是具体的下载词库链接
            print(txt)  # 打印
      
     # 搜索到的全部下载
     if __name__ == '__main__':
        sg = SoGou('动物词汇大全【官方推荐】')  # 获取搜索关键字下的词库
        txt = sg.load_word()  # 下载
        print(txt)  # 打印
        
```

#### 打印格式：是一个键值对。键是词库名，值的词库内容

    {'动物词汇大全【官方推荐】': ['阿比西尼亚猫', '阿博胡鲶', '阿勃劳棱鲱'....]}
    
    

[1]: https://www.jtyoui.com