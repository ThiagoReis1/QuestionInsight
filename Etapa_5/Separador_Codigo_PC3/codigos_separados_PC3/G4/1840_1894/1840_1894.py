from math import *

n = float(input("numero de mols: "))
V = float(input("volume do gas: "))
T1 = float(input("temperatura de um gas: "))

T = T1 + 273.1
R = 0.082057

# calculo da pressao

p = n * R * T / V

# impressao da pressao

print(p)