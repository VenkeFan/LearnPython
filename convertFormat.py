#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#导入模块
import os,sys
from PIL import Image

#定义函数名称              
def convertImage():             
	for foldName, subfolders, filenames in os.walk(path):     #用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
		for filename in filenames:     #遍历列表下的子文件夹名
			if  filename!= sys.argv[0]:  #代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
				if filename.endswith('.png'):   #当文件名以.png后缀结尾时
					print (os.path.join(foldName,filename))  #输出提示
					im = Image.open(os.path.join(foldName,filename))
					# im.save('/Users/fanqi/downloads/imgtest/test.jpg')
					image = im.convert('RGB')
					image.save('/Users/fanqi/downloads/imgtest/test.jpg')

if __name__ == '__main__': 
	path = r'/Users/fanqi/downloads/imgtest'	#运行程序前，记得修改主文件夹路径！
	convertImage()