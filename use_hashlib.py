#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 根据用户输入的口令，计算出存储在数据库中的MD5口令
# import hashlib

# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }

# def login(user, password):
# 	md5 = hashlib.md5()
# 	md5.update(password.encode('utf-8'))
# 	return db[user] == md5.hexdigest()


# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')


# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
import hashlib, random

db = {}

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + username + self.salt)

def register(username, password):
	user = User(username, password)
	db[username] = user

def get_md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()


def login(username, password):
	user = db[username]
	md5_pwd = get_md5(password + username + user.salt)
	return user.password == md5_pwd


# 测试:
register('Tom', 'python3qaz')
assert login('Tom', 'python3qaz')
assert not login('Tom', '123456')
print('ok')