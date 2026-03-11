import math

r = float(input("Raio: "))
n = int(input("Numero de lados: "))

L = round(2*r*math.sin(math.pi/n),2)

print(L)