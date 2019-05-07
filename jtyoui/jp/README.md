# **JP** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 日语单词翻译模块集合
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/日语-JP-black.svg)]()


#### 安装
    pip install jtyoui
    pip install janome
    pip install bs4


### 日语翻译
节选：2011年日语高考真题.txt

    車椅子の選手がいる。足や腕のない選手もいる。さまざまな困難を乗り越える意志と競技で見せる力強さに驚き、感動する日々が続く。北京パラリンピック（残奥会）が佳境を迎えている。
    競輸選手だった石井雅史選手は練習中に自動車と衝突、高次脳機能障害になった。記憶力が減退し、集中力が続かない。職業としての自転車は辞めるしかなかった。治療を重ね、再び自転車に乗ったのは５年後のことだ。
    今回は４年前のオリンピック大会より金メダルの数を１０パーセント減らした。数人の出場で優勝を争うような例を減らして、メダルの価値を上げるためだ。
    競技レベルの向上にしたがって、競泳や卓球では北京オリンピックと両方に出場した選手も出てきた。
    
    
```python
import jtyoui
if __name__ == '__main__':
    Response_Headers="""cookie: HJ_UID=a0752831-ba30-9486-ddc8-66bcbb7f303a; _REF=https://www.baidu.com/link?url%3DTvv2c125EbCEB2T5xBtSlQeMb4zSO1v2ZkeB8uvhFXacQdks-Z0OXCabLXXX-Wpa&wd%3D&eqid%3D9cbe02970005752c000000025cd1684b; _REG=www.baidu.com|; _SREG_3=www.baidu.com|; HJ_CST=0; HJ_CSST_3=0; _SREF_3=https://www.baidu.com/link?url%3DTvv2c125EbCEB2T5xBtSlQeMb4zSO1v2ZkeB8uvhFXacQdks-Z0OXCabLXXX-Wpa&wd%3D&eqid%3D9cbe02970005752c000000025cd1684b; TRACKSITEMAP=3%2C6%2C; HJ_SID=5b45f4b2-9ae1-4a93-803b-7e2d08faba78; HJ_SSID_3=e959e1f7-6b25-4c49-a26d-a914297c0f32
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"""
    c=jtyoui.cut('2011年日语高考真题.txt')
    jtyoui.analysis(c,Response_Headers)#如果不行的话，记得换缓存，缓存获取方法，打开小D网站，按F12获取cookie、替换Response_Headers
```
翻译结果：

    かきょう(佳境)	<名>	佳境，兴趣浓厚的境地；风景优美的地方
    むかえる(迎える)	<他Ⅱ>	迎，迎
    れんしゅう(練習)	<名・他Ⅲ>	练习，反复学习
    じどうしゃ(自動車)	<名>	汽车
    しょうとつ(衝突)	<自Ⅲ>	撞上，冲撞，碰上；矛盾，不一致；冲突
    こうじ(高次)	<名>	高度
    きのう(機能)	<自Ⅲ>	机能；功能；作用
    きおく(記憶)	<名>	记忆，记忆力，记性
    げんたい(減退)	<名・自Ⅲ>	衰退，减退
    しゅうちゅう(集中)	<名・自他Ⅲ>	集中
    しょくぎょう(職業)	<名>	职业
    ちりょう(治療)	<名・他Ⅲ>	治疗，医疗，医治，治
    かさねる(重ねる)	<他Ⅱ>	再次，多次，重复，反复；摞，重叠起来
    ふたたび(再び)	<副>	再，又，重
    たいかい(大会)	<名>	大会
    きろく(記録)	<名・他Ⅲ>	记载，记录；抄写下来的文件；竞赛等的最好成绩
    ゆうしょう(優勝)	<自Ⅲ>	最优秀；冠军
    スタート	<名>	【英】start ;出发，起动，开始，开端
    こんかい(今回)	<名>	此次，此番，这回
    オリンピック	<名>	【英】Olympic；奥林匹克运动会，奥运会
    きんメダル(金メダル)	<名>	金质奖章，金牌
    パーセント	<名>	percent ;百分率，百分数，百分之……
    へらす(減らす)	<他Ⅰ>	减少，削减，缩减
    しゅつじょう(出場)	<名・自Ⅲ>	出场，参加
    あらそう(争う)	<他Ⅰ>	争，争夺；斗争；奋斗；争论，争辩；竞争，对抗
    メダル	<名>	【英】medal；奖章，奖牌，纪念章
    かち(価値)	<名>	价值
    あげる(上げる)	<自Ⅱ>	潮水上涨
    こうじょう(向上)	<名・自Ⅲ>	向上，提高；进步
    したがう	<自Ⅰ>	跟随；服从，听从，遵从，顺从；按照，适应；伴随，随着；顺，沿；仿效，仿照
    きょうえい(競泳)	<名・自Ⅲ>	;游泳比赛
    たっきゅう(卓球)	<名>	乒乓球
    りょうほう(両方)	<名>	两边，两方；两个方面，两个方向；双方，两者，两方
    ちょうてん(頂点)	<名>	〈数〉顶点
    さんろく(山麓)	<名>	山麓

***
[1]: https://blog.jtyoui.com