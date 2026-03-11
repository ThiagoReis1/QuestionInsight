from math import *
raio = float(input("Raio: "))
num_lados = int(input("Numero de lados:"))
apotema = raio * cos(pi/num_lados)
print(round(apotema,2))

