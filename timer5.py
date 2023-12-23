#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import schedule
import time

# 时间有冲突的执行多个任务

def job1():
	print('I`m working...in job1 start', time.strftime("%Y-%m-%d %H:%M:%S"))
	time.sleep(5)
	print('I`m working...in job1 end', time.strftime("%Y-%m-%d %H:%M:%S"))

def job2():
	print('I`m working...in job2', time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__': 
	schedule.every(3).seconds.do(job1)
	schedule.every(3).seconds.do(job2)

	while True:
		schedule.run_pending()
		time.sleep(1)

# 根据代码运行结果可以看出，schedule方法是串行的，代码中有时间冲突，所以执行完第一个任务，才会执行第二个任务，即任务二每隔3秒执行一次，而任务一执行时间是5秒。
# 如果不用多线程,则定时任务会不准确,因为任务会按照顺序执行,如果上一个任务比较耗时,则下一个任务就会"延误"