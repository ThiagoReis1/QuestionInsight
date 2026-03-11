v0 = float(input('qual a velocidade inicial?'))
d = float(input('qual a distancia entre voce e o falmer?'))
#calculo
from math import *
calc = (d*(9.8/(v0**2)))
b = asin(calc) * 90/pi
print(round(b,2))