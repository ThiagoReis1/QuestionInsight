from numpy import *


a = array(eval(input("Alimentos: ")))
b = array(eval(input("Quantidade: ")))

s = 0

for i in range(size(a)):
    if a[i].upper() == "BANANA":
        s += b[i]*0.97
    elif a[i].upper() == "BIFE":
        s += b[i]*2.95
    elif a[i].upper() == "FEIJOADA":
        s += b[i]*1.27
    elif a[i].upper() == "OMELETE":
        s += b[i]*1.04
    elif a[i].upper() == "TOMATE":
        s += b[i]*0.2

print(round(s,2))