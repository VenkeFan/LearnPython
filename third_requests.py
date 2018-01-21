#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### Get #########################

import requests

## 不带参数
# r = requests.get('https://www.douban.com')
# print('status: %s \n test: %s' %(r.status_code, r.text))

## 带参数
# r = requests.get('https://www.douban.com/search', params = {'q': 'python', 'cat': '1001'})
# print(r.url)
# print(r.encoding)
# print(r.content)

## json
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

## HTTP Header
# r = requests.get('https://www.douban.com/', headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text);

######################### Post #########################

## 默认为application/x-www-form-urlencoded
# r = requests.post('https://accounts.douban.com/login', data = {'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r.text)

## json
# params = {'key': 'value'}
# r = requests.post(url, json = params)

## 上传文件
## 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files = upload_files)

######################### 获取HTTP响应的其他信息 #########################

## 响应头
# r = requests.get('http://www.python.org')
# print(r.headers)
# print(r.headers['Content-Type'])

## 获取Cookie
# print(r.cookies['ts'])

## 传入Cookie
# cs = {'token': '12345', 'status': 'working')
# r = requests.get(url, cookies = cs)

## 指定超时
r = requests.get(url, timeout = 2.5) # 2.5秒