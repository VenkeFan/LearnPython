#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### namedtuple #########################

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y']) # namedtuple('名称', [属性list]) 
# p = Point(10, 20)
# print("x: %s, y: %s" % (p.x, p.y))

######################### deque #########################

# from collections import deque

# # deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# q.insert(2, 'z')
# print(q)

######################### defaultdict #########################

# from collections import defaultdict

# # 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# # 如果希望key不存在时，返回一个默认值，就可以用defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key'] = 'abc'
# print(dd['key'])
# print(dd['key2'])

######################### OrderedDict #########################

# from collections import OrderedDict

# # 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序

# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)

# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)

# od = OrderedDict()
# od['z'] = 1
# od['y'] = 2
# od['x'] = 3
# print(list(od.keys()))

######################### Counter #########################

from collections import Counter

c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print(c)