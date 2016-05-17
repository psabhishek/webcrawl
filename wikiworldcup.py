#Given is a page having the list of world cup finals. Try extracting the year,
# winner and the host nation

import urllib
import requests
from lxml import html

url = "https://en.wikipedia.org/wiki/List_of_ICC_Cricket_World_Cup_finals"

req = requests.get(url)
tree = html.fromstring(req.text)

obj = tree.cssselect(".wikitable.sortable tr th a ")#css selector for years
a_obj = tree.cssselect(".wikitable.sortable tr td:nth-child(2) a")#css selector for winner
b_obj = tree.cssselect(".wikitable.sortable  tr td:nth-child(6) ")#css selector for host
j = len(obj)
'''
for i in range(0,12):
    print obj[i].text_content()
'''
k = len(a_obj)

for i in range(0,k):
    dict = {'year': obj[i+1].text_content()
        , 'winner': a_obj[i].text_content(), 'host': b_obj[i].text_content()}
    print "YEAR --"+dict['year'],"  WINNER --" +dict['winner'],"  HOST --" +dict['host']