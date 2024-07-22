from bs4 import BeautifulSoup
import json
marbles = {}
hexes = []

with open('color_table.html', 'r', encoding='utf-8') as fp:
    content = fp.read()
    soup = BeautifulSoup(content, 'lxml')
tables = soup.find_all('table', {'class': 'colortable'})

tbody = tables[1].tbody
trs = tbody.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    if len(tds) == 0:
        continue
    id = tds[2].dfn.string.strip()
    marble = {}
    marble['name'] = id.capitalize()
    marble['hex'] = tds[3].string.strip()
    marble['color'] = [int(i) for i in tds[4].string.strip().split(',')]
    marble['basic'] = False
    if marble['hex'] not in hexes:
        marbles[id] = marble
        hexes.append(marble['hex'])

tbody = tables[0].tbody
trs = tbody.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    if len(tds) == 0:
        continue
    id = tds[2].dfn.string.strip()
    marbles[id]['basic'] = True

with open('marble_list.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(marbles, ensure_ascii=False))
