from math import*
var = float(input("angulo: "))
d = float(input("distancia: "))
var2 = radians(var)
var3 = sqrt(d*(9.8/sin(2*var2)))
print(round(var3,2))
