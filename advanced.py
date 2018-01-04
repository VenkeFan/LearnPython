#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### 切片 #########################

# 去除字符串首尾的空格
def trim(str):
	if str[:1] == ' ':
		return trim(str = str[1:])
	elif str[-1:] == ' ':
		return trim(str = str[:-1])
	else:
		return str

# 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('切片练习测试成功!')


######################### 迭代 #########################

# 使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(l):
	if len(l) < 1:
		return None, None

	min = l[0]
	max = l[0]

	for item in l:
		if item < min:
			min = item
		if item > max:
			max = item

	return (min, max)

# 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('迭代练习测试成功!')


######################### 列表生成式 #########################

#使用内建的isinstance函数判断一个变量是不是字符串，保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('列表生成式练习测试通过!')
# else:
#     print('测试失败!')


######################### 生成器 #########################

# 斐波拉契数列
# def fib(max):
# 	n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'


# 杨辉三角
def triangles(max):
	i = 1
	results = []

	while i <= max:
		curList = []
		if i == 1:
			curList = [1]
		else:
			preList = results[i - 2]
			curList = [preList[0]]
			for j, value in enumerate(preList):
				if j == len(preList) - 1:
					curList.append(value)
				else:
					curList.append(preList[j] + preList[j + 1])
		
		results.append(curList)

		print(curList)

		i += 1

	return results


def trianglesGenerator():
	i = 1
	curList = []

	while True:
		if i == 1:
			curList = [1]
		else:
			preList = curList
			curList = [preList[0]]
			for j, value in enumerate(preList):
				if j == len(preList) - 1:
					curList.append(value)
				else:
					curList.append(preList[j] + preList[j + 1])
		
		yield curList

		i += 1

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

# 测试:
# n = 0
# results = []
# for t in trianglesGenerator():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('杨辉三角生成器测试通过!')
# else:
#     print('测试失败!')


######################### 迭代器 #########################
