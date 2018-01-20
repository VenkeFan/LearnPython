#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### 缩放图像 #########################

# from PIL import Image

# # 当前路径打开一个jpg图像文件
# img = Image.open('snapshot.jpg')
# # 获得图像尺寸
# w, h = img.size
# print('Original image size: %sx%s' % (w, h))

# # 缩放到50%:
# img.thumbnail((w // 2, h // 2))
# print('Resize image to: %sx%s' % (w//2, h//2))

# # 把缩放后的图像用jpeg格式保存
# img.save('thumbnail.jpeg')

######################### 模糊效果 #########################

# from PIL import Image, ImageFilter

# img = Image.open('snapshot.jpg')
# img2 = img.filter(ImageFilter.BLUR)
# img2.save('blur.jpg')

######################### 绘制验证码 #########################

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
	return chr(random.randint(65, 90))

# 随机颜色1
def rndColor1():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
img = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
font = ImageFont.truetype('arial.ttf', 36)

# 创建Draw对象
draw = ImageDraw.Draw(img)

# 填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill = rndColor1());

# 输出文字
for t in range(4):
	draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())

# 模糊
img = img.filter(ImageFilter.BLUR);
img.save('code.jpg')