# Gacha? simulator 抽卡模拟器
# 真随机
import random

s3 = [3]    # 40%
s4 = [4]    # 50%
s5 = [5]    # 8%
s6 = [6]    # 2%
pool = s3*40 + s4*50 + s5*8 + s6*2  #加权重
result = []

for t in range(10):
    result.append(pool[random.randint(0, 99)])

print('Your result is ', result)
