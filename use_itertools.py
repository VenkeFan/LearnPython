#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### “无限”迭代器 #########################

import itertools

#### count()
# natuals = itertools.count(1)
# for n in natuals:
# 	if n > 20:
# 		break
# 	print(n)

#### cycle()
# cs = itertools.cycle('ABC')
# i = 0
# for c in cs:
# 	if i >= 10:
# 		break
# 	i += 1
# 	print(c)

#### repeat()
# ns = itertools.repeat('A', 3)
# for n in ns:
# 	print(n)

##### takewhile()
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x < 10, natuals)
# print(list(ns))

######################### chain() #########################

# for c in itertools.chain('ABC', 'XYZ', '123'):
# 	print(c)

######################### groupby() #########################

# for key, group in itertools.groupby('AAABBBCCaAA'):
# 	print(key, list(group))

# print('不区分大小写：')
# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
# 	print(key, list(group))


# 练习
# 计算圆周率可以根据公式
# def pi(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

#     # step 4: 求和:
#     return 3.14

def pi(n):
	natuals = itertools.count(1, 2)
	ns = itertools.takewhile(lambda x: x <= n * 2 - 1, natuals)
	
	result = 0
	divisor = 4
	for n in list(ns):
		result = result + divisor / n 
		divisor = -divisor

	return result

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')




