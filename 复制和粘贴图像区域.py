#coding=utf-8
from PIL import Image

'''
    crop()  可以从一幅图像中裁剪指定区域(四元组的坐标依次是（左，上，右，下）。PIL 中指定坐标系的左上角坐标为（0，0）)
    transpose() 旋转获取的区域(transpose有这么几种模式FLIP_LEFT_RIGHT ，FLIP_TOP_BOTTOM ，ROTATE_90 ，ROTATE_180 ，ROTATE_270，TRANSPOSE ，TRANSVERSE)
    paste() 将区域放回去(paste函数的参数为(需要修改的图片，粘贴的起始点的横坐标，粘贴的起始点的纵坐标)
'''


img = Image.open("./img/test.jpg")

box = (100, 100, 250, 250)

region = img.crop(box)

region = region.transpose(Image.ROTATE_180)

region.show()

img.paste(region, box)

img.show()

