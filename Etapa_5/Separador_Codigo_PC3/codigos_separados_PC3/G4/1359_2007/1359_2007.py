from math import *
ve = float(input("digite velocidade de exautão efetiva: "))
mi = float(input("digite massa inicial: "))
mf = float(input("digite massa final: "))
dv = ve * log(mi/mf)
print(round(dv, 2))