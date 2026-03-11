from math import pi, tan
lado = int(input("digite o lado: "))
apotema = lado/(2*tan(pi/7))
areah = (7*lado*apotema)/2
print(round(areah, 2))
