from math import*

# faça seu código aqui!
lado = float(input("l da figura:"))
apotema = lado/(2*tan(pi/9))
area = (9*lado*apotema)/2
print(round(area,2))