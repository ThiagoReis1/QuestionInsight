from math import *
raio = float(input("Digite o raio: "))
n = int(input("Digite o numero de lado: "))

lado = 2 * raio * sin(pi/n)

print(round(lado, 2))