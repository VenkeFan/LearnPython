#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import schedule
import time


def job(text = ""):
	print(text, 'I`m working...', time.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__': 
	schedule.every().seconds.do(job, '每秒一次')
	# schedule.every(5).seconds.do(job, '5秒一次')
	# schedule.every(10).minutes.do(job, '10分钟一次')
	# schedule.every().hour.do(job, '1小时一次')
	# # 每天10:30执行
	# schedule.every().day.at('10:30').do(job)
	# # 每隔5到10天执行一次
	# schedule.every(5).to(10).days.do(job)
	# # 每周一的这个时候执行一次
	# schedule.every().monday.do(job)
	# # 每周三13:15执行一次
	# schedule.every().wednesday.at('13:15').do(job)

	while True:
		# run_pending: 运行所有可以运行的任务
		schedule.run_pending()
		time.sleep(1)