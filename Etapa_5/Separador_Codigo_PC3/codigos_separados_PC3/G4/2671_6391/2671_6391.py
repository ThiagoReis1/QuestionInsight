from math import * 

r = float(input("Determine um valor real para o raio: "))

l = int(input("Digite um numero de Lados para o poligono: "))

a = r * cos ( pi / l )

print(round(a, 2))