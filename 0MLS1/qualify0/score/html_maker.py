from bs4 import BeautifulSoup
import json
with open('./score_table_layout.html', 'r', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp.read(), 'lxml')
with open('./show_data.json', 'r', encoding='utf-8') as fp:
    data = json.loads(fp.read())

ids = data.keys()
ids = sorted(ids, key=lambda x: data[x]['sum'], reverse=True)

for id in ids:
    if data[id]['basic']:
        data[id]['s_class'] = 'text-secondary'
        data[id]['prob_s'] = '/'
        data[id]['th'] = '%d*' % data[id]['th']
    else:
        data[id]['s_class'] = ''
        data[id]['prob_s'] = '%.1lf%%' % (data[id]['prob'] * 100)
    if data[id]['change'] > 0:
        data[id]['change_s'] = '+%d' % data[id]['change']
        data[id]['c_class'] = 'text-success'
    elif data[id]['change'] < 0:
        data[id]['change_s'] = '%d' % data[id]['change']
        data[id]['c_class'] = 'text-danger'
    else:
        data[id]['change_s'] = '=0'
        data[id]['c_class'] = 'text-secondary'
    data[id]['score1'] = data[id].get('score1', '-')
    data[id]['score2'] = data[id].get('score2', '-')
    data[id]['score3'] = data[id].get('score3', '-')
    data[id]['score4'] = data[id].get('score4', '-')
    td = '''
<tr>
    <td class="{s_class}">{th}</td>
    <td class="{s_class} {c_class}">{change_s}</td>
    <td style="width:50px;background:{hex}"></td>
    <td class="{s_class}">{name}</td>
    <td class="{s_class}">{score1}</td>
    <td class="{s_class}">{score2}</td>
    <td class="{s_class}">{score3}</td>
    <td class="{s_class}">{score4}</td>
    <td class="{s_class}">{sum}</td>
    <td class="{s_class}">{prob_s}</td>
</tr>
'''.format(**data[id])
    soup.tbody.append(BeautifulSoup(td, 'lxml'))

with open('score_table.html', 'wb') as fp:
    fp.write(soup.prettify('utf-8'))
