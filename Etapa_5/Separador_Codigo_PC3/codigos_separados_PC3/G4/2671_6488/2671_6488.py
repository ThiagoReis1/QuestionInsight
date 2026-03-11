import math

r = float(input("Digite o raio do poligono: "))
n = int(input("Qual o numero de lados do poligono? "))

a = r * math.cos(math.pi/n)

print(round(a, 2))