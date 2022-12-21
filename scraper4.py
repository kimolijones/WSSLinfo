import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import urllib
import os

df = pd.read_html('https://aviationweather.gov/metar/data?ids=WSSL&format=decoded&date=&hours=0&taf=on')


print(df)


def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.nea.gov.sg/weather/rain-areas") 
soup = BeautifulSoup(htmldata, 'html.parser') 


print(soup.find_all(id='rain_overlay'))
