#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/19 0019
# @Email : jtyoui@qq.com
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_qq_mail(from_addr, password, to_addr, content, subject='', files=None, host=('smtp.qq.com', 465)):
    """这个一个邮箱发送函数.默认是qq邮箱

    :param from_addr: 发送方邮箱
    :param password: 填入发送方邮箱的授权码
    :param to_addr: 收件人为多个收件人,通过;为间隔的字符串,比如: xx@qq.com;yy@qq.com
    :param content: 正文
    :param subject: 主题
    :param files: 附加
    :param host: 邮件传输协议
    :return: bool类型.打印成功和失败
    """
    text = MIMEText(content, _charset='utf-8')
    m = MIMEMultipart()
    if files:
        import os
        from email import encoders
        file_name = os.path.basename(files)  # 获得文件名字
        file = MIMEApplication(open(files, 'rb').read())
        file.add_header('Content-Disposition', 'attachment', filename=('GBK', '', file_name))
        encoders.encode_base64(file)  # 解决文件名乱码问题
        m.attach(file)
    m['Subject'] = subject
    m['From'] = from_addr
    m['To'] = to_addr
    m.attach(text)
    server = None
    try:
        server = smtplib.SMTP_SSL(*host)  # 安全模式
        server.login(from_addr, password)  # 登陆
        server.sendmail(from_addr, to_addr, m.as_string())  # 发送
        return True
    except smtplib.SMTPException as e:
        print(e)
        return False
    finally:
        if not server:
            server.quit()


# jfciwswgxlmedjei9

if __name__ == '__main__':
    flag = send_qq_mail('ptyoui@jtyoui.com', '授权码', 'jtyoui@jtyoui.com', '测试邮箱', '政治文件', files='政治.txt')
    if flag:
        print('发送成功!')
    else:
        print('发送失败!')
