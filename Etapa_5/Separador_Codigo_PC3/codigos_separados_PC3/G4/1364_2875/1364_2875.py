from math import*
Vo= float(input("velocidade inicial: "))
d= float(input("distancia: "))

a= asin(d * 9.8 /(Vo**2) ) * (90/ pi)

print(round(a,2))
				 

		