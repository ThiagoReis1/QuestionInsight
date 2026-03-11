from math import *

n = int(input("digite a porcao"))

sn1 = sqrt(5)
sn2 = sn1 - 1
sn3 = sn2 / 4
sn4 = n * sn3

sf1 = sqrt(5)
sf2 = sf1 * 2
sf3 = 5 - sf2
sf4 = sqrt(sf3)
sf5 = n * sf4

a1 = sqrt(5)
a2 = a1 * 2
a3 = 5 - a2
a4 = 5 * a3
a5 = n * a4

print(round(sn4,2))
print(round(sf5,2))
print(round(a5,2))


a5 = n * a4