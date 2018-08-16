# # -*- coding:utf-8 -*-
#
from PIL import Image
from pylab import *
import os
#
# def cut(id,vx,vy):
#     #打开图片图片1.jpg
#     name1 = "/home/xuna/桌面/3/图片" + id + ".jpg"
#     name2 = "/home/xuna/桌面/3/图片" + id + "_切块_"
#     im = Image.open(name1)
#
#     #偏移量
#     dx = 40
#     dy = 40
#     n = 1
#
#     #左上角切割
#     x1 = 0
#     y1 = 0
#     x2 = vx
#     y2 = vy
#
#     #纵向
#     while x2 <= 320:
#         #横向切
#         while y2 <= 480:
#             name3 = name2 + str(n) + ".jpg"
#             #print n,x1,y1,x2,y2
#             im2 = im.crop((y1, x1, y2, x2))
#             im2.save(name3)
#             y1 = y1 + dy
#             y2 = y1 + vy
#             n = n + 1
#         x1 = x1 + dx
#         x2 = x1 + vx
#         y1 = 0
#         y2 = vy
#
#     print("图片切割成功，切割得到的子图片数为")
#     return n-1
#
#
# if __name__=="__main__":
#
#     #取图片id的后两位
#     id = "1"
#
#     #切割图片的面积 vx,vy
#     #大
#     res = cut(id,160,160)
#
#     #中
#     #res = cut(id,120,120)
#
#     #小
#     #res = cut(id,80,80)
#
#     print(res)
image = Image.open('mifeng.png')
box = (250,100,550,400)
image2 = image.crop(box)
im = array(image2)
image2.save(os.path.join('home','yqw','mifeng.png'))
# imshow(array(image))
imshow(im)
show()
