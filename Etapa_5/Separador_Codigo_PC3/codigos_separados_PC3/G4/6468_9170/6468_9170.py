from math import tan, pi

cp = float(input("Comprimento do ladodo pentagono:"))

apot = cp/(2*tan(pi/5))

area = (5*cp*apot)/2

print(round(area,2))