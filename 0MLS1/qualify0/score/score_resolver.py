import re
import json
scoretable = {}
with open('R1raw.txt', 'r', encoding='utf-8') as fp:
    R1raw = fp.read()
    for i in R1raw.split('\n'):
        i = i.strip()
        if i == '':
            continue
        j = re.match('\S+ (\S+) (\d+)pts', i)
        name = j.group(1)
        score = int(j.group(2))
        scoretable[name] = [score]

with open('R2raw.txt', 'r', encoding='utf-8') as fp:
    R2raw = fp.read()
    for i in R2raw.split('\n'):
        i = i.strip()
        if i == '':
            continue
        j = re.match('\S+ (\S+) (\d+)pts', i)
        name = j.group(1)
        score = int(j.group(2))
        score2 = score - scoretable[name][0]
        scoretable[name].append(score2)

scoredata = {}
for i in scoretable.items():
    scoredata[i[0].lower()] = {'score1': i[1][0], 'score2': i[1][1]}

with open('score_table.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(scoredata))
