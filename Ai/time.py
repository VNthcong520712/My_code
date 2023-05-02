import datetime as dt
from time import strftime as sf

now = dt.datetime.now()
print(now.hour, now.minute, now.second)
print(now.day, now.month, now.year, "\n")

print(sf('%H'), sf('%M'), sf("%S"))
print(sf('%d'), sf('%m'), sf("%Y"))
print(sf('%h'), sf('%d'), sf("%y"))