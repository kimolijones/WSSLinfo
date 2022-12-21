import streamlit as st
import pandas as pd
from datetime import timedelta, datetime
import math

st.set_page_config(page_title="WSSLInfo", page_icon=":airplane:")

df = pd.read_html('https://aviationweather.gov/metar/data?ids=WSSL&format=decoded&date=&hours=0&taf=on')
print(df)

def round_dt(dt, delta):
    return datetime.min + math.floor((dt - datetime.min) / delta) * delta

delta = timedelta(minutes=30)

curndt = datetime.now()

roundt = round_dt(curndt,delta)

year = str(roundt.year)
month = str(roundt.month)
day = str(roundt.day)
time = str(roundt.hour)+str(roundt.minute)

print(roundt)

st.write(df)

sgsource = "https://www.nea.gov.sg/docs/default-source/rain-area/dpsri_70km_"+year+month+day+time+"0000dBR.dpsri.png"
print(sgsource)
st.image(sgsource) 
st.image("https://www.nea.gov.sg/assets/images/map/base-853.png")
st.write(sgsource)


bigsource = "https://www.nea.gov.sg/docs/default-source/rain-area-240km/dpsri_240km_"+year+month+day+time+"0000dBR.dpsri.png"
print(bigsource)
st.image(bigsource) 
st.image("https://www.nea.gov.sg/assets/images/map/240km-v2.jpg")
st.write(bigsource)