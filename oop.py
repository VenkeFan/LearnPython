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
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

