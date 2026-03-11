import math
cos = math.cos
pi = math.pi
tan = math.tan
raio = float(input("Escreva um numero real aqui: "))
n = int(input("Escreva um numero inteiro aqui: "))
area = 1/2 * (raio * cos(pi/n))**2 * tan(pi/n)
print(round(area, 2))