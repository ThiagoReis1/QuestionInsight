from math import *

lado = float(input("lado"))
apotema = (lado / (2 * tan(pi / 10)))
areadecagono = 5 * lado * apotema
print(round(areadecagono,2))