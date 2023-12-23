#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time


cancel_timer = False

def start():
	print("hello world")

def heart_beat():
	print(time.strftime("%Y-%m-%d %H:%M:%S"))
	if not cancel_timer:
		start()
		threading.Timer(3, heart_beat).start()


if __name__ == '__main__': 
	heart_beat()
	# 15秒后停止定时器
	time.sleep(15)
	cancel_timer = True