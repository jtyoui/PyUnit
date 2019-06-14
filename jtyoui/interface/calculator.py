#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/6/14 16:37
# @Author: Jtyoui@qq.com
import tkinter


class Calculator(tkinter.Frame):
    def __init__(self):
        self.master = tkinter.Tk()
        self.master.title('计算器')
        self.master.resizable(width=False, height=False)  # 防止大小调整
        self.master.geometry('200x240+200+300')
        super().__init__(master=self.master)
        self.pack()
        self._create_widget()
        self.master.mainloop()

    def _create_widget(self):
        """通过grid实现计算器界面"""
        btn = (['MC', 'M+', 'M-', 'MR'],
               ['C', '±', '/', 'X'],
               [7, 8, 9, '-'],
               [4, 5, 6, '+'],
               [1, 2, 3, '='],
               [0, '.'])
        tkinter.Entry(self).grid(row=0, column=0, columnspan=4, pady=10)
        for row_index, row in enumerate(btn, 1):
            for c_index, c in enumerate(row):
                self.b = tkinter.Button(self, text=c, width=3, height=1, command=self.logic)
                if c == '=':
                    self.b.grid(row=row_index, column=c_index, rowspan=2, sticky=tkinter.NSEW)
                elif c == 0:
                    self.b.grid(row=row_index, column=c_index, columnspan=2, sticky=tkinter.NSEW)
                elif c == '.':
                    self.b.grid(row=row_index, column=c_index + 1, sticky=tkinter.NSEW)
                else:
                    self.b.grid(row=row_index, column=c_index, sticky=tkinter.NSEW)

    def logic(self):
        print(self.b)


if __name__ == '__main__':
    Calculator()
