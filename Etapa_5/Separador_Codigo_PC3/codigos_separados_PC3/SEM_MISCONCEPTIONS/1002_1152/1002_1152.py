from math import *
preco = float(input("Preço:"))
altura = float(input("Altura:"))
raio = float(input("Raio:"))
volume = pi * raio**2 * altura
total = preco * volume
resultado = round((total),2)
print(resultado)