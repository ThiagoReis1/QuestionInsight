from math import*
var = float(input("Ve: "))
var1 = float(input("Mo: "))
var2 = float(input("Mf: "))

dV = var * (log (var1/var2))

print(round(dV,2))