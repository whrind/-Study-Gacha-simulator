# Gacha? simulator 抽卡模拟器
# 真随机
import random

s3 = [3]    # 40%
s4 = [4]    # 50%
s5 = [5]    # 8%
s6 = [6]    # 2%
pool = s3*400 + s4*500 + s5*80 + s6*20  #加权重
result = []

for t in range(10):
    result.append(pool[random.randint(0, 999)])

print('Your result is ', result)
