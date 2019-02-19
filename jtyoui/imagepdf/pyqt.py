# -*- coding: UTF-8 -*-
import fitz, glob, os, sys
import requests
from PyQt5 import (QtCore, QtGui, QtWidgets)


class ImagePDF:
    """
    需要安装第三方包：PyMuPDF、requests和PyQt5
    pip install PyMuPDF
    pip install PyQt5
    pip install requests
    """

    def __init__(self):
        super().__init__()
        self.translate = QtCore.QCoreApplication.translate
        self.main_window = QtWidgets.QMainWindow()  # 加载主窗口
        self.main_window.resize(440, 311)  # 设置窗口大小
        self.main_window.setWindowTitle(self.translate("MainWindow", "PDF和图片互转"))  # 设置窗口名字
        self.main_window.setFixedSize(self.main_window.width(), self.main_window.height())  # 禁止窗口大小被改变
        self.pale = QtGui.QPalette()
        self.req = requests.get('https://gitee.com/tyoui/logo/raw/master/pdf.png')  # 获取背景图片的网络连接
        self.photo = QtGui.QPixmap()
        self.photo.loadFromData(self.req.content)
        self.pale.setBrush(self.main_window.backgroundRole(), QtGui.QBrush(self.photo))  # 加载背景图像
        self.main_window.setPalette(self.pale)  # 设置窗口背景图
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.central_widget.setObjectName("centralwidget")
        self.font = QtGui.QFont()  # 字体
        self.font.setFamily("Arial")  # 字体类型
        self.font.setPointSize(14)  # 字体大小
        self.label = QtWidgets.QLabel(self.central_widget)  # 初始化label标签
        self.img_pdf = QtWidgets.QPushButton(self.central_widget)  # 初始化按钮
        self.pdf_img = QtWidgets.QPushButton(self.central_widget)
        self.open_dir = QtWidgets.QPushButton(self.central_widget)
        self.save_file = QtWidgets.QPushButton(self.central_widget)
        self.file_dir = None
        self.pdf_name = None
        self.setup_ui()  # 打开界面

    def setup_ui(self):
        self.main_window.setCentralWidget(self.central_widget)
        self.main_window.setStatusBar(self.statusbar)
        self.set_attr(self.label, (15, 160, 420, 31), "label", "欢迎使用图片转PDF,PDF转图片软件,作者:Jtyoui")
        self.set_attr(self.open_dir, (50, 90, 161, 31), "open_dir", "打开图片文件夹")
        self.set_attr(self.img_pdf, (250, 90, 161, 31), "img_pdf", "将图片转PDF")

        self.set_attr(self.save_file, (50, 230, 161, 31), "save_file", "打开PDF文件")
        self.set_attr(self.pdf_img, (250, 230, 161, 31), "pdf_img", "将PDF转图片")

        QtCore.QMetaObject.connectSlotsByName(self.main_window)
        self.click()  # 监听事件

    def set_attr(self, this, position, file_name, title):
        """
        设置标签属性
        :param this: 标签对象
        :param position: 标签的位置
        :param file_name: 标签的名字
        :param title: 标签的标题
        :return: None
        """
        this.setGeometry(QtCore.QRect(*position))
        this.setFont(self.font)
        this.setObjectName(file_name)
        this.setText(self.translate("MainWindow", title))

    def click(self):
        """
        监听四个按钮事件
        :return: None
        """
        self.open_dir.clicked.connect(self.get_dir)
        self.save_file.clicked.connect(self.get_file)
        self.img_pdf.clicked.connect(self.image_pdf)
        self.pdf_img.clicked.connect(self.pdf_image)

    def get_dir(self):
        # 获得文件夹的绝对路径
        self.file_dir = QtWidgets.QFileDialog.getExistingDirectory(self.central_widget, '选择文件夹', './')

    def get_file(self):
        # 获得PDF文件的绝对路径
        self.pdf_name = QtWidgets.QFileDialog.getOpenFileName(self.central_widget, '选择PDF文件', '/', '(*.pdf)')

    def image_pdf(self):
        if not self.file_dir:  # 判断图片文件夹是否被选择
            self.open_success('请先选择图片文件夹的位置！')
            return
        img = self.file_dir + "/*"  # 获得文件夹下的所有对象
        dir_name, base_name = get_dir_name(self.file_dir)
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
        self.open_success('转化成功！！')
        self.file_dir = None  # 初始化图片文件夹地址

    def pdf_image(self):
        if self.pdf_name is None:  # 是否打开过文件
            self.open_success('请先选择PDF文件的位置！')
            return
        elif not self.pdf_name[0]:  # 是否确认过文件
            self.open_success('请先选择PDF文件的位置！')
            self.pdf_name = None
            return
        dir_name, base_name = get_dir_name(self.pdf_name[0])
        pdf = fitz.open(self.pdf_name[0])
        for pg in range(0, pdf.pageCount):
            page = pdf[pg]  # 获得每一页的对象
            trans = fitz.Matrix(1.0, 1.0).preRotate(0)
            pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
            pm.writePNG(dir_name + os.sep + base_name[:-4] + '_' + '{:0>3d}.png'.format(pg + 1))  # 保存图片
        pdf.close()
        self.open_success('转化成功！！')
        self.pdf_name = None  # 初始化地址

    def open_success(self, message):
        # 成功之后弹出小框
        QtWidgets.QMessageBox.information(self.central_widget, '信息', message)


def pdf_image():
    app = QtWidgets.QApplication(sys.argv)
    ui = ImagePDF()
    ui.main_window.show()
    sys.exit(app.exec_())


def get_dir_name(file_dir):
    base_name = os.path.basename(file_dir)  # 获得地址的文件名
    dir_name = os.path.dirname(file_dir)  # 获得地址的父链接
    return dir_name, base_name


if __name__ == '__main__':
    pdf_image()
