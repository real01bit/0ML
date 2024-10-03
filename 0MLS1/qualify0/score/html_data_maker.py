import json
from probability_calc import prob_calc
data = {}
ids = []
last_sum_keys = ['score1']
sum_keys = ['score1', 'score2']
with open('./../data/marble.json', 'r', encoding='utf-8') as fp:
    marble_data = json.loads(fp.read())
with open('./../data/score.json', 'r', encoding='utf-8') as fp:
    score_data = json.loads(fp.read())
for mid in marble_data.keys():
    ids.append(mid)
    data[mid] = {}
    data[mid]['name'] = marble_data[mid]['name']
    data[mid]['hex'] = marble_data[mid]['hex']
    data[mid]['basic'] = marble_data[mid]['basic']
    data[mid]['sum'] = 0
    data[mid]['sum0'] = 0
    for key in sum_keys:
        data[mid][key] = score_data[mid][key]
        data[mid]['sum'] += data[mid][key]
    for key in last_sum_keys:
        data[mid]['sum0'] += data[mid][key]

sid = sorted(ids, key=lambda x: data[x]['sum0'], reverse=True)
th = 0
bth = 0
pid = ''
pbid = ''
for mid in sid:
    if data[mid]['basic']:
        bth += 1
        if pbid != '' and data[pbid]['sum0'] == data[mid]['sum0']:
            data[mid]['th0'] = data[pbid]['th0']
        else:
            data[mid]['th0'] = bth
        pbid = mid
    else:
        th += 1
        if pid != '' and data[pid]['sum0'] == data[mid]['sum0']:
            data[mid]['th0'] = data[pid]['th0']
        else:
            data[mid]['th0'] = th
        pid = mid

sid = sorted(ids, key=lambda x: data[x]['sum'], reverse=True)
th = 0
bth = 0
pid = ''
pbid = ''
for mid in sid:
    if data[mid]['basic']:
        bth += 1
        if pbid != '' and data[pbid]['sum'] == data[mid]['sum']:
            data[mid]['th'] = data[pbid]['th']
        else:
            data[mid]['th'] = bth
        pbid = mid
    else:
        th += 1
        if pid != '' and data[pid]['sum'] == data[mid]['sum']:
            data[mid]['th'] = data[pid]['th']
        else:
            data[mid]['th'] = th
        pid = mid
    data[mid]['change'] = data[mid]['th0'] - data[mid]['th']

n = 1000000
res = prob_calc(data, 2, n)
for mid in ids:
    if data[mid]['basic']:
        data[mid]['prob'] = -1
    else:
        data[mid]['prob'] = res[mid] / n


with open('./show_data.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(data))
