import urllib
import requests
from lxml import html
url = "http://www.flipkart.com/search?q=dell+inspiron"
#total of 72 pages
req = requests.get(url)

tree = html.fromstring(req.text)
tree.make_links_absolute(url)


obj = tree.cssselect("a.pu-image.fk-product-thumb ")

j = len(obj)
#for i in range(0 , j-1):
k = obj[1].get("href")
req = requests.get(k)
tree = html.fromstring(req.text)
tree.make_links_absolute(url)
a_obj =tree.cssselect(".lnkViewMore")
a = a_obj[0].get("href")
req = requests.get(a)
tree = html.fromstring(req.text)
tree.make_links_absolute(a)
a_obj = tree.cssselect(".line.bmargin10 .review-text")
x = len(a_obj)
for i in range(0,x-1):
    print a_obj[i].text_content()


while 1:
    b_obj = tree.cssselect(".fk-navigation.fk-text-center.tmargin10 .nav_bar_next_prev")

    c = b_obj[0].get("href")
    req = requests.get(c)
    tree = html.fromstring(req.text)
    tree.make_links_absolute(c)
    z_obj = tree.cssselect(".line.bmargin10 .review-text")
    x = len(z_obj)
    for i in range(0, x - 1):
        print a_obj[i].text_content()





