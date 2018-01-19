#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### __enter__ / __exit__ #########################

# class Query(object):
# 	def __init__(self, name):
# 		self.name = name

# 	def __enter__(self):
# 		print('Begin')
# 		return self

# 	def __exit__(self, exc_type, exc_value, traceback):
# 		if exc_type:
# 			print('Error')
# 		else:
# 			print('End')

# 	def query(self):
# 		print('Query info about %s...' % self.name)

# with Query('Tom') as q:
# 	q.query()

######################### @contextmanager #########################

# from contextlib import contextmanager

## Example1:
# class  Query(object):
# 	def __init__(self, name):
# 		super( Query, self).__init__()
# 		self.name = name

# 	def query(self):
# 		print('Query info about %s...' % self.name)

# @contextmanager
# def create_query(name):
# 	print('Begin')
# 	q = Query(name)
# 	yield q
# 	print('End')

# with create_query('Amy') as q:
# 	q.query()


## Example2:
# @contextmanager
# def tag(name):
# 	print('<%s>' % name)
# 	yield
# 	print('</%s>' % name)

# with tag('h1'):
# 	print('hello')
# 	print('world')

######################### @closing #########################

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
	for line in page:
		print(line)

		