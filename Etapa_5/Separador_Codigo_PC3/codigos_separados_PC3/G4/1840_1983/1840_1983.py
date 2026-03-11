from math import*
n = float(input("numero de mols: "))
v = float(input("volume: "))
temperatura = float(input("temperatura: "))
r = 0.082057
t = temperatura+273.1
p = (n * r * t) / v
print(p)