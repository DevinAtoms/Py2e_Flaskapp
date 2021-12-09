import re

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

spells_link = re.compile(r'Spells.aspx\?Tradition=[0-9]')

URL = "https://2e.aonprd.com/Spells.aspx?ID=3"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'templates.parser', from_encoding='ISO-8859-7')

name = soup.find('span', id="ctl00_RadDrawer1_Content_MainContent_DetailedOutput").next_sibling
print(name)

traits = soup.find_all('span', class_='trait')
trait_list = []
for t in traits:
    trait_list.append(t.a.get_text())

print(trait_list)

traditions = soup.find_all('a', href=re.compile(r'Spells.aspx\?Tradition=[1-9]'))
tradition_list = []
for tr in traditions:
    tradition_list.append(tr.get_text().title())

print(tradition_list)

bloodline = soup.find_all('a', href=re.compile(r'Bloodlines.aspx\?ID=[0-9]'))
for b in bloodline:
    print(b.get_text().title())

actions = soup.find_all('img', alt=re.compile(r'Actions'))
print(actions[1]['alt'])

action_type = soup.find_all('a', href=re.compile(r'Rules.aspx\?ID=[\d]+'))
action_list = []
for at in action_type:
    action_list.append(at.get_text().title())

print(action_list)


span = soup.find(id='main').extract()

spanlist = []
for ch in span.children:
    if re.fullmatch(r'[\s\W\D]+', ch.text):
        pass
    else:
        if type(ch) is not Tag or re.match(r'Heightened\s\W[\d]+[\w]+\W', ch.text):
            spanlist.append(ch.get_text().strip())
        else:
            pass

spanlist = [re.sub(r"[^.)(+,'\d\w\s?!]", '', s) for s in spanlist]

print(spanlist)



