import datetime as dt
import dateutil.tz as tz

tz_honolulu = tz.gettz('Pacific/Honolulu')
print(dt.datetime.now(tz_honolulu))


import datetime as dt
import dateutil.tz as tz

timezone = tz.gettz('Asia/Hong_Kong')
time = dt.datetime.now(timezone)
print (time, time.tzinfo)
