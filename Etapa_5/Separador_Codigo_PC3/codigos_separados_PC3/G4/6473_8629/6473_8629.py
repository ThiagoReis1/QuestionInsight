import math

lado = float(input("lado: "))
pi = math.pi / 10
tan = 2 *math.tan(pi)
apotema = (lado) / tan
area = 5 * lado * apotema
print(round(area, 2))