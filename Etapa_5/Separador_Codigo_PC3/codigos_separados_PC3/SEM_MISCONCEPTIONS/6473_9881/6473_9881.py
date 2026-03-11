from math import*
lado = float(input("comprimento do lado: "))
apotema = lado/(2*tan(pi/10))
AreaD = 5*lado*apotema
round(AreaD, 2)