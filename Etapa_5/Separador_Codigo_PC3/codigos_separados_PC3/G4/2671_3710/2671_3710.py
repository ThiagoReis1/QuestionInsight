import math

raio = float(input("Insira o raio: "))
lado_n = float(input("Insira o numero de lados: "))

x = math.pi / lado_n

a = raio * math.cos(x)

print(round(a, 2))