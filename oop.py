#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


class Timer(object):
	def run(self):
		print('Timer Start...')


# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()


# run_twice(Dog())
# run_twice(Cat())
# run_twice(Timer())


# d = Dog()
# print(type(d) == Dog)
# print(type(d) == Animal)

# print(isinstance(d, Dog))
# print(isinstance(d, Animal))


# print(dir(Dog()))

# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
	count = 0

	def __init__(self, name):
		self.name = name
		Student.count = Student.count + 1

# 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


######################### 使用@property #########################

# 练习
# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
	@property
	def width(self):
	    return self._width

	@width.setter
	def width(self, value):
		if not isinstance(value, float) and not isinstance(value, int):
			raise('width must be a number!')
		if value < 0:
			raise('width must be greater than 0')

		self._width = value

	@property
	def height(self):
	    return self._height

	@height.setter
	def height(self, value):
		if not isinstance(value, float) and not isinstance(value, int):
			raise('height must be a number!')
		if value < 0:
			raise('height must be greater than 0')

		self._height = value


	@property
	def resolution(self):
	    return self._width * self._height
	
# 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

######################### 定制类 #########################

### __str__ ###
class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name

	__repr__ = __str__

# 测试
s = Student('Xin')
print(s)

### __iter__ ###
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a

	def __getitem__(self, n):
		if isinstance(n, int): # 如果n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a	
		elif isinstance(n, slice): # 如果n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
		

# 测试
# for x in Fib():
# 	print(x)

### __getitem__ ###

# 测试
# f = Fib()
# print(f[0])
# print(f[1])
# print(f[2])
# print(f[12])

# print(f[2:5])

### __getattr__ ###
class Chain(object):
	def __init__(self, path=''):
		self._path = path
	
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__

c = Chain()
print(c.status.user.timeline.list)
print(c._path)

### __call__ ###
class Student(object):
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print('My name is %s' % self.name)

s = Student('Xin')
s()

print(callable(s))
print(callable(max))
print(callable([1, 2, 3]))
print(callable('str'))

######################### 枚举类 #########################

from enum import Enum, unique
@unique
class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

	@property
	def gender(self):
	    return self._gender

	@gender.setter
	def gender(self, value):
		if not isinstance(value, Gender):
			raise TypeError('value must be Gender enum!')
		self._gender = value

	def __str__(self):
		return 'name: %s, gender: %s' %(self.name, self.gender)
	__repr__ = __str__

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

######################### 元类 #########################

### type() ###

def fn(self, name='world...'):
	print('hello, ', name)

Person = type('Person', (object, ), dict(say = fn)) # 动态创建类

p1 = Person()
p1.say()

######################### metaclass #########################

# metaclass是类的模板，所以必须从`type`类型派生，metaclass的类名总是以Metaclass结尾：
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
	pass

l1 = MyList()
l1.add(1)
l1.append(2)
print(l1)

l2 = list()
l2.add(2)
print(l2)
		


