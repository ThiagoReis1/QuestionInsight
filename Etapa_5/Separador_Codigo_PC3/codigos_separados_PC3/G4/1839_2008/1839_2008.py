from math import *

p = float(input("pressao: "))
n = float(input("numero de mols: "))
T1 = float(input("temperatura: "))

T = T1 + 273.15
R = 0.082

V = n * R * T / p

print(V)
