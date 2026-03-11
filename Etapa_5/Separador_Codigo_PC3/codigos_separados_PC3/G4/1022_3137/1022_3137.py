from math import *
a = float(input("valor da area:  " ))
custo = float(input("valor do custo:  "))
x = 2 * a **2 * (2 **0.5 + 1 )
y = x * custo
print(round(y, 2))