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


### 执行程序:两个都可以

```python
from jtyoui.imagepdf import ui #TK

if __name__ == '__main__':
    ui()
```

### 核心代码
```Python
import fitz
import os

def get_dir_name(file_dir):
    base_name = os.path.basename(file_dir)  # 获得地址的文件名
    dir_name = os.path.dirname(file_dir)  # 获得地址的父链接
    return dir_name, base_name
    
def image_pdf(file_dir):
    dir_name, base_name = get_dir_name(file_dir)
    doc = fitz.Document()
    for img in os.listdir(file_dir):  # 排序获得对象
        img=file_dir+os.sep+img
        img_doc = fitz.Document(img)  # 获得图片对象
        pdf_bytes = img_doc.convertToPDF()  # 获得图片流对象
        img_pdf = fitz.Document("pdf", pdf_bytes)  # 将图片流创建单个的PDF文件
        doc.insertPDF(img_pdf)  # 将单个文件插入到文档
        img_doc.close()
        img_pdf.close()
    doc.save(dir_name + os.sep + base_name + ".pdf")  # 保存文档
    doc.close()
    
def pdf_image(pdf_name):
    dir_name, base_name = get_dir_name(pdf_name)
    pdf = fitz.Document(pdf_name)
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]  # 获得每一页的对象
        trans = fitz.Matrix(1.0, 1.0).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        pm.writePNG(dir_name + os.sep + base_name[:-4] + '_' + '{:0>3d}.png'.format(pg + 1))  # 保存图片
    pdf.close()
```

### 将doc文件中的照片提取出来
```python
from jtyoui.imagepdf import doc_to_photo
import os
if __name__ == '__main__':
    path = r'C:\Users\Desktop'
    doc_to_photo(path + os.sep + '政法-诉讼-民事诉讼.doc', path)
```

### 软件界面
![](https://gitee.com/tyoui/logo/raw/master/img_pdf.png)

## 编程语言
[点击查看Python3版本](https://gitee.com/tyoui/imgPDF)

[点击查看Java8版本](https://gitee.com/tyoui/jpdf)

[1]: https://blog.jtyoui.com