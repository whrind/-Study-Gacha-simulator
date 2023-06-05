# Gacha? simulator 抽卡模拟器
# python内置随机 random
"""In this case, we can see the distribution is very average.
    python make the random more reasonable,
    and it is too easy to get 6"""
import random


def main():
    s3 = [3]    # 40%
    s4 = [4]    # 50%
    s5 = [5]    # 8%
    s6 = [6]    # 2%
    pool = s3*400 + s4*500 + s5*80 + s6*20  #加权重 weight 1000
    gacha(pool)
    #test(pool)


def onetime(pool):
    print('Your result is ', pool[random.randint(0, 999)])


def tentime(pool):
    result = []
    for _ in range(10):
        result.append(pool[random.randint(0, 999)])
    print('Your result is ', result)


def test(pool):
    res = []
    for _ in range(1000):
        res.append(pool[random.randint(0,999)])
    print('The 3 (40%) has', res.count(3))
    print('The 4 (50%) has', res.count(4))
    print('The 5 (8%) has', res.count(5))
    print('The 6 (2%) has', res.count(6))


def gacha(pool):
    x = input('Please input your choice:(1 or 10, or q to quit) ')
    if x == '1':
        onetime(pool)
        gacha(pool)
    elif x == '10':
        tentime(pool)
        gacha(pool)
    elif x == 'q':
        print('Thanks your support!')
    else:
        print('Do not support it, please try again!')
        gacha(pool)


main()
