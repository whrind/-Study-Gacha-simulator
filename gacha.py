# Gacha? simulator 抽卡模拟器
# 真随机 real random
import random


def main():
    s3 = [3]    # 40%
    s4 = [4]    # 50%
    s5 = [5]    # 8%
    s6 = [6]    # 2%
    pool = s3*400 + s4*500 + s5*80 + s6*20  #加权重 weight 1000


def onetime(pool):
    print('Your result is ', pool[random.randint(0, 999)])


def tentime(pool):
    result = []
    for _ in range(10):
        result.append(pool[random.randint(0, 999)])
    print('Your result is ', result)

def gacha():



main()
