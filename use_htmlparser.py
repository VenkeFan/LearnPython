#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):
# 	def handle_starttag(self, tag, attrs):
# 		print('handle_starttag: <%s>' % tag)

# 	def handle_endtag(self, tag):
# 		print('handle_endtag: </%s>' % tag)

# 	def handle_startendtag(self, tag, attrs):
# 		print('handle_startendtag: <%s/>' % tag)

# 	def handle_data(self, data):
# 		print('handle_data: ', data)

# 	def handle_comment(self, data):
# 		print('handle_comment: <!--', data, '-->')

# 	def handle_entityref(self, name):
# 		print('handle_entityref: &%s;' % name)

# 	def handle_charref(self, name):
# 		print('handle_charref: &#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

## 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

from html.parser import HTMLParser
from urllib import request

class MyHTMLParser(HTMLParser):
	def __init__(self):
		super( MyHTMLParser, self).__init__()
		self._attrs = {}
		self.title = ''
		self.dt = ''
		self.location = ''

	def handle_starttag(self, tag, attrs):
			print('handle_starttag: <%s>, attrs: %s' % (tag, str(attrs)))
			for t in attrs:
				if len(t) > 1 and not t[0] in self._attrs:
					self._attrs[t[0]] = t[1]

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		print(self._attrs)
		# if 'class' in self._attrs:
		# 	if self._attrs['class'] == 'event-title':
		# 		self.title = data
		# 	elif self._attrs['class'] == 'event-location':
		# 		self.location = data
		# if 'datetime' in self._attrs and self._attrs['datetime']:
		# 	self.dt = data
		

def get_html(url):
	with request.urlopen(url) as f:
		if f.status == 200:
			return f.read().decode('utf-8')
		else:
			return None


html = get_html('https://www.python.org/events/python-events/')

parser = MyHTMLParser()
parser.feed(html)
print('title: %s, datetime: %s, location: %s' % (parser.title, parser.dt, parser.location))


