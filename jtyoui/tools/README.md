# **Tools** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 这是一个工具模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/工具-Tools-black.svg)]()


#### 安装
    pip install jtyoui


### 使用
```python
from jtyoui.tools import Tool,StringTime
if __name__ == '__main__':
    tool=Tool( '我家在贵州省遵义县的一个地方是虾子')
    i_s = tool.index_select_string('01056666600000056', '56+')
    print(i_s)  #['贵州省遵义县', '虾子']
    
    tool.string = '一、相亲最大的好处是。二、想要什么婚姻。三五、开放型的婚姻是凉鞋。三、'
    t_s = tool.split('[一二三四五六七八九十]+、', retain=True)
    print(t_s)#['一、相亲最大的好处是。', '二、想要什么婚姻。', '三五、开放型的婚姻是凉鞋。', '三、']
    
    tool.string = '我家在贵州省遵义县的一个地方是虾子'
    s_i = tool.string_select_index(ls=['贵州省', '遵义县', '虾子'], start_name='5', end_name='6')
    print(s_i)#['O', 'O', 'O', '5', '6', '6', '5', '6', '6', 'O', 'O', 'O', 'O', 'O', 'O', '5', '6']
     
    st = StringTime('二零零七年十月三十一号下午2点半')
    print(st.find_times()) # 2007-10-31 14:30:00
```

***
[1]: https://blog.jtyoui.com