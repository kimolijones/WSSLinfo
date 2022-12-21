from datetime import timedelta, datetime
import math

def round_dt(dt, delta):
    return datetime.min + math.floor((dt - datetime.min) / delta) * delta

delta = timedelta(minutes=30)

dt = datetime(2022, 9, 1, 14, 28, 0)
print(round_dt(dt,delta))

print(datetime.min)

dt = datetime.now()
print(round_dt(dt,delta))
print(datetime.min)