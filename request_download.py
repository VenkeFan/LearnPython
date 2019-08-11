#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import re

def download_file(urlStr, fileFolder):
	folderExist = os.path.exists(fileFolder);
	if not folderExist:
		os.makedirs(fileFolder);

	# 读取远程资源
	res = requests.get(urlStr);
	res.raise_for_status();

	# 获取文件名
	fileName = os.path.basename(urlStr);
	filePath = os.path.join(fileFolder, fileName);
	print('writting resource:', filePath);

	# 保存到本地
	imageFile = open(filePath, 'wb');
	for chunk in res.iter_content(100000):
		imageFile.write(chunk);
	imageFile.close();
	print('writting finished');


# 程序主入口
if __name__ == '__main__':
	url = 'http://file.beiwaionline.com/CourseContent/gaizao/dxyw/content/kcjj/ch1/word1.mp4';
	folder = 'Language/';
	download_file(url, folder);

