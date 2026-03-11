from math import*
lado = float(input("lado: "))
denominador = radians(float(2 * tan(pi/10)))
apotema = radians(lado/denominador)
area = (5*lado*apotema)
print(round(area, 2))