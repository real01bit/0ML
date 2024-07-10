import requests
fp = open('color_table.html', 'wb')
fp.write(requests.get('https://www.w3.org/TR/css-color-3/#svg-color').content)
