# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:03:14 2017

@author: sudar
"""
import urllib
from bs4 import BeautifulSoup
import json
import urllib.request
        

def make_soup(url):
        link = urllib.request.urlopen(url)
        soupdata = BeautifulSoup(link, "html.parser")
        return soupdata
soup = make_soup("https://www.unh.edu/dining/regular-hours-operation")


    
    #for hours in record.find_all("th"):
   #hoursdata = ""
mylist =[]
for record in soup.find_all("tr"):
    list_of_hours=[]
    for hour in record.find_all(["th","td"]):
        getdata=record.text, hour.text
        list_of_hours.append(getdata)
    mylist.append(list_of_hours)
print(mylist)

        
        
    
 
            
        
 
    
            
                
                
            
            
            
            
            
           
            
       
      
       
       
       
       
        #hoursdata =hoursdata+","+data.text
        
        #hoursdatasave = hoursdatasave + "\n" + hoursdata[1:]

    

    
        
    
    




    


    




    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    


    


    






