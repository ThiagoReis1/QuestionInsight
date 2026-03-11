from math import *

p = float(input("Digite o valor da pressão: "))
n = float(input("Digite o numero de mols: "))
t = float(input("Digite a temperatura: ")) + 273.15
r = 0.082

v = (n * r * t) / p

print(v)
