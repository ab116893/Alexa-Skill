# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:03:14 2017

@author: sudar
"""

from bs4 import BeautifulSoup
import json
import requests



url = requests.get("https://www.unh.edu/dining/regular-hours-operation")
html_content = url.text
soup = BeautifulSoup(url.content,"html.parser")
for tr in soup.find_all("tr")[1]:
    tds = tr.find_all("td")
    print("value:%s, value2:%s, value3:%s\n" % \
          (tds[0].text, tds[0].text, tds[2].text))
    
    
    
    
    




    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    


    


    






