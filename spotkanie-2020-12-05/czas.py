import datetime as dt
import time as t

t1 = dt.datetime.now()
t.sleep(1)
t2 = dt.datetime.now()

d = t2 - t1 #timedelta

print(d)


import dateutil.tz as tz

tz_polska = tz.gettz('Europe/Warsaw')
tz_hawaii = tz.gettz('Pacific/Honolulu')


t_szczecin = dt.datetime.now(tz_polska)
t_honolulu = dt.datetime.now(tz_hawaii)

offset_szczecin = t_szczecin.utcoffset() / dt.timedelta(hours=1)
offset_honolulu = t_honolulu.utcoffset() / dt.timedelta(hours=1)


wielkanoc = dt.datetime(2020,4,30).astimezone(tz_polska)

boze_narodzenie = dt.datetime(2020,12,30).astimezone(tz_polska)

print(wielkanoc)

print(boze_narodzenie)


#format

#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
