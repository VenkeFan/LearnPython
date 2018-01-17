#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################### 获取当前日期和时间 #########################

# from datetime import datetime

# now = datetime.now()
# print(now)
# print(type(now))

######################### 获取指定日期和时间 #########################

# from datetime import datetime

# dt = datetime(2018, 1, 17, 7, 30)
# print(dt)

######################### datetime转timestamp #########################

# from datetime import datetime

# dt = datetime.now()
# print(dt.timestamp())

######################### timestamp转datetime #########################

# from datetime import datetime

# t = 1429417200.0
# print('local: ', datetime.fromtimestamp(t))
# print('utc+0: ', datetime.utcfromtimestamp(t))

######################### str转datetime #########################

# from datetime import datetime

# cd = datetime.strptime('2018-1-17 9:13:25', '%Y-%m-%d %H:%M:%S')
# print(cd)

######################### datetime转str #########################

# from datetime import datetime

# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

######################### datetime加减 #########################

# from datetime import datetime, timedelta

# now = datetime.now()
# print(now)
# print(now + timedelta(hours = 10))
# print(now - timedelta(days = 1))
# print(now + timedelta(days = 2, hours = 12))

######################### 本地时间转UTC时间 #########################

# from datetime import datetime, timedelta, timezone

# tz_utc_8 = timezone(timedelta(hours = 8)) # 创建时区UTC+8:00
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo = tz_utc_8) # 强制设置为UTC+8:00
# print(dt)

######################### 时区转换 #########################

from datetime import datetime, timedelta, timezone

utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc) # 拿到UTC时间，并强制设置时区为UTC+0:00
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8))) # astimezone()将转换时区为北京时间:
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9))) # 将UTC+0转换时区为东京时间
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours = 9))) # 将bj_dt转换时区为东京时间
print(tokyo_dt2)