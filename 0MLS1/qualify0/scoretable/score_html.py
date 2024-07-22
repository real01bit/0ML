import json
from bs4 import BeautifulSoup
data = {}
score_data = {}
keys = ['score1']
last_key = 'score2'
with open('../marble/marble_list.json', 'r', encoding='utf-8') as fp:
    data = json.loads(fp.read())
with open('score_table.json', 'r', encoding='utf-8') as fp:
    score_data = json.loads(fp.read())

with open('score_table_layout.html', 'r', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp.read(), 'lxml')
tbody = soup.tbody

score_list_0 = []
for marble_id in score_data.keys():
    score_data[marble_id]['sum0'] = 0
    for key in keys:
        score_data[marble_id]['sum0'] += score_data[marble_id][key]
    score_list_0.append(
        {'id': marble_id, 'score': score_data[marble_id]['sum0']})
score_list_0 = sorted(score_list_0, key=lambda x: x['score'], reverse=True)
th0 = 1
lt0 = 1
ls0 = 0
fth0 = 1
flt0 = 1
fls0 = 0
for row in score_list_0:
    marble_id = row['id']
    score = row['score']
    if data[marble_id]['basic']:
        if score != fls0:
            flt0 = fth0
        score_data[marble_id]['th0'] = flt0
        fls0 = score
        fth0 += 1
    else:
        if score != ls0:
            lt0 = th0
        score_data[marble_id]['th0'] = lt0
        ls0 = score
        th0 += 1

score_list = []
for marble_id in score_data.keys():
    score_data[marble_id]['sum'] = score_data[marble_id]['sum0'] + \
        score_data[marble_id][last_key]
    score_list.append(
        {'id': marble_id, 'score': score_data[marble_id]['sum']})
score_list = sorted(score_list, key=lambda x: x['score'], reverse=True)
th = 1
lt = 1
ls = 0
fth = 1
flt = 1
fls = 0
for row in score_list:
    marble_id = row['id']
    score = row['score']
    if data[marble_id]['basic']:
        if score != fls:
            flt = fth
        score_data[marble_id]['th'] = flt
        fls = score
        fth += 1
    else:
        if score != ls:
            lt = th
        score_data[marble_id]['th'] = lt
        ls = score
        th += 1

for row in score_list:
    marble_id = row['id']
    tr = soup.new_tag('tr')

    td_th = soup.new_tag('td')
    td_th.string = str(score_data[marble_id]['th'])
    if data[marble_id]['basic']:
        td_th['class'] = 'text-secondary'
    tr.append(td_th)

    td_change = soup.new_tag('td')
    change = score_data[marble_id]['th0'] - score_data[marble_id]['th']
    if change > 0:
        td_change.string = '+' + str(change)
    else:
        td_change.string = str(change)
    if data[marble_id]['basic']:
        td_change['class'] = 'text-secondary'
    tr.append(td_change)

    td_name = soup.new_tag('td')
    td_name.string = data[marble_id]['name']
    if data[marble_id]['basic']:
        td_name['class'] = 'text-secondary'
    tr.append(td_name)

    td_1 = soup.new_tag('td')
    td_1.string = str(score_data[marble_id]['score1'])
    if data[marble_id]['basic']:
        td_1['class'] = 'text-secondary'
    tr.append(td_1)

    td_2 = soup.new_tag('td')
    td_2.string = str(score_data[marble_id]['score2'])
    if data[marble_id]['basic']:
        td_2['class'] = 'text-secondary'
    tr.append(td_2)

    td_3 = soup.new_tag('td')
    td_3.string = '-'
    if data[marble_id]['basic']:
        td_3['class'] = 'text-secondary'
    tr.append(td_3)

    td_4 = soup.new_tag('td')
    td_4.string = '-'
    if data[marble_id]['basic']:
        td_4['class'] = 'text-secondary'
    tr.append(td_4)

    td_sum = soup.new_tag('td')
    td_sum.string = str(score_data[marble_id]['sum'])
    if data[marble_id]['basic']:
        td_sum['class'] = 'text-secondary'
    tr.append(td_sum)

    td_pp = soup.new_tag('td')
    td_pp.string = '/'
    if data[marble_id]['basic']:
        td_pp['class'] = 'text-secondary'
    tr.append(td_pp)

    tbody.append(tr)

with open('score_table.html', 'wb') as fp:
    fp.write(soup.prettify('utf-8'))
