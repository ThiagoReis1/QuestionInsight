from math import *
r = float(input("Digite aqui o raio:"))
n = int(input("Digite aqui o numero de lados:"))


apotema = r * cos( pi/n)

print(round(apotema, 2))