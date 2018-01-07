#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### 单元测试 #########################

import unittest

# from mydict import MyDict

# class TestDict(unittest.TestCase):
# 	"""docstring for TestDict"""

# 	def setUp(self):
# 		print('setUp...')

# 	def tearDown(self):
# 		print('tearDown...')

# 	def test_init(self):
# 		d = MyDict(a=1, b='test')
# 		self.assertEqual(d.a, 1);
# 		self.assertEqual(d.b, 'test')
# 		self.assertTrue(isinstance(d, dict))

# 	def test_key(self):
# 		d = MyDict()
# 		d['key'] = 'value'
# 		self.assertEqual(d.key, 'value')
		
# 	def test_attr(self):
# 		d = MyDict()
# 		d.key = 'value'
# 		self.assertTrue('key' in d)
# 		self.assertEqual(d['key'], 'value')

# 	def test_keyerror(self):
# 		d = MyDict()
# 		with self.assertRaises(KeyError):
# 			value = d['empty']

# 	def test_attrerror(self):
# 		d = MyDict()
# 		with self.assertRaises(AttributeError):
# 			value = d.empty

######################### setUp与tearDown #########################

# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
# 这两个方法会分别在每调用一个测试方法的前后分别被执行。


# 运行单元测试
# 方法一：
# if __name__ == '__main__':
# 	unittest.main()

# 方法二：
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试：$ python -m unittest mydict_test
# 这是推荐的做法，因为这样可以一次批量运行很多单元测试


# 练习

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
    	if self.score < 0 or self.score > 100:
    		raise ValueError()
    	if self.score >= 80:
    		return 'A'
    	if self.score >= 60:
    		return 'B'
    	return 'C'

class TestStudent(unittest.TestCase):
	def test_80_to_100(self):
		s1 = Student('Tom', 80)
		s2 = Student('Jerry', 100)
		self.assertEqual(s1.get_grade(), 'A')
		self.assertEqual(s2.get_grade(), 'A')

	def test_60_to_80(self):
		s1 = Student('Tom', 60)
		s2 = Student('Jerry', 79)
		self.assertEqual(s1.get_grade(), 'B')
		self.assertEqual(s2.get_grade(), 'B')

	def test_0_to_60(self):
		s1 = Student('Tom', 0)
		s2 = Student('Jerry', 59)
		self.assertEqual(s1.get_grade(), 'C')
		self.assertEqual(s2.get_grade(), 'C')
	
	def test_invalid(self):
		s1 = Student('Tom', -1)
		s2 = Student('Jerry', 101)
		with self.assertRaises(ValueError):
			s1.get_grade()
		with self.assertRaises(ValueError):
			s2.get_grade()