import time

# 时间戳
print(time.time())

# 结构化时间
print(time.localtime())
# 格林尼治时间
print(time.gmtime())

# 结构化时间转化为时间戳
print(time.mktime(time.localtime()))

# 字符串时间转化
print(time.strftime("%Y-%m-%d %X", time.localtime()))
print(time.strptime("2018-02-10 15:13:50","%Y-%m-%d %X"))


print(time.asctime())
print(time.ctime())