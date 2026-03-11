from math import *

a = float(input("raio de a: "))
c = float(input("custo da construcao: "))
			 
perimetro = float(2 * pi * a)

custototal = (perimetro * c)
print(round(custototal, 2))