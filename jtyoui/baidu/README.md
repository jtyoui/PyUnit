# **BaiDu** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## BaiDu资料及与百度有关的内容
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.7-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/百度-BaiDu-black.svg)]()


#### 安装
    pip install jtyoui


### 查询任意实体信息
```python
import jtyoui
if __name__ == '__main__':
    bd = jtyoui.BaiDuInfoSearch('万绮雯')
    print(bd.desc()) # 万绮雯（Joey Meng)，1970年10月2日出生中国香港，演员。
    for name, value in bd.info().items():
        print(name, value)
        # 中文名 万绮雯
        # 外文名 Joey Meng Yee Man
        # 别名 万二蚊、十三万、蚊蚊
        # 国籍 中国
        # 民族 汉
        # 星座 天枰座
        # 血型 A型
        # 身高 171cm
        # 出生地 中国香港
        # 出生日期 1970年10月2日
        # 职业 演员
        # 经纪公司 金石堂演艺娱乐事务所
        # 代表作品 我和僵尸有个约会、 我和春天有个约会、精武门
        # 主要成就 1989年亚洲小姐亚军亚洲电视最佳女主角奖
```

### 下载百度文库
```python
from jtyoui.baidu import BaiDuWenKu
if __name__ == '__main__':
    wk = BaiDuWenKu(url=r'https://wenku.baidu.com/view/f50def7c43323968001c924c.html?sxts=1563610333674') #下载链接
    wk.load(save_path=r'D:')#保存目录
```

***
[1]: https://blog.jtyoui.com