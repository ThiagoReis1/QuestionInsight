from math import *

lado = float(input("lado do heptagono: "))
apotema = lado/(2*tan(pi/7))
area = (7 * lado * apotema)/2
# faça seu código aqui!
print(round(area,2))