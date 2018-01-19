#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### “无限”迭代器#########################

import itertools

# natuals = itertools.count(1)
# for n in natuals:
# 	if n > 20:
# 		break
# 	print(n)


cs = itertools.cycle('ABC', 3)
for c in cs:
	print(c)