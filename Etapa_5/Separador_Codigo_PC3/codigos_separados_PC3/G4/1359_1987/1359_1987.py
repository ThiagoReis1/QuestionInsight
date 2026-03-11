from math import *
ve = float(input("Velocidade de exaustão efetiva, em m/s:"))
mo = float(input("Massa inicial do foguete, em toneladas:"))
mf = float(input("Massa final do foguete, em toneladas:"))
deltv = ve * log(mo//mf)
print(float(round(deltv,2)))
