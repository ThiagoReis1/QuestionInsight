from math import*

q0 = float(input("Reais: "))
r = float(input("Rendimento: "))

y = ((log(3*q0) - log(q0))/r)

print(int(y)+1)