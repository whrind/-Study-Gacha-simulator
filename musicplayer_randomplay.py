import random


def main():
    slist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 8 songs
    scount = len(slist)
    q = queue(scount)
    nslist = []
    for i in range(scount):
        nslist.append(slist[q[i]])
    print('The song list is', nslist)


def queue(c):  # make a random queue
    randomlist = []
    # randomlist.append(random.randint(0, c - 1))
    t = 0
    while len(randomlist) < c:
        randomlist.append(random.randint(0, c - 1))
        if randomlist.count(randomlist[t]) > 1:
            randomlist.remove(randomlist[t])
        else:
            t += 1
            # randomlist.append(random.randint(0, c - 1))
    return randomlist


main()
