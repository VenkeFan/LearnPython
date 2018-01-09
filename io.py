#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### 文件读写 #########################

fPath = r'/Users/fanqi/Desktop/MyGit/LearnPython/iotest.txt'

with open(fPath, 'r') as f:
	str = f.read()
	print(str)

######################### StringIO #########################

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

print(f.getvalue())


f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break

	print(s.strip())

######################### BytesIO #########################

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())


f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
s = f.read()
print(s)

######################### 序列化 #########################

import pickle

d = dict(name='Bob', age=20, score=88)
f = open('dump.text', 'wb')
pickle.dump(d, f) # 序列化并写入文件
f.close()

f = open('dump.text', 'rb')
d = pickle.load(f) # 反序列化
f.close()
print('反序列化: ', d);

######################### JSON #########################

import json

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def studentToDict(std):
	return {'name': std.name, 'age': std.age, 'score': std.score}

def dictToStudent(d):
	return Student(d['name'], d['age'], d['score'])

s = Student('Tom', 20, 78)
print(json.dumps(s, default = studentToDict))
# # 偷懒的写法。因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
# josn.dumps(s, default = lambda obj: obj.__dict__)


jsonStr = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(jsonStr, object_hook = dictToStudent))

