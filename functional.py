#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### map / reduce #########################

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
	return name.capitalize();

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce

def prod(l):
	def quadrature(x, y):
		return x * y

	return reduce(quadrature, l)

# 测试:
result = prod([3, 5, 7, 9])
print('3 * 5 * 7 * 9 =', result)


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def strToFloat(str):
	l = str.split('.')
	if len(l) != 2:
		return None

	intStr = l[0]
	decimalStr = l[1]

	def toInteger(s):
		return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s))

	return toInteger(intStr) + toInteger(decimalStr) / (10 ** len(decimalStr))

# 测试:
f = strToFloat('123.456')
print('strToFloat(\'123.456\') =', f)

######################### filter #########################

# 用filter求素数（埃氏筛法）
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 可以直接在下面的filter()里使用lambda表达式
# def _not_divisible(n):
#     return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n

        it = filter(lambda x: x % n > 0, it) # 构造新序列

for n in primes():
    if n < 100:
        print(n)
    else:
        break


# 筛选回数，回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
def is_palindrome(n):
	if n < 0 or (n != 0 and n % 10 == 0):
		return False

	r = 0
	tmp = n

	while tmp > 0:
		r = r * 10 + tmp % 10
		tmp = tmp // 10
	
	return r == n

# 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('回数测试成功!')
# else:
#     print('测试失败!')

######################### sorted #########################

def by_name(t):
	return t[0].lower

def by_score(t):
	return t[-1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key = by_score, reverse = True)
print(L2)

######################### 返回函数 / 闭包 #########################

def createCounter():
	dic = {'count': 0}

	def counter():
		dic['count'] += 1
		return dic['count']

	return counter

## 别人的几种方法：
# begin

# 第一种创造一个生成器
def createCounterA():
    def f():
        n = 0
        while True:
            n = n + 1
            yield n     #先创造一个生成器
    sun = f()
    def counter():
        return next(sun)   #用一个函数来调用生成器
    return counter

# 第二种：使用列表（列表list是全局变量）
def createCounterB():
    fs = [0]          #创建一个只有一个元素的列表
    def counter():
        fs[0] = fs[0] + 1
        return fs[0]
    return counter

# 第三种：使用nonlocal关键字，将局部变量变成全局变量
def createCounterC():
    n = 0
    def f():
        nonlocal n
        n = n + 1
        return n
    return f

 # end

# 测试:
counterA = createCounter()
print('counterA: ', counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('闭包测试通过!')
else:
    print('测试失败!')

######################### 匿名函数 #########################

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
L2 = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print('普通函数：', L, '\n匿名函数：', L2)

######################### 装饰器(Decorator) #########################

import functools

# 不带参数的 Decorator
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2018-01-01')

now()
print('func name ------>', now.__name__)

# 带参数的 Decorator
def log2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' %(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log2('execute')
def now2():
	print('2018-01-02')

now2()
print('func name ------>', now2.__name__)

######################### 偏函数 #########################

import functools

int2 = functools.partial(int, base = 2)

print(int2('100'))
