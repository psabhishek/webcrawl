import sentmod as s
import urllib
import requests
from lxml import html
url = "http://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=i+phone"
#total of 72 pages
req = requests.get(url)

tree = html.fromstring(req.text)
tree.make_links_absolute(url)

obj = tree.cssselect(".a-link-normal.a-text-normal")
j = len(obj)
url2 = obj[1].get("href")
print url2
req = requests.get(url2)
tree = html.fromstring(req.text)
tree.make_links_absolute(url)

obj_2 = tree.cssselect(".a-column.a-span12.a-text-center a.a-link-normal.a-text-normal")
j = len(obj_2)
print j
k = obj_2[1].get("href")
req = requests.get(k)
tree = html.fromstring(req.text)
tree.make_links_absolute(k)

obj_4 =tree.cssselect(".a-section.a-padding-small .a-row.a-spacing-large a.a-link-emphasis.a-text-bold")
cout = obj_4[0].get("href")
req = requests.get(cout)

tree = html.fromstring(req.text)
tree.make_links_absolute(cout)
obj_5 = tree.cssselect(".a-section.review .a-row.review-data .a-size-base.review-text")
rev_len = len(obj_5)

a_obj =tree.cssselect(".a-pagination li:nth-child(7).page-button")#309 pages
lengh = int(a_obj[0].text_content())
for y in range(0 , rev_len-1):
    print obj_5[y].text_content()
while lengh-1!=0:
    z_obj =tree.cssselect(".a-last a")

    cin = z_obj[0].get("href")


    req = requests.get(cin)
    tree = html.fromstring(req.text)
    tree.make_links_absolute(cin)
    obj_5 = tree.cssselect(".a-section.review .a-row.review-data .a-size-base.review-text")
    for y in range(0 , rev_len-1):
        z = obj_5[y].text_content()
        print z
        sentiment_value, confidence = s.sentiment(z)
        print sentiment_value, confidence
        if confidence * 100 >= 80:
            output = open("//home//abhishek//Desktop//p_q//amazon.txt", "a")
            # output.write(tweets)
            # output.write("::::")
            output.write(sentiment_value)
            output.write("\n")
            output.close()

    lengh-=1

'''

#.a-pagination .a-last pagination


#    obj_3 = tree.cssselect(".a-row.a-spacing-small .a-section")
 #   rev_length = len(obj_3)
 #   for x in rainge(0 , rev_length-1):
  #      print obj_3[x].text_content()

'''
