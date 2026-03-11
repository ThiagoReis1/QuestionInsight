from numpy import *

e = input().upper()

tv = e.count("A") + e.count("E") + e.count("I") + e.count("O") + e.count("U")
to = len(e) - tv

dv = tv * 0.12
do = to * 0.18

print(round((dv+do), 2)) #o 2