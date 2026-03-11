from math import *

# faça seu código aqui!
l = int(input("comprimento do lado do decagono: "))
apt = (l) / ( 2 * tan(pi/10))
aread = 5 * l * apt
print(round(aread, 2))