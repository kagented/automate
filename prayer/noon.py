from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import re

res = requests.get('https://www.noonprayerkorea.com')

html = res.content

soup = BeautifulSoup(html, 'html.parser')

text = soup.select_one('#comp-jbykc7h3').text

print(text)

f = open('noon.txt', 'w', encoding='UTF8')

f.write(text)

f.close()
