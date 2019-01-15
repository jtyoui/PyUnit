#### 验证码识别。Python版本
#### 使用说明
    # 使用的时候注意填写密码。
    if __name__ == '__main__':
        # 第一个参数是要识别图像的照片。第二参数是图片类型（看code_type.txt文件）
        # cr = codeRecognition.cr.decode(filename='getimage.jpg', code_type=1004)
        cr = codeRecognition.cr.decode('code.png', 3006)
        print(cr)
