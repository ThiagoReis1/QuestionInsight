from math import*


velocidade = input("digite um valor")
distancia = input("digite um valor")

a = asin(distancia*9.8/velocidade**2/)*90/pi
print(round(a,2))