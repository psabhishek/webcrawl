import sentmod as s
import urllib
import requests
from lxml import html
ask = raw_input("search??")
url = "http://www.flipkart.com/search?q="+ask+""
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
        tweet = a_obj[i].text_content()
        print tweet
        sentiment_value, confidence = s.sentiment(tweet)
        print sentiment_value, confidence
        if confidence * 100 >= 80:
            output = open("//home//abhishek//Desktop//p_q//flip.txt", "a")
            # output.write(tweets)
            # output.write("::::")
            output.write(sentiment_value)
            output.write("\n")
            output.close()





