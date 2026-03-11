import math 
velocidade = float(input("velocidade:"))
distancia = float(input("distancia:"))

a = math.asin(distancia*9.8/velocidade**2)*90/math.pi
print(round(a, 2))