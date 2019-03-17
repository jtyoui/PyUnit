#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/9 0009
# @Email : jtyoui@qq.com
# @Software : PyCharm

import fitz  # 安装 pip install PyMuPDF
from PIL import Image, ImageTk  # 安装 pip install pillow
from tkinter import filedialog, messagebox
import os
import io
import urllib.request
import tkinter

DIRS, FILE = '', ''  # 文件夹地址,pdf文件地址


def select_pdf():
    global FILE
    FILE = filedialog.askopenfilename(filetypes=(("PDF file", "*.pdf"),))  # 获得pdf文件地址


def select_dir():
    global DIRS
    DIRS = filedialog.askdirectory()  # 获得文件夹地址


def start():
    global DIRS, FILE
    if DIRS:
        image_pdf(DIRS)  # 执行图片转pdf
        DIRS = ''
    elif FILE:
        if not os.path.exists(FILE[:-4]):
            os.mkdir(FILE[:-4])
        pdf_image(FILE)  # 执行pdf转照片
        FILE = ''
    else:
        messagebox.showwarning('警告', '先选择在执行!')


def get_dir_name(file_dir):
    base_name = os.path.basename(file_dir)  # 获得地址的文件名
    dir_name = os.path.dirname(file_dir)  # 获得地址的父链接
    return dir_name, base_name


def image_pdf(file_dir):
    dir_name, base_name = get_dir_name(file_dir)
    doc = fitz.Document()
    for img in os.listdir(file_dir):  # 排序获得对象
        img = file_dir + os.sep + img
        img_doc = fitz.Document(img)  # 获得图片对象
        pdf_bytes = img_doc.convertToPDF()  # 获得图片流对象
        img_pdf = fitz.Document("pdf", pdf_bytes)  # 将图片流创建单个的PDF文件
        doc.insertPDF(img_pdf)  # 将单个文件插入到文档
        img_doc.close()
        img_pdf.close()
    doc.save(dir_name + os.sep + base_name + ".pdf")  # 保存文档
    doc.close()
    messagebox.showinfo('提示', '转换成功!')


def pdf_image(pdf_name):
    dir_name, base_name = get_dir_name(pdf_name)
    pdf = fitz.Document(pdf_name)
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]  # 获得每一页的对象
        trans = fitz.Matrix(1.0, 1.0).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        pm.writePNG(FILE[:-4] + os.sep + base_name[:-4] + '_{:0>4d}.png'.format(pg + 1))  # 保存图片
    pdf.close()
    messagebox.showinfo('提示', '转换成功!')


def ui():
    root = tkinter.Tk()
    root.title('PDF和照片互转器')  # 标题
    root.resizable(width=False, height=False)  # 防止大小调整
    canvas = tkinter.Canvas(root, width=450, height=320, highlightthickness=0)  # 创建画布

    photo = urllib.request.urlopen('https://gitee.com/tyoui/logo/raw/master/pdf.png')  # 获取背景图片的网络连接
    data_stream = io.BytesIO(photo.read())  # 转化为字节流对象
    pil_image = Image.open(fp=data_stream)  # 生成图片
    image = ImageTk.PhotoImage(pil_image)  # 生成tk图片对象
    canvas.create_image(225, 160, image=image)

    select_dir_button = tkinter.Button(root, text="选择照片文件夹", command=select_dir, bg='yellow')  # 创建按钮
    select_pdf_button = tkinter.Button(root, text="选择PDF文件", command=select_pdf, bg='green')
    click_button = tkinter.Button(root, text="点击执行", command=start, bg='blue')

    select_dir_button.pack()  # 启动按钮
    select_pdf_button.pack()
    click_button.pack()

    canvas.create_window(240, 120, width=100, height=30, window=select_dir_button)  # 将按钮创建到画布
    canvas.create_window(240, 190, width=100, height=30, window=select_pdf_button)
    canvas.create_window(240, 260, width=100, height=30, window=click_button)
    canvas.pack()  # 启动画布
    root.mainloop()  # 主程序循环


if __name__ == '__main__':
    ui()
