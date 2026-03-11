import math
raio = float(input("digite o valor: "))
lados = int(input("digite o valor: "))
L = 2*raio*math.sin(math.pi/lados)
print(round(L,2))
