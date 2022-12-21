import streamlit as st
import pandas as pd
from datetime import timedelta, datetime
import math

st.set_page_config(page_title="WSSLInfo", page_icon=":airplane:")

df = pd.read_html('https://aviationweather.gov/metar/data?ids=WSSL&format=decoded&date=&hours=0&taf=on')

def round_dt(dt, delta):
    return datetime.min + math.floor((dt - datetime.min) / delta) * delta

delta = timedelta(minutes=5)

curndt = datetime.now()
roundt = round_dt(curndt,delta)
disdt = roundt - timedelta(minutes=10)

year = str(disdt.year)
month = str(disdt.month)
day = str(disdt.day)
time = str(disdt.hour)+str(disdt.minute)

print(roundt)
print(disdt)

st.write(df)

sgsource = "https://www.nea.gov.sg/docs/default-source/rain-area/dpsri_70km_"+year+month+day+time+"0000dBR.dpsri.png"
print(sgsource)
st.image("https://www.nea.gov.sg/docs/default-source/rain-area/dpsri_70km_"+year+month+day+time+"0000dBR.dpsri.png") 
st.image("https://www.nea.gov.sg/assets/images/map/base-853.png")
st.write(sgsource)


bigsource = "https://www.nea.gov.sg/docs/default-source/rain-area-240km/dpsri_240km_"+year+month+day+time+"0000dBR.dpsri.png"
print(bigsource)
st.image("https://www.nea.gov.sg/docs/default-source/rain-area-240km/dpsri_240km_"+year+month+day+time+"0000dBR.dpsri.png") 
st.image("https://www.nea.gov.sg/assets/images/map/240km-v2.jpg")
st.write(bigsource)