# Gacha? simulator 抽卡模拟器
# 60抽未出6星，下一概率+2%
# 60抽内2%， sum(?+?+?+?)/60 = 2%, 每 append 一次加 weight
import random
'''linear regression ?'''

def main():
    # s3 = [3]    # 40%
    # s4 = [4]    # 50%
    # s5 = [5]    # 8%
    # s6 = [6]    # 2%    initiative is 0.2%(2), gradually to 12.2%(122), avg is 2%, if 6 that reset to 0.2%
    # pool = s3*400 + s4*500 + s5*80 + s6*2  # 加权重 weight 1000
    pool = []
    rec = []
    check(pool, rec)
    gacha(pool)
    pass


def check(pool, rec):   # back modified pool
    s3 = [3]    # 40%
    s4 = [4]    # 50%
    s5 = [5]    # 8%
    s6 = [6]    # 2%    initiative is 0.2%(2), gradually to 12.2%(122), avg is 2%, if 6 that reset to 0.2%
    record = [6, 6]     # for initiative
    record += rec
    n = 981     # 0, 1, 2....
    if record.count(6) > 1:
        record.clear()
        pool = s3*400 + s4*500 + s5*80 + s6*2   # 加权重 weight 1000
        n = 981
        return pool, record, n
    else:
        pool += s6*2
        n += 2
        return pool, record, n


def onetime(pool):
    result = []
    rec = []
    pool = check(pool, rec)[0]
    n = check(pool, rec)[2]
    result.append(pool[random.randint(0, n)])
    rec += result
    check(pool, rec)    # give back the rec
    return rec, result


def tentime(pool):
    result = []
    rec = []
    for _ in range(10):
        pool = check(pool, rec)[0]
        n = check(pool, rec)[2]
        result.append(pool[random.randint(0, n)])
        rec += result
        check(pool, rec)
    return rec, result


def test(pool):      # test the choice distribution of pool
    res = []
    for _ in range(1000):
        res.append(pool[random.randint(0, 999)])
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
        print('Thanks for your support!')
    else:
        print('Do not support it, please try again!')
        gacha(pool)


main()