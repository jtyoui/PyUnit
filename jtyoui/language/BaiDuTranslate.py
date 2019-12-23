#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/11 17:05
# @Author: Jtyoui@qq.com
from jtyoui.web import post, get_js

_sign = """
function a(r, o) {
    for (var t = 0; t < o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
        a = "+" === o.charAt(t + 1) ? r >>> a: r << a,
        r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
    }
    return r
}
var C = null;
var hash = function(r, _gtk) {
    var o = r.length;
    o > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(o / 2) - 5, 10) + r.substr( - 10, 10));
    var t = void 0,
    t = null !== C ? C: (C = _gtk || "") || "";
    for (var e = t.split("."), h = Number(e[0]) || 0, i = Number(e[1]) || 0, d = [], f = 0, g = 0; g < r.length; g++) {
        var m = r.charCodeAt(g);
        128 > m ? d[f++] = m: (2048 > m ? d[f++] = m >> 6 | 192 : (55296 === (64512 & m) && g + 1 < r.length && 56320=== 
        (64512 & r.charCodeAt(g + 1)) ? (m = 65536 + ((1023 & m) << 10) + (1023 & r.charCodeAt(++g)), d[f++] = m >> 18
        |240, d[f++] = m >> 12 & 63 | 128) : d[f++] = m >> 12 | 224, d[f++] = m >> 6 & 63 | 128), d[f++] = 63 & m | 128)
    }
    for (var S = h,
    u = "+-a^+6",
    l = "+-3^+b+-f",
    s = 0; s < d.length; s++) S += d[s],
    S = a(S, u);
    return S = a(S, l),
    S ^= i,
    0 > S && (S = (2147483647 & S) + 2147483648),
    S %= 1e6,
    S.toString() + "." + (S ^ h)
}
"""


def bai_du_translate(word, from_, to_, cookie):
    """百度翻译：需要自己增加cookie

    :param word: 翻译的单词
    :param from_: 该单词是什么语言
    :param to_: 翻译成什么语言
    :param cookie: 百度翻译网址cookie
    :return: 返回json数据
    """
    params = {}
    gtk = '320305.131321201'
    sign = get_js(_sign, 'hash', [word, gtk])
    params['query'] = word
    params['from'] = from_
    params['to'] = to_
    params['sign'] = sign
    params['token'] = 'dbb0f2ac18d5288a0ab1c09e69092827'
    response = post(url='https://fanyi.baidu.com/v2transapi', params=params, cookie=cookie)
    json = response.json()
    return json


class BaiDuLanguage:
    English = 'en'  # 英语
    Chinese = 'zh'  # 中文
    Japan = 'jp'  # 日本
    Arab = 'ara'  # 阿拉伯
    Estonia = 'est'  # 爱沙尼亚
    Bulgarian = 'bul'  # 保加利亚语
    Polish = 'pl'  # 波兰语
    Danish = 'dan'  # 丹麦语
    German = 'de'  # 德语
    Russian = 'ru'  # 俄语
    French = 'fra'  # 法语
    Finnish = 'fin'  # 芬兰语
    Korean = 'kor'  # 韩语
    Dutch = 'nl'  # 荷兰语
    Czech = 'cs'  # 捷克语
    Romanian = 'rom'  # 罗马尼亚语
    Portuguese = 'pt'  # 葡萄牙语
    Swedish = 'swe'  # 瑞典语
    Slovenian = 'slo'  # 斯洛文尼亚语
    Thai = 'th'  # 泰语
    Spanish = 'spa'  # 西班牙语
    Greek = 'el'  # 希腊语
    Hungarian = 'hu'  # 匈牙利语
    Italian = 'it'  # 意大利语
    Vietnamese = 'vie'  # 越南语
    Cantonese = 'yue'  # 粤语


if __name__ == '__main__':
    c = 'BAIDUID=1E9344586B339BDFE673A622D274BAD9:FG=1; BIDUPSID=1E9344586B339BDFE673A622D274BAD9; PSTM=1551668971; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; from_lang_often=%5B%7B%22value%22%3A%22dan%22%2C%22text%22%3A%22%u4E39%u9EA6%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1559124247,1559526164,1559625839,1560239569; delPer=0; H_PS_PSSID=1421_21110_29135_29237_28518_29099_28839; PSINO=6; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1560242851; yjs_js_security_passport=412be9bc7e1f3b3ca2628a701b66667a703c1b81_1560242855_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%5D'
    p = bai_du_translate('hello', BaiDuLanguage.English, BaiDuLanguage.Chinese, c)
    print(p)
