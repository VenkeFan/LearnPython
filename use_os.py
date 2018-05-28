#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def pringOSInfo():
	print(os.uname())

def getAbsPath():
	print(os.path.abspath('.'))

def getAllDirs():
	dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
	for d in dirs:
		print(d)

def getTxtFiles():
	files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt']
	for f in files:
		print(f)


if __name__ == '__main__':
	getAllDirs()