from math import *

qnt_p = int(input("digite quantidade de pocoes: "))
sb = ((sqrt(5) - 1) / 4) * qnt_p
sf = (sqrt(5 - 2 * sqrt(5))) * qnt_p
am = ((5 * (5 - 2 * sqrt(5)))) * qnt_p
print(round(sb, 2))
print(round(sf, 2))
print(round(am, 2))