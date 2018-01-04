#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x


def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny


def quadratic(a, b, c):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(b, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(c, (int, float)):
		raise TypeError('bad operand type')

	if a == 0:
		return None
	
	x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a);
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a);

	return x1, x2


# 默认参数
def power(x, n = 2):
	result = 1;
	for i in range(n):
		result = result * x
	return result


def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name = %s, gender = %s, age = %d, city = %s' %(name, gender, age, city))


def add_end(l = []):
	l.append('end')
	return l

def add_end2(l = None):
	if l is None:
		l = []
	l.append('end')
	return l


# 可变参数
def calc(*numbers):
	sum = 0
	for i in numbers:
		sum += i * i
	return sum


# 关键字参数
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数
def person_2(name, age, *, city, gender):
	print('name:', name, 'age:', age, 'city:', city, 'gender:', gender)


# 递归函数
def factorial(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return n * factorial(n - 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def hanoi(n, src, tmp, dst):#将n个盘子从src搬到dst
    if n == 1: #只有一个盘子的情况
        print(src, '->', dst)
    else: #有一个以上盘子的情况
        hanoi(n-1, src, dst, tmp) #将上方的n-1个盘子从src搬到tmp
        print(src, '->', dst) #将第n个盘子从src轻松愉快地移动到dst
        hanoi(n-1, tmp, src, dst) #擦屁股，将tmp上的n-1个盘子搬到dst上

