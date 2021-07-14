import requests
import urljoin
from bs4 import BeautifulSoup
from urljoin.urljoin import url_path_join
def web(page,WebUrl):
     if(page>0):
          url = WebUrl
          code = requests.get(url)
          plain = code.text
          s = BeautifulSoup(plain,'html.parser')
          i=1
          for link in s.findAll('a',{'class':'forumlink'}):
               ref = link.get('href')
               print(str(i)+": "+ref)
               i+=1
               web(page-1,ref)


print("TU")               
web(4,'https://www.pcforum.sk')