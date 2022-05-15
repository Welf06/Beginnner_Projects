from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import re 

class Scrapper():
   
   def article_getter(self, url):
      page = requests.get(url)
      soup = BeautifulSoup(page.text, "html.parser")
      article = ''
      if re.findall('^https://times', url): 
         article_div = soup.find_all('div', class_='main')
      else:
         article_div = soup.find_all('p')
         for p in article_div:
            article += str(p.text)
      return article
   
class Hindu(Scrapper):
   hindu_urls = ['https://www.google.com/search?q=hindu&tbm=nws&ei','https://www.google.com/search?q=hindu&tbm=nws&ei=9T8XYvOfGKCeseMPl_q1yA8&start=10&sa=N&ved=2ahUKEwiz7rid9Jf2AhUgT2wGHRd9DfkQ8tMDegQIARA4&biw=1536&bih=714&dpr=1.25', 'https://www.google.com/search?q=hindu&tbm=nws&ei=sUAXYrdZyZqx4w_LubKQBg&start=20&sa=N&ved=2ahUKEwj39fP29Jf2AhVJTWwGHcucDGI4ChDy0wN6BAgBEDo&biw=1536&bih=714&dpr=1.25', 'https://www.google.com/search?q=hindu&tbm=nws&ei=2kAXYvbCFNmXseMPssum8Ac&start=30&sa=N&ved=2ahUKEwj2l86K9Zf2AhXZS2wGHbKlCX44FBDy0wN6BAgBEDw&biw=1536&bih=714&dpr=1.25', 'https://www.google.com/search?q=hindu&tbm=nws&ei=7UAXYpbfPMKRseMPgtG34Ao&start=40&sa=N&ved=2ahUKEwjWif6T9Zf2AhXCSGwGHYLoDaw4HhDy0wN6BAgBED4&biw=1536&bih=714&dpr=1.25']
   
   ndtv_urls = ['https://www.google.com/search?q=ndtv&tbm=nws&ei','https://www.google.com/search?q=ndtv&rlz=1C1ONGR_enIN984IN984&tbm=nws&ei=gLEXYo-vMIqJ-AaY77HQAw&start=10&sa=N&ved=2ahUKEwiP7-3B4Jj2AhWKBN4KHZh3DDo4FBDy0wN6BAgBEDk&biw=1536&bih=714&dpr=1.25', 'https://www.google.com/search?q=ndtv&rlz=1C1ONGR_enIN984IN984&tbm=nws&ei=hrEXYvHJMMbP-QaZ75nICg&start=20&sa=N&ved=2ahUKEwjxpNzE4Jj2AhXGZ94KHZl3Bqk4ChDy0wN6BAgBEDo&biw=1536&bih=714&dpr=1.25', 'https://www.google.com/search?q=ndtv&rlz=1C1ONGR_enIN984IN984&tbm=nws&ei=obEXYoC_D8ifhwPsjqDwDg&start=30&sa=N&ved=2ahUKEwjAk6vR4Jj2AhXIz2EKHWwHCO44FBDy0wN6BAgBEDw&biw=1536&bih=714&dpr=1.25', 'https://www.google.com/search?q=ndtv&rlz=1C1ONGR_enIN984IN984&tbm=nws&ei=q7EXYtXqGrSC1e8Phf6ZqAc&start=40&sa=N&ved=2ahUKEwiV7JjW4Jj2AhU0QfUHHQV_BnU4HhDy0wN6BAgBED4&biw=1536&bih=714&dpr=1.25']
   
   toi_urls = ['https://www.google.com/search?q=times+of+india&rlz=1C1ONGR_enIN984IN984&source=lnms&tbm=nws&sa']
   
   def url_getter(self, urls):
      
      urls = Hindu.toi_urls
      for url in urls:
         list_of_urls = [] 
         page = requests.get(url)
         soup = BeautifulSoup(page.text, "html.parser")
         article_div = soup.find_all('a')
         for a in article_div:
            if 'google' not in str(a):
               link = re.findall('https[\S]+' ,a['href'])
            if a.text != '':
               try:
                  end_index = link[0].find('&')
                  link = link[0][0:end_index]
                  list_of_urls.append((a.find('div').text, link))
               except:
                  continue
         return list_of_urls



# hindu = Hindu()
# lst = hindu.url_getter()
# article_list = {}
# for i in lst:
#    article_list[i[1]] = hindu.article_getter(i[1])
   
# print(hindu.article_getter('https://timesofindia.indiatimes.com/blogs/toi-editorials/ukraine-crisis-a-recovering-indian-economy-has-to-navigate-stormy-waters-once-again/'))


