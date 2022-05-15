from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import re 

def url_getter(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        articles = soup.find_all(class_ = "news_Itm-cont")
        return [(art.a.text, art.a['href']) for art in articles]

def article_getter(url):
   page = requests.get(url)
   soup = BeautifulSoup(page.text, "html.parser")
   article_div = soup.find_all(id= 'ins_storybody')
   return article_div[0].text
   
   
url = 'https://www.ndtv.com/india/'
lst = url_getter(url)
for i in lst:
   article = article_getter(i[1])
   print(article)
   break