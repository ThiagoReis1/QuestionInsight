from math import*

x = (float(input("comprimento do lado do decagono: ")))
lado = x
apt = 2*tan(pi/10)
apotema = lado/apt

area = 5*lado*apotema
		
print(round(area,2))