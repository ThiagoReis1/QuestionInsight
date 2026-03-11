from math import*
raio = float(input("Raio:"))
lados = int(input("Lados:"))

lado=2*raio*sin(pi/lados)

print(round(lado,2))