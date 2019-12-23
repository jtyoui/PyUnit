#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 15:29
# @Email  : jtyoui@qq.com
# @Software: PyCharm
from jtyoui.data.methods import random_lower_char, random_upper_char, random_digits, random_special
from jtyoui.file_zip import sep
import random


class Captcha:
    """验证码生成器

    >>> c = Captcha(300, 60)  # 验证码大小是300*60
    >>> c.format(lower=1, upper=2, digits=4, special=1)  # 有小写字母1个、大写字母2、数字4个、特殊符号1个
    >>> c.make_photo(f'D://')  # 生成的验证码存放在D盘下

    """

    def __init__(self, width=240, height=60):
        self.width = width
        self.height = height
        self.flag = []
        self.number = 4

    @staticmethod
    def color1():
        return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

    @staticmethod
    def color2():
        return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

    def format(self, lower=4, upper=0, digits=0, special=0):
        """验证码格式

        :param lower: 小写字母
        :param upper: 大写字母
        :param digits: 数字
        :param special: 特殊符号
        """
        self.flag.clear()
        self.number = lower + upper + digits + special
        self.flag.extend(random_lower_char(lower))
        self.flag.extend(random_upper_char(upper))
        self.flag.extend(random_digits(digits))
        self.flag.extend(random_special(special))
        random.shuffle(self.flag)

    def make_photo(self, dir_):
        """生成验证码

        :param dir_: 存放验证码照片的文件夹
        """
        from PIL import Image  # 安装pillow： pip install pillow
        from PIL import ImageFont
        from PIL import ImageDraw
        from PIL import ImageFilter
        image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        font = ImageFont.truetype('arial.ttf', 36)

        draw = ImageDraw.Draw(image)
        for w in range(self.width):
            for h in range(self.height):
                draw.point((w, h), fill=self.color1())
        for index, t in enumerate(self.flag):
            draw.text(((self.width - 10) // self.number * index + 10, 10), t, font=font, fill=self.color2())
        image = image.filter(ImageFilter.BLUR)
        image.save(dir_ + sep + ''.join(self.flag) + '.jpg', 'jpeg')
        return image


if __name__ == '__main__':
    c = Captcha(300, 60)  # 验证码大小是300*60
    for _ in range(10):  # 生成10张验证码
        c.format(lower=1, upper=2, digits=4, special=1)  # 有小写字母1个、大写字母2、数字4个、特殊符号1个
        c.make_photo(r'D://')  # 生成的验证码存放在D盘下
