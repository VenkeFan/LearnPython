#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time


exec_count = 0

def start():
	print("hello world")

def heart_beat():
	print(time.strftime("%Y-%m-%d %H:%M:%S"))
	global exec_count
	exec_count += 1
	# 执行15次后停止定时器
	if exec_count <= 15:
		start()
		threading.Timer(3, heart_beat).start()


if __name__ == '__main__': 
	heart_beat()