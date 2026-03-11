from math import *
preco  = float(input("Preco: "))
altura = float(input("Altura: "))
raio   = float(input("Raio: "))
volume = pi * raio**2 * altura
total = preco * volume
print(round(total, 2))