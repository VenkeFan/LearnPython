#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### Get #########################

# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
# 	data = f.read()
# 	print('Status: ', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data: ', data.decode('utf-8'))


## 模拟浏览器发送GET请求

# req = request.Request('http://www.douban.com')
# # 模拟iPhone 6发起请求
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
# 	print('Status: ', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data: ', f.read().decode('utf-8'))

######################### Post #########################

# from urllib import request, parse

# print('Login to weibo.cn...')
# email = input('Email: ')
# password = input('Password: ')
# login_data = parse.urlencode([
# 	('username', email),
# 	('password', password),
# 	('entry', 'mweibo'),
# 	('cliend_id', ''),
# 	('savestate', '1'),
# 	('ec', ''),
# 	('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# 	])

# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data = login_data.encode('utf-8')) as f:
# 	print('Status: ', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data:', f.read().decode('utf-8'))

######################### Handler #########################

# from urllib import request

# proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = request.build_opener(proxy_handler, proxy_auth_handler)

# with opener.open('http://www.example.com/login.html') as f:
# 	print('Status: ', f.status, f.reas)


# 练习
# 利用urllib读取JSON，然后将JSON解析为Python对象

from urllib import request
import json

def fetch_data(url):
	with request.urlopen(url) as f:
		if f.status == 200:
			return json.loads(f.read().decode('utf-8'))
		else:
			return None


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')

