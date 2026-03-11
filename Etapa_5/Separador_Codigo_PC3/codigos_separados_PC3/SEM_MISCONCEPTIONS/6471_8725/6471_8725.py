from math import*

# faça seu código aqui!

x=float(input("comprimento do lado:"))
apotema= x/(2*tan(pi/8))
area=4*x*apotema

print(round(area,2))
