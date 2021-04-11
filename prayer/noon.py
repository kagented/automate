from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import re

res = requests.get('https://www.noonprayerkorea.com')

html = res.content

soup = BeautifulSoup(html, 'html.parser')

text = soup.find_all(text=True)

output = ''

blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    'style',
    ]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

output = output[1000:-110]

print(output)

f = open('noon.txt', 'w', encoding='UTF8')

f.write(output)

f.close()
