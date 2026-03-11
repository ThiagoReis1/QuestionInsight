from math import pi , tan

#Variáveis
L = float(input("Lado do undecagono: "))

#Entrada
apot = L / (2 * tan(pi/11))
area = 11 * L * apot / 2

#Saída
print(round(area,  2))


