#obj shows the css selector for all the linkes on the first page
#then I took out the cssselector of last page so i get no of pages
#then i just go to css selecor of arrow untill i reach last page




import urllib
import requests
from lxml import html
url = "http://www.bedbathandbeyond.com/store/category/bedding/bedding/10504/"
#total of 72 pages
req = requests.get(url)

tree = html.fromstring(req.text)
tree.make_links_absolute(url)

obj = tree.cssselect(".productContent.ec_listing a.prodImg")#css select for first page


j = len(obj)
for i in range(0, j - 1):
    print obj[i].get("href")

a_obj = tree.cssselect(".listPageNumbers li:nth-child(5)")#css select for last page it just give the no of pages
x = int(a_obj[1].text_content())


while x-1!=0:

    obj = tree.cssselect(".listPageNumbers .redirPage.dynFormSubmit.pagArrow")#css select for arrow
    j = len(obj)
    j = obj[1].get("href")
    print obj[1].get("href")
    req = requests.get(j)

    tree = html.fromstring(req.text)
    tree.make_links_absolute(j)
    obj2 = tree.cssselect(".productContent.ec_listing a.prodImg")#extract all the items from all the page
    j = len(obj2)
    for i in range(0, j - 1):
        print obj2[i].get("href")
    x-=1


