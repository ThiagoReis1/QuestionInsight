from math import*

r = float(input("Digite o raio: "))
n = int(input("Digite o numero de lados: "))

a = (1/2) * ((r  * cos(pi/n))**2 * tan(pi/n))

print(round(a,2))
