#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import schedule
import time
import threading
import datetime

# 时间有冲突的执行多个任务

def job1():
	print('I`m working...in job1 start', time.strftime("%Y-%m-%d %H:%M:%S"))
	time.sleep(5)
	print('I`m working...in job1 end', time.strftime("%Y-%m-%d %H:%M:%S"))

def job2():
	print('I`m working...in job2 start', time.strftime("%Y-%m-%d %H:%M:%S"))
	time.sleep(3)
	print('I`m working...in job2 end', time.strftime("%Y-%m-%d %H:%M:%S"))

def job1_task():
	threading.Thread(target=job1).start()

def job2_task():
	threading.Thread(target=job2).start()

def run():
	schedule.every(3).seconds.do(job1_task)
	schedule.every(3).seconds.do(job2_task)

	while True:
		schedule.run_pending()
		time.sleep(1)

if __name__ == '__main__': 
	run()