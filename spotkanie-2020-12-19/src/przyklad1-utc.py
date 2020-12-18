from datetime import datetime


 
#metoda 1:
import dateutil.tz as tz
tz_utc = tz.gettz("UTC")

teraz = datetime.now(tz_utc)

print(f"Teraz jest {teraz} w strefie {teraz.tzinfo}")

#metoda 2:
from datetime import timezone
tz_utc = timezone.utc

teraz = datetime.now(tz_utc)

print(f"Teraz jest {teraz} w strefie {teraz.tzinfo}")


#metoda 3:
from dateutil.tz import tz

teraz = datetime.now(tz.tzutc())

print(f"Teraz jest {teraz} w strefie {teraz.tzinfo}")
