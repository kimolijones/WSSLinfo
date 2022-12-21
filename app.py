import streamlit as st
import pandas as pd
from datetime import timedelta, datetime
import math
import pytz

st.set_page_config(page_title="WSSLInfo", page_icon=":airplane:")

df = pd.read_html('https://aviationweather.gov/metar/data?ids=WSSL&format=decoded&date=&hours=0&taf=on')
df1 = df[0]
df2 = df[1]

dtt = datetime(year=1, month=1, day=1, hour=0, minute=0, second=0, tzinfo=pytz.timezone("Etc/GMT-8"))

delta = timedelta(minutes=5)

def round_dt(dt, delta):
    return dtt + math.floor((dt - dtt) / delta) * delta

curndt = datetime.now(pytz.timezone("Etc/GMT-8"))
roundt = round_dt(curndt, delta)
disdt = roundt - timedelta(minutes=10)

if disdt.month < 10:
    disdt.month = str("0" + str(disdt.month))
else: # disdt.month >= 10:
    disdt.month = disdt.month

if disdt.day < 10:
    disdt.day = str("0" + str(disdt.month))
else: # disdt.day >= 10:
    disdt.day = disdt.day

if disdt.hour < 10:
    disdt.hour = str("0" + str(disdt.month))
else: # disdt.hour >= 10:
    disdt.hour = disdt.hour

if disdt.minute < 10:
    disdt.minute = str("0" + str(disdt.month))
else: # disdt.minute >= 10:
    disdt.minute = disdt.minute

year = str(disdt.year)
month = str(disdt.month)
day = str(disdt.day)
time = str(disdt.hour)+str(disdt.minute)

print()
print(disdt.hour)
print(disdt.minute)
print(time)
print(curndt)
print(roundt)
print(disdt)

st.title(":airplane: WSSLinfo")
st.text("last refreshed: "+str(curndt))
st.dataframe(df1, 1000)
st.dataframe(df2, 1000)

sgsource = "https://www.nea.gov.sg/docs/default-source/rain-area/dpsri_70km_"+year+month+day+time+"0000dBR.dpsri.png"
print(sgsource)
st.image("https://www.nea.gov.sg/docs/default-source/rain-area/dpsri_70km_"+year+month+day+time+"0000dBR.dpsri.png", width = 853) 
st.image("https://www.nea.gov.sg/assets/images/map/base-853.png", width = 853)
st.write(sgsource)


bigsource = "https://www.nea.gov.sg/docs/default-source/rain-area-240km/dpsri_240km_"+year+month+day+time+"0000dBR.dpsri.png"
print(bigsource)
st.image("https://www.nea.gov.sg/docs/default-source/rain-area-240km/dpsri_240km_"+year+month+day+time+"0000dBR.dpsri.png", width = 853) 
st.image("https://www.nea.gov.sg/assets/images/map/240km-v2.jpg", width = 853)
st.write(bigsource)

st.write("Created by: Lee LK - 268")
st.write("Source code: https://github.com/kimolijones/WSSLinfo")