'''
Given is a page having a list of all the states and union territories of India. Try the following:

    Fetch count of States and Union Territories
    Fetch population and date of formation of each state

'''
import urllib
import requests
from lxml import html

url = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"

req = requests.get(url)
tree = html.fromstring(req.text)

obj = tree.cssselect(".wikitable.sortable td:nth-child(2) a")#css selector for name of states

a_obj = tree.cssselect(".wikitable.sortable td:nth-child(4)")#css selector for date of formation
b_obj = tree.cssselect(".wikitable.sortable td:nth-child(5)")#css selector for population


for i in range(0, 29):
    dict = {'Name': obj[i].get("title")
                , 'date of formation': a_obj[i].text_content(), 'population': b_obj[i].text_content()}
    print "NAME -- "+dict['Name'],"DATE OF FORMATION-- " +dict['date of formation'],"POPULATION-- " +dict['population']
no_states = tree.cssselect(".wikitable.sortable tr:nth-child(30) td")
print "NO OF STATES  "+no_states[0].text_content()   #no of states



