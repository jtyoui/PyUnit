# **imgPDF** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]


## PDF和照片相互装换程序
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)][1]
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)][1]
[![](https://img.shields.io/badge/Email-jtyoui@qq.com-red.svg)]()
[![](https://img.shields.io/badge/项目-jtyoui.imagepdf-black.svg)]()


#### 介绍
PDF和照片可以相互转化


#### 安装教程

    pip install jtyoui


### 执行程序
```python
from jtyoui.imagepdf import start

if __name__ == '__main__':
    start()
```

### 核心代码
```Python
import fitz,glob,os

def get_dir_name(file_dir):
    base_name = os.path.basename(file_dir)  # 获得地址的文件名
    dir_name = os.path.dirname(file_dir)  # 获得地址的父链接
    return dir_name, base_name
    
def image_pdf(file_dir):
    img = file_dir + "/*"  # 获得文件夹下的所有对象
    dir_name, base_name = get_dir_name(file_dir)
    doc = fitz.open()
    for img in sorted(glob.glob(img)):  # 排序获得对象
        img_doc = fitz.open(img)  # 获得图片对象
        pdf_bytes = img_doc.convertToPDF()  # 获得图片流对象
        img_pdf = fitz.open("pdf", pdf_bytes)  # 将图片流创建单个的PDF文件
        doc.insertPDF(img_pdf)  # 将单个文件插入到文档
        img_doc.close()
        img_pdf.close()
    doc.save(dir_name + os.sep + base_name + ".pdf")  # 保存文档
    doc.close()
    
def pdf_image(pdf_name):
    dir_name, base_name = get_dir_name(pdf_name)
    pdf = fitz.open(pdf_name)
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]  # 获得每一页的对象
        trans = fitz.Matrix(1.0, 1.0).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        pm.writePNG(dir_name + os.sep + base_name[:-4] + '_' + '{:0>3d}.png'.format(pg + 1))  # 保存图片
    pdf.close()
```

### 软件界面
![](https://github.com/jtyoui/logo/blob/master/img_pdf.png?raw=true)

## 编程语言
[点击查看Python3版本](https://gitee.com/tyoui/imgPDF)

[点击查看Java8版本](https://gitee.com/tyoui/jpdf)

[1]: https://blog.jtyoui.com