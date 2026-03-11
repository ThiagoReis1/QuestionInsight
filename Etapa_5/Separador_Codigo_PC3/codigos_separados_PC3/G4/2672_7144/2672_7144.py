from math import*

r = float(input("Digite o valor do raio: "))
n = int(input("Digite o numero de lados: "))

area = 0.5*((r*cos(pi/n)))**2 *(tan(pi/n))
				 
print(round(area,2))