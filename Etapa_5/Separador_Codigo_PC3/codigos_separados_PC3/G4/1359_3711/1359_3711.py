from math import *
vef = float(input("velocidade de exaustao efetiva"))
mi = float(input("massa inicial"))
mf = float(input("massa final"))
delta_v = vef*log(mi/mf)
print(round(delta_v,2))