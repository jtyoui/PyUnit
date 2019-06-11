# **Language** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 处理语言的模块
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-语言-black.svg)]()


#### 安装
    pip install jtyoui

#### 处理汉语中的简体字与繁体字
```python
from jtyoui.language import han
if __name__ == '__main__':
    j = han.j_to_f('千载正字一夕改,如今吾辈来重光!')
    print(''.join(j))
    f = han.f_to_j('千載正字一夕改,如今吾輩來重光!')
    print(''.join(f))
```

#### 将汉字转为拼音
```python
from jtyoui.language import load_pin_yin,chinese_to_pin_yin
if __name__ == '__main__':
    load = load_pin_yin(True) #带声调
    print(chinese_to_pin_yin(load, '我喜欢你！'))
    # ['wǒ', 'xǐ', 'huān', 'nǐ'] 
    
    load = load_pin_yin(False) #不带声调
    print(chinese_to_pin_yin(load, '你好！世界'))
    # ['ni', 'hao', 'shi', 'jie']
```

### 翻译
```python
import jtyoui
if __name__ == '__main__':
    print(jtyoui.translate_to_chinese('good', jtyoui.Languages.English))  # 英语
    print(jtyoui.translate_to_chinese('アベンジャーズ', jtyoui.Languages.Japanese))  # 日语
    print(jtyoui.translate_to_chinese('안녕하세요', jtyoui.Languages.Korean))  # 韩语
    print(jtyoui.translate_to_chinese('Bonjour', jtyoui.Languages.French))  # 法语
    print(jtyoui.translate_to_chinese('Hallo', jtyoui.Languages.German))  # 德语
    print(jtyoui.translate_to_chinese('Amor', jtyoui.Languages.Spanish))  # 西班牙语

```

### 拼音纠错
```python
from jtyoui.language import ChineseError
if __name__ == '__main__':
    ce = ChineseError(['六盘水钟山区'])
    print(ce.error_word('六盘水综三去'))
```

### 百度翻译(需要增加cookie，获得cookie的方法是用浏览器使用一次百度翻译)
```python
from jtyoui.language import bai_du_translate,BaiDuLanguage
if __name__ == '__main__':
    c = 'BAIDUID=1E9344586B339BDFE673A622D274BAD9:FG=1; BIDUPSID=1E9344586B339BDFE673A622D274BAD9; PSTM=1551668971; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; from_lang_often=%5B%7B%22value%22%3A%22dan%22%2C%22text%22%3A%22%u4E39%u9EA6%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1559124247,1559526164,1559625839,1560239569; delPer=0; H_PS_PSSID=1421_21110_29135_29237_28518_29099_28839; PSINO=6; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1560242851; yjs_js_security_passport=412be9bc7e1f3b3ca2628a701b66667a703c1b81_1560242855_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%5D'
    p = bai_du_translate('https://fanyi.baidu.com/v2transapi', 'goods', BaiDuLanguage.English, BaiDuLanguage.Chinese, c)
    print(p)
```

***
[1]: https://blog.jtyoui.com