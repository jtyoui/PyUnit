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

### 查询字符串时间
```python
from jtyoui.tools import StringTime

if __name__ == '__main__':
    # 默认是当日期
    st = StringTime('二零零七年十月三十一号下午2点半')
    print(st.find_times())
    st.sentence = '下周星期一下午2点半开会'
    print(st.find_times())
    print('-----------------------------------')
    # 切换日期
    st = StringTime('下周星期一下午2点半开会', '2019-4-17 00:00:00')
    print(st.find_times())

```


### 时间格式表
    　%H 　小时(以00-23来表示)。
    　%I 　小时(以01-12来表示)。
    　%K 　小时(以0-23来表示)。
    　%l 　小时(以0-12来表示)。
    　%M 　分钟(以00-59来表示)。
    　%P 　AM或PM。
    　%r 　时间(含时分秒，小时以12小时AM/PM来表示)。
    　%s 　总秒数。起算时间为1970-01-01 00:00:00 UTC。
    　%S 　秒(以本地的惯用法来表示)。
    　%T 　时间(含时分秒，小时以24小时制来表示)。
    　%X 　时间(以本地的惯用法来表示)。
    　%Z 　市区。
    　%a 　星期的缩写。
    　%A 　星期的完整名称。
    　%b 　月份英文名的缩写。
    　%B 　月份的完整英文名称。
    　%c 　日期与时间。只输入date指令也会显示同样的结果。
    　%d 　日期(以01-31来表示)。
    　%D 　日期(含年月日)。
    　%j 　该年中的第几天。
    　%m 　月份(以01-12来表示)。
    　%U 　该年中的周数。
    　%w 　该周的天数，0代表周日，1代表周一，异词类推。
    　%x 　日期(以本地的惯用法来表示)。
    　%y 　年份(以00-99来表示)。
    　%Y 　年份(以四位数来表示)。
    　%n 　在显示时，插入新的一行。
    　%t 　在显示时，插入tab。
    　MM 　月份(必要)。
    　DD 　日期(必要)。
    　hh 　小时(必要)。
    　mm 　分钟(必要)。
    　CC 　年份的前两位数(选择性)。
    　YY 　年份的后两位数(选择性)。
    　ss 　秒(选择性)。
    　-d<字符串> 　显示字符串所指的日期与时间。字符串前后必须加上双引号。
    　-s<字符串> 　根据字符串来设置日期与时间。字符串前后必须加上双引号。
    　-u 　显示GMT。

### 造句
```python
from jtyoui.tools import Sentence
if __name__ == '__main__':
    s = Sentence()
    data = s['我爱你']
    for jz in data:
        print(jz)
    # (1) 洁白的雪，我爱你，我爱你的纯洁。你把大地装饰得一片银白，你把大地打扮得多么美丽。
    # (2) 我爱你，星星，你有着迷人的魅力，你有着调皮捣蛋的性格，你有着五彩缤纷的衣服。
    # (3) 我爱你大海，爱你的浩瀚无际，也爱你的美丽，更爱你的神秘感。大海你是一位宽容的母亲。大海，你的宽容大度，是我们学习的榜样。
    # (4) 我爱你黄河，你的身躯里散发着泥土的芳香。我爱你黄河，你的身躯上闪耀着黄色的光芒。我爱你黄河，你的脉搏如此强壮，震撼着华夏儿女的心房。我爱你黄河，你的浩瀚与日月同辉，在我心中激荡。zaojv.com
    # (5) 我爱你，不是因为你是一个怎样的人，而是因为我喜欢与你在一起时的感觉。
    #  ......
    #  ......
    # (153) 我爱你可以为你放弃一切！包括你。
    # (154) 说什么我爱你都他妈的对不起。
    # (155) 你问我爱你有多深，拳头代表我的心。

```

***
[1]: https://blog.jtyoui.com