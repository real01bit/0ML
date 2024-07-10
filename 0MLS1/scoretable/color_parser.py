from bs4 import BeautifulSoup
import json
with open('color_table.html', 'r', encoding='utf-8') as fp:
    content = fp.read()
    soup = BeautifulSoup(content, 'lxml')
table = soup.find('table', {'class': 'colortable'})
tbody = table.tbody
trs = tbody.find_all('tr')
marbles = []
hexes = []
for tr in trs:
    tds = tr.find_all('td')
    marble = {}
    if len(tds) == 0:
        continue
    marble['id'] = tds[2].dfn.string.strip()
    marble['name'] = marble['id'].capitalize()
    marble['hex'] = tds[3].string.strip()
    marble['color'] = [int(i) for i in tds[4].string.strip().split(',')]
    if marble['hex'] not in hexes:
        marbles.append(marble)
        hexes.append(marble['hex'])
with open('marble_list.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(marbles, ensure_ascii=False))
