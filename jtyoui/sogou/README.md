# **SoGou** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]


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
    sg = SoGou('动物')  # 获取搜索关键字下的词库
    for s in sg.load_url:  # 遍历关键字下的URL
        print(s)
        '''
        https://pinyin.sogou.com/d/dict/download_cell.php?id=15206&name=动物词汇大全【官方推荐】
        https://pinyin.sogou.com/d/dict/download_cell.php?id=71952&name=猫咪种类大全【官方推荐】
        https://pinyin.sogou.com/d/dict/download_cell.php?id=37729&name=a wolf
        https://pinyin.sogou.com/d/dict/download_cell.php?id=2694&name=ecology
        https://pinyin.sogou.com/d/dict/download_cell.php?id=53028&name=包涵动物的成语
        https://pinyin.sogou.com/d/dict/download_cell.php?id=7945&name=哺乳动物名
        https://pinyin.sogou.com/d/dict/download_cell.php?id=22897&name=常见贝壳
        https://pinyin.sogou.com/d/dict/download_cell.php?id=7943&name=虫蛇类名词
        https://pinyin.sogou.com/d/dict/download_cell.php?id=8085&name=淡水热带鱼
        https://pinyin.sogou.com/d/dict/download_cell.php?id=8261&name=动物百科词条
        https://pinyin.sogou.com/d/dict/download_cell.php?id=37086&name=动物词汇大全
        https://pinyin.sogou.com/d/dict/download_cell.php?id=68644&name=动物世界
        https://pinyin.sogou.com/d/dict/download_cell.php?id=24696&name=动物疫病病名
        https://pinyin.sogou.com/d/dict/download_cell.php?id=12754&name=浮游动物
        https://pinyin.sogou.com/d/dict/download_cell.php?id=57920&name=干支魂
        https://pinyin.sogou.com/d/dict/download_cell.php?id=22876&name=广东贝类
        https://pinyin.sogou.com/d/dict/download_cell.php?id=7938&name=国家一级保护动物
        https://pinyin.sogou.com/d/dict/download_cell.php?id=6725&name=海水鱼类名称
        https://pinyin.sogou.com/d/dict/download_cell.php?id=72186&name=海洋动物
        https://pinyin.sogou.com/d/dict/download_cell.php?id=13136&name=河南辉县方言
        https://pinyin.sogou.com/d/dict/download_cell.php?id=59019&name=猴赛雷
        https://pinyin.sogou.com/d/dict/download_cell.php?id=53917&name=狐类名录
        https://pinyin.sogou.com/d/dict/download_cell.php?id=43999&name=虎皮鹦鹉种类
        https://pinyin.sogou.com/d/dict/download_cell.php?id=7935&name=金鱼名
        https://pinyin.sogou.com/d/dict/download_cell.php?id=93784&name=昆虫名录2
        https://pinyin.sogou.com/d/dict/download_cell.php?id=50218&name=灭绝哺乳动物
        https://pinyin.sogou.com/d/dict/download_cell.php?id=8088&name=名犬大全
        https://pinyin.sogou.com/d/dict/download_cell.php?id=13735&name=鸟名
        https://pinyin.sogou.com/d/dict/download_cell.php?id=50224&name=啮齿动物名
        https://pinyin.sogou.com/d/dict/download_cell.php?id=8055&name=啮齿目动物
        https://pinyin.sogou.com/d/dict/download_cell.php?id=7936&name=热带鱼名
        https://pinyin.sogou.com/d/dict/download_cell.php?id=8058&name=蛇类名录
        https://pinyin.sogou.com/d/dict/download_cell.php?id=50217&name=史前哺乳动物
        https://pinyin.sogou.com/d/dict/download_cell.php?id=65153&name=世界名猫大全
        https://pinyin.sogou.com/d/dict/download_cell.php?id=7946&name=世界名犬
        https://pinyin.sogou.com/d/dict/download_cell.php?id=44642&name=世界鸟类
        https://pinyin.sogou.com/d/dict/download_cell.php?id=1330&name=世界犬种大全
        https://pinyin.sogou.com/d/dict/download_cell.php?id=6200&name=世界鱼类名录
        https://pinyin.sogou.com/d/dict/download_cell.php?id=12759&name=水产生物名称
        https://pinyin.sogou.com/d/dict/download_cell.php?id=33360&name=水生动物医学
        https://pinyin.sogou.com/d/dict/download_cell.php?id=3246&name=水族水草造景相关
        https://pinyin.sogou.com/d/dict/download_cell.php?id=14076&name=台湾贝类
        https://pinyin.sogou.com/d/dict/download_cell.php?id=37601&name=血结缔
        https://pinyin.sogou.com/d/dict/download_cell.php?id=39477&name=盐城工学院
        https://pinyin.sogou.com/d/dict/download_cell.php?id=2604&name=鱼 终生生活在水里、用鳃呼吸、用鳍游泳的脊椎动物
        https://pinyin.sogou.com/d/dict/download_cell.php?id=59377&name=玉米蛇
        https://pinyin.sogou.com/d/dict/download_cell.php?id=2660&name=粤语词库
        https://pinyin.sogou.com/d/dict/download_cell.php?id=63943&name=中国常见园林害虫
        https://pinyin.sogou.com/d/dict/download_cell.php?id=6616&name=中国淡水鱼类名称
        https://pinyin.sogou.com/d/dict/download_cell.php?id=41667&name=中国观鸟年报-中国鸟类名录3.0
        https://pinyin.sogou.com/d/dict/download_cell.php?id=93782&name=中国昆虫名录1
        https://pinyin.sogou.com/d/dict/download_cell.php?id=84299&name=中国鸟类名录4.0词库
        https://pinyin.sogou.com/d/dict/download_cell.php?id=62667&name=中国爬行动物名录
        https://pinyin.sogou.com/d/dict/download_cell.php?id=61881&name=中国有尾目动物名录词库
        https://pinyin.sogou.com/d/dict/download_cell.php?id=1336&name=重点保护野生动物名录
        https://pinyin.sogou.com/d/dict/download_cell.php?id=8061&name=鹦鹉种类
        https://pinyin.sogou.com/d/dict/download_cell.php?id=8059&name=蜥类名录
        https://pinyin.sogou.com/d/dict/download_cell.php?id=8084&name=蟋蟀名称
        https://pinyin.sogou.com/d/dict/download_cell.php?id=28826&name=鰟鮍类，鱊类
        '''
    txt = sg.load_word(' https://pinyin.sogou.com/d/dict/download_cell.php?id=8084&name=蟋蟀名称')  # 选择具体的下载词库链接
    print(txt)  # 打印
  
```

### 搜索到的全部下载（支持模糊搜索）
```python
from jtyoui.sogou import SoGou
if __name__ == '__main__':
    sg = SoGou('蟋蟀名称')  # 获取搜索关键字下的词库
    txt = sg.load_word()  # 下载动物类全部信息
    print(txt)  # 打印
        
```

#### 打印格式：是一个键值对。键是词库名，值的词库内容

    {'动物词汇大全【官方推荐】': ['阿比西尼亚猫', '阿博胡鲶', '阿勃劳棱鲱'....]}

### 搜狗词库表
[点击查询搜狗词库表](https://gitee.com/tyoui/word)    
    

[1]: https://blog.jtyoui.com