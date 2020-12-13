import datetime as dt
import dateutil.tz as tz

tz_polska = tz.gettz('Europe/Warsaw')
urodzinyM = dt.datetime(2021, 2, 24, tzinfo = tz_polska)
teraz = dt.datetime.now(tz_polska)
ileczasuM = urodzinyM - teraz
print('Urodziny Matiego: ', ileczasuM)
#2021_06_25
wakacje = dt.datetime(2021, 6, 25, tzinfo = tz_polska)
teraz = dt.datetime.now(tz_polska)
ileczasuW = wakacje - teraz
print("Wakacje za: ", ileczasuW)
