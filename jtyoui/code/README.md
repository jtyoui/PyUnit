# **验证码识别** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]


[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-jtyoui.code-black.svg)]()
### 安装
    pip install jtyoui


#### 使用说明   

```python
    from jtyoui.code import cr
    
    if __name__ == '__main__':
        # 第一个参数是要识别验证码照片的地址。必填。str类型
        # 第二参数是图片类型(看下面code_type类型)，必填，int类型
        # 第三个参数是等待时间的延迟。默认是60秒。非必填，int类型
        code = cr.decode(filename=None, code_type=None, timeout=60)
        print(code)
```

### code_type类型，验证码类型都是4位。
    验证码类型	验证码描述
   
    1000	不限长度的英文+数字
    10x     x位英文+数字,x的取值范围[01,20],比如：1003 表示3位英文+数字，1020表示20位英文+数字
   
    2000	不限长度的纯汉字
    20x     x位纯汉字,x的取值范围[01,20],比如：2003 表示3位纯汉字，2020表示20位纯汉字
    
    3000	不限长度的纯英文
    30x     x位纯英文,x的取值范围[01,20],比如：3003 表示3位纯英文，3020表示20位纯英文
    
    4000	不限长度的纯数字
    40x     x位纯数字,x的取值范围[01,20],比如：4003 表示3位纯数字，4020表示20位纯数字
    
    特殊字符
    5000	不定长汉字英文数字、符号、空格
    5001	不定长汉字英文数字、符号、空格（区分大小写）
    5006	6位英文数字符号
    5000	不定长汉字英文数字、符号、空格
    6100	google验证码（只输入斜体部分）
    6200	九宫格坐标验证码（9个汉字选出4个）
    6201	九宫格坐标验证码（9个汉字选出1-4个）
    6300	加减乘除计算题
    6301	知识问答计算题（结果为数字）
    6400	4组汉字4选1
    6500	选出两个相同动物序号
    6600	单选题根据问题选择答案编号
    6601	单选题选出字符所在位置
    6602	单选题有多少个指定的汉字
    6701	多选题返回数字（8个图中选择1-8个）
    6101	简单问答题（拼音字母、汉字、计数、认图）
    4105	模糊动态5位数字
    
    
[1]: https://blog.jtyoui.com