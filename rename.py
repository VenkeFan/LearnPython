#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#导入模块
import os,sys

#定义函数名称              
def add_prefix_files():             
	mark = 'yf_'                 
	old_mark = 'ly_'
	for foldName, subfolders, filenames in os.walk(path):     #用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
		for filename in filenames:     #遍历列表下的子文件夹名
			if  filename!= sys.argv[0]:  #代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
				if filename.startswith(old_mark):   #当文件名以old_mark前缀开头时
					nfilename = filename[3:]	#这里下标是old_mark的长度
					# print (nfilename)
					os.rename(os.path.join(foldName,filename),os.path.join(foldName,mark+nfilename))  #重命名文件
					print (filename,"has been renamed successfully! New name is: ",mark+nfilename)  #输出提示

if __name__ == '__main__': 
	path = r'/Users/fanqi/desktop/work/leyuan/code/LeYuan/leyuan/LeYuan/Assets.xcassets'	#运行程序前，记得修改主文件夹路径！
	add_prefix_files()         #调用定义的函数，注意名称与定义的函数名一致
