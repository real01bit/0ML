import csv
from bs4 import BeautifulSoup
soup = BeautifulSoup()
table = soup.new_tag('table')
table.append('''<thead>
<th>#</th>
<th>Name</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>Sum</th>
<th>Promotion probability</th>
</thead>''')
tbody = soup.new_tag('tbody')

data = []
with open('score_table.csv', 'r', newline='', encoding='utf-8') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        row['name'] = row['id'].capitalize()
        row['sum'] = int(row.get('score1', 0))+int(row.get('score2', 0)) + \
            int(row.get('score3', 0))+int(row.get('score4', 0))
        row['pp'] = 0
        data.append(row)
data = sorted(data, key=lambda x: x['sum'], reverse=True)
th = 1
friendly = ['black', 'silver', 'gray', 'white', 'maroon', 'red', 'purple',
            'magenta', 'green', 'lime', 'olive', 'yellow', 'navy', 'blue', 'teal', 'cyan', 'orange']
fth = 1
for row in data:
    tr = soup.new_tag('tr')

    if row['id'] in friendly:
        tr.append('<td style=\'color:gray\'>%d</td>' % fth)
        fth += 1
    else:
        tr.append('<td>%d</td>' % th)
        th += 1
    print(row)
    tr.append('''<td>{0[name]}</td>
<td>{0[score1]}</td>
<td>{0[score2]}</td>
<td style=\'color:gray\'>-</td>
<td style=\'color:gray\'>-</td>
<td>{0[sum]}</td>
<td>{0[pp]}</td>'''.format(row))
    tbody.append(tr)
table.append(tbody)
soup.append(table)
with open('score_table.html', 'w', encoding='utf-8') as fp:
    print()
    fp.write(soup.prettify())
