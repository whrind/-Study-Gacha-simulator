import random


def main():
    slist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    scount = len(slist)
    print(queue(scount))




def queue(c):
    randomlist = []
    randomlist.append(random.randint(0, c-1))
    t = 0
    while len(randomlist) < c:
        randomlist.append(random.randint(0, c - 1))
        t += 1
        if randomlist.count(randomlist[t]) > 1:
            randomlist.pop()



def listreapeat(lis):
    l = len(lis)



main()
