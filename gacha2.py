# Gacha? simulator 抽卡模拟器
# 60抽未出6星，下一概率+2%
import random

s3 = [3]    # 40%
s4 = [4]    # 50%
s5 = [5]    # 8%
s6 = [6]    # 2%
pool = s3*40 + s4*50 + s5*8 + s6*2  #加权重
result = []