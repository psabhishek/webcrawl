import urllib
import requests
from lxml import html
url = "http://www.snapdeal.com/search?keyword=i%20phone&sort=rlvncy"
#total of 72 pages
req = requests.get(url)

tree = html.fromstring(req.text)
tree.make_links_absolute(url)



obj = tree.cssselect(".col-xs-19.reset-padding .product-row.js-product-list .col-xs-6.product-tuple-listing.js-tuple .product-tuple-description a")
j = len(obj)
print j
for i in range(0,j-1):
    print obj[i].get("href")


