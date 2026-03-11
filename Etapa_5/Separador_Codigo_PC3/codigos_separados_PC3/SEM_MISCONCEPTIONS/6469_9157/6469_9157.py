from math import tan,pi
lado = float(input("lado "))
apotema = float(lado/2*tan(pi/6))
area = float(3*lado*apotema*3)
print(round(area, 2))
