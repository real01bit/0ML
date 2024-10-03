import random


def prob_calc(data, m, n):
    ids = []
    for key in data.keys():
        if not data[key]['basic']:
            ids.append(key)
    res = {}
    sr = [i for i in range(138)]
    for id in ids:
        res[id] = 0
    for i in range(n):
        print('\r%d/%d [%s] %.1lf%%' %
              (i, n, '='*round(i/n*40)+' '*(40-round(i/n*40)), i/n*100), end='')
        td = {}
        for key in ids:
            td[key] = data[key]['sum']
        for j in range(m):
            tsr = sr
            random.shuffle(tsr)
            for k in range(len(ids)):
                td[ids[k]] += tsr[k]
        tid = sorted(ids, key=lambda x: td[x], reverse=True)
        for j in range(43):
            res[tid[j]] += 1
    print('\r%d/%d [========================================] OK' % (n, n))
    return res
