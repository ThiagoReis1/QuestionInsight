from math import *

b = float(input("Digite o lado de b: "))
c = float(input("Digite o lado de c: "))
alfa = float(input("Digite o valor de alfa: "))

alfa = radians(alfa)
a =(sqrt(b**2 + c**2 - 2 * b * c * cos(alfa)))

print (round(a , 2))
