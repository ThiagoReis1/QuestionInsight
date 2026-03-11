from math import *
n = float(input("Digite o numero de mols:"))
V = float(input("Digite o volume:"))
t = float(input("Digite a temperatura:"))

T = t + 273.1
R = 0.082057

p = (n * R * T)/V

print(p)