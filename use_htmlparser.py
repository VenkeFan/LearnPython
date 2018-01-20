#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('handle_starttag: <%s>' % tag)

	def handle_endtag(self, tag):
		print('handle_endtag: </%s>' % tag)

	def handle_startendtag(self, tag, attrs):
		print('handle_startendtag: <%s/>' % tag)

	def handle_data(self, data):
		print('handle_data: ', data)

	def handle_comment(self, data):
		print('handle_comment: <!--', data, '-->')

	def handle_entityref(self, name):
		print('handle_entityref: &%s;' % name)

	def handle_charref(self, name):
		print('handle_charref: &#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

## 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

# from html.parser import HTMLParser
# from urllib import request
# import re

# class MyHTMLParser(HTMLParser):
# 	def __init__(self):
# 		super( MyHTMLParser, self).__init__()
# 		self.flag = False
# 		self.result = []

# 		self.dic = {}
# 		self.key = ''

# 	def handle_starttag(self, tag, attrs):
# 		if len(attrs) > 0  and attrs[0][1] == 'list-recent-events menu':
# 			self.flag = True
# 		if self.flag == True:
# 			if tag == 'a':
# 				self.key = 'title'
# 			if tag == 'time':
# 				self.key = 'time'
# 			if tag == 'span':
# 				self.key = 'location'


# 	def handle_endtag(self, tag):
# 		if tag == 'ul' and self.flag == True:
# 			self.flag = False
# 		if self.flag == True and tag == 'li':
# 			self.result.append(self.dic)
# 			self.dic = {}


# 	def handle_data(self, data):
# 		if self.key != '':
# 			self.dic[self.key] = data
# 			self.key = ''
		

# def get_html(url):
# 	with request.urlopen(url) as f:
# 		if f.status == 200:
# 			return f.read().decode('utf-8')
# 		else:
# 			return None


# html = get_html('https://www.python.org/events/python-events/')

# parser = MyHTMLParser()
# parser.feed(html)
# for item in parser.result:
#     for (k, v) in item.items():
#         print('%s: %s' % (k, v))
#     print('-------------------')


