import json
fp = open('./Q3_sel.txt', 'r')
raw = fp.read()
fp.close()
ids = [[], [], [], [], []]
mids = raw.split(';')
for mid in mids:
    if mid == '':
        break
    id = mid.split(',')[0]
    sel = int(mid.split(',')[1])
    for i in range(5):
        if sel & (1 << i) > 0:
            ids[i].append(id)
with open('Q3s_data.json', 'w') as ouf:
    ouf.write(json.dumps(ids))
print('%d,%d,%d,%d,%d' %
      (len(ids[0]), len(ids[1]), len(ids[2]), len(ids[3]), len(ids[4])))
