# **imgPDF** [![tyoui](https://github.com/zhangwei0530/logo/blob/master/logo/photolog.png?raw=true)](http://www.jtyoui.com)

[![](https://github.com/zhangwei0530/logo/blob/master/logo/logo.png?raw=true)](http://www.jtyoui.com)

## PDF和照片相互装换程序
[![](https://img.shields.io/badge/个人网站-jtyoui-yellow.com.svg)](https://www.jtyoui.com/)
[![](https://img.shields.io/badge/Python-3.6-green.svg)]()
[![](https://img.shields.io/badge/BlogWeb-Tyoui-bule.svg)](http://www.tyoui.cn)
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
    import fitz,glob
    
    def image_pdf(self):
    """
        将照片装换为PDF
    """
        doc = fitz.open()
        for img in sorted(glob.glob("照片文件夹的地址")):
            img_doc = fitz.open(img)
            pdf_bytes = img_doc.convertToPDF()
            img_pdf = fitz.open("pdf", pdf_bytes)
            doc.insertPDF(img_pdf)
            img_doc.close()
            img_pdf.close()
        doc.save("保存PDF文件的地址")
        doc.close()
        
        
        def pdf_image(self):
        """
            将PDF转化为图片
        """
            pdf = fitz.open("PDF的文件地址")
            for pg in range(0, pdf.pageCount):
                page = pdf[pg]
                trans = fitz.Matrix(1.0, 1.0).preRotate(0)
                pm = page.getPixmap(matrix=trans, alpha=False)
                pm.writePNG("保存照片地址")
            pdf.close()
```

### 软件界面
![](https://github.com/jtyoui/logo/blob/master/img_pdf.png?raw=true)

## 编程语言
[点击查看Python3版本](https://gitee.com/tyoui/imgPDF)

[点击查看Java8版本](https://gitee.com/tyoui/jpdf)