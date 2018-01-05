#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### try...except...finally... #########################

# try:
# 	print('try..')
# 	r = 10 / 2
# 	print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
# 	print('ZeroDivisionError:', e)
# else:
# 	print("no error")
# finally:
# 	print('finally...')
# print('END')

######################### 调用栈 #########################

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')

# main()
# print('END')

######################### 记录错误 #########################

# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
# 	try:
# 		bar('0')
# 	except Exception as e:
# 		logging.exception(e)

# main()
# print('END')

######################### 抛出错误 #########################

# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n

# foo('0')

### reraise ###

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise

# bar()

# 练习

# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
from functools import reduce
import loggint

def str2num(s):
	# return int(s)
	num = 0.0
	try:
		if '.' in s:
			num = float(s)
		else:
			num = int(s)
	except ValueError as e:
		logging.exception(e)
		raise e

	return num
	

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()