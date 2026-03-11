from math import*
raio = float(input("insira um numero: "))
lados = int(input("insira outro numero: "))

a = raio * cos(pi/lados)

print(round(a,2))