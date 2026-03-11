from math import*

raio = float(input("Digite o raio do poligono regular: "))
lado = int(input("Digite o numero de lados: "))

areaA = (1/2)*((raio*cos(radian(pi/lado)**2)*radians(tan(pi/lado))))
print(round(areaA, 2))
				  



