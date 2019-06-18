#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/17 17:32
# @Author: Jtyoui@qq.com
from tkinter.filedialog import *


class UI(Frame):

    def __init__(self):
        root = Tk()
        root.geometry('800x800+900+50')
        root.title('GUI')
        super().__init__(master=root)
        self.master = root
        self.pack()
        self.create_widget()
        self.master.mainloop()

    def create_widget(self):
        menubar = Menu(self)
        menu_file = Menu(menubar)
        two = Menu(menu_file)
        menubar.add_cascade(label='程序测试', menu=menu_file)
        menu_file.add_cascade(label='第二级1', menu=two)
        menu_file.add_cascade(label='第二级2', menu=two)
        two.add_command(label='第三级', command=self.test)
        self.master['menu'] = menubar

    def test(self):
        top = Toplevel()
        text = Text(top)
        text.pack()


UI()
