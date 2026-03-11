import math

r = float(input("Qual o raio?"))
n = int(input("Qual o numero de lados?"))

L = 2 * r * math.sin(math.pi / n)

print(round(L,2))