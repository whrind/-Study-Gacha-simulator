# Gacha? simulator 抽卡模拟器
# 60抽未出6星，下一概率+2%
# 60抽内2%， sum(?+?+?+?)/60 = 2%, 每 append 一次加 weight
import random
'''linear regression ?'''

gpool = []      # global variable
grec = []
gn = 0
gresult = []


def main():
    # s3 = [3]    # 40%
    # s4 = [4]    # 50%
    # s5 = [5]    # 8%
    # s6 = [6]    # 2%    initiative is 0.2%(2), gradually to 12.2%(122), avg is 2%, if 6 that reset to 0.2%
    # pool = s3*400 + s4*500 + s5*80 + s6*2  # 加权重 weight 1000
    init()
    test()
    pass


def init():
    global gpool, gn
    s3 = [3]  # 40%
    s4 = [4]  # 50%
    s5 = [5]  # 8%
    s6 = [6]  # 2%    initiative is 0.2%(2), gradually to 12.2%(122), avg is 2%, if 6 that reset to 0.2%
    gn += 981  # 0, 1, 2....
    gpool += s3 * 400 + s4 * 500 + s5 * 80 + s6 * 2  # 加权重 weight 1000


def check():   # return modified pool
    global gpool, grec, gn
    # record = []     # for initiative
    # record += rec
    if grec.count(6) > 0:
        grec.clear()
        init()
    else:
        gpool += [6]*1
        gn += 1


def onetime():  # 解包一次get，把rec储存，下次get在返回rec
    global gpool, grec, gn
    result = []
    result.append(gpool[random.randint(0, gn)])
    grec += result
    result.clear()
    check()


def tentime():
    global gpool, grec, gn
    result = []
    for _ in range(10):
        result.append(gpool[random.randint(0, gn)])
        grec += result
        result.clear()
        check()


def test():      # test the choice distribution of pool
    global gpool, grec, gn, gresult
    result = []
    for _ in range(1000):
        # res.append(pool[random.randint(0, 999)])
        result.append(gpool[random.randint(0, gn)])
        grec += result
        gresult += result
        result.clear()
        check()
        # print('The 3 (40%) has', gpool.count(3))
        # print('The 4 (50%) has', gpool.count(4))
        # print('The 5 (8%) has', gpool.count(5))
        # print('The 6 (2%) has', gpool.count(6))
    total = gresult.count(3) + gresult.count(4) + gresult.count(5) + gresult.count(6)
    print(f"Final 3 (40%) is {(gresult.count(3)/total)*100:.2f}%")
    print(f'Final 4 (50%) is {(gresult.count(4)/total)*100:.2f}%')
    print(f'Final 5 (8%) is {(gresult.count(5)/total)*100:.2f}%')
    print(f'Final 6 (2%) is {(gresult.count(6)/total)*100:.2f}%')


def gacha(pool):
    x = input('Please input your choice:(1 or 10, or q to quit) ')
    if x == '1':
        print('Your result is ', onetime(pool)[1])
        print('rec is ', onetime(pool)[0])
        gacha(pool)
    elif x == '10':
        print('Your result is ', tentime(pool)[1])
        gacha(pool)
    elif x == 'q':
        print('Thanks for your support!')
    else:
        print('Do not support it, please try again!')
        gacha(pool)


main()
