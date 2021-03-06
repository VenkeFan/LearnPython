#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 根据用户输入的口令，计算出存储在数据库中的MD5口令
import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
	md5 = hashlib.md5()
	hashPwd = md5.update(password, 'utf-8')
	return db[user] == hashPwd


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')