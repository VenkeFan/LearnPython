#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 请写一个能处理去掉=的base64解码函数
import base64

def safe_base64_decode(s):
	remainder = len(s) % 4
	for i in range(4 - remainder):
		s += b'='

	return base64.b64decode(s)



# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')