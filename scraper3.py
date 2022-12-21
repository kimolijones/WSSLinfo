import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import urllib
import os

df = pd.read_html('https://aviationweather.gov/metar/data?ids=WSSL&format=decoded&date=&hours=0&taf=on')


print(df[1])


def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.nea.gov.sg/weather/rain-areas") 
soup = BeautifulSoup(htmldata, 'html.parser') 


img_list = []
dl_list = []

for img in soup.find_all('img'):
    print(img.get('src'))
    img_list.append(img.get('src'))
    print(img_list)
    dl_list.append('https://www.nea.gov.sg'+str(img.get('src')))
    print(dl_list)
    


