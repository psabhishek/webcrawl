
import urllib
import requests
from lxml import html
url = "http://www.flipkart.com/apple-iphone-6-plus/p/itme7zfybgjccnzu?pid=MOBEYHZ2Z8N6RDFE&al=NJUVYIA%2Fw4WtXWUmTD1QJ8ldugMWZuE7Qdj0IGOOVquzvKqM74%2Bw4ozF8ood385i6wtImiC4GuE%3D&ref=L%3A1736779214712752633&srno=p_1&otracker=from-search"
#total of 72 pages
req = requests.get(url)

tree = html.fromstring(req.text)
tree.make_links_absolute(url)


obj = tree.cssselect("span .review-text")
j = len(obj)
print j