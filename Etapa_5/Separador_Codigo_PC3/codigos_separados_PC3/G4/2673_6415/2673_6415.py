from math import*

r = float(input("Digite o raio:"))
n = int(input("Digite o numero de lados:"))

l = 2 * r * sin(3.14/n)

print(round(l,2))
