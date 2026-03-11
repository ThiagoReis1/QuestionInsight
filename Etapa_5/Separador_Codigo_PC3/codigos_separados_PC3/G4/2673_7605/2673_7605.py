import math

raio = float(input("Digite o valor do raio: " ))
n = int(input("Digite o numero de lados: "))
l = 2 * raio * math.sin(math.pi/n)
print(round(l,2))