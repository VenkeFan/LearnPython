#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import datetime


# 每天凌晨3点执行func方法。

def func():
	print("hello world")
	# 如果需要循环调用，就要添加以下方法
	timer = threading.Timer(86400, func)
	timer.start()


if __name__ == '__main__': 
	# 获取现在时间
	now_time = datetime.datetime.now()
	# 获取明天时间
	next_time = now_time + datetime.timedelta(days=+1)
	next_year = next_time.date().year
	next_month = next_time.date().month
	next_day = next_time.date().day
	# print('%s-%s-%s %s' % (next_year, next_month, next_day, next_time))
	# 获取明天3点时间
	next_time = datetime.datetime.strptime(str(next_year) + '-' + str(next_month) + '-' + str(next_day) + ' ' + '03:00:00', '%Y-%m-%d %H:%M:%S')
	# print(next_time)

	# 获取距离明天3点时间，单位为秒
	timer_start_time = (next_time - now_time).total_seconds()
	# print(timer_start_time)

	# 定时器，参数为（多少时间后执行，单位为秒，执行的方法）
	timer = threading.Timer(timer_start_time, func)
	timer.start()