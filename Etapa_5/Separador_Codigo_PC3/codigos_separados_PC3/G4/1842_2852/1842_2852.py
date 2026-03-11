from math import *
q0 = float(input("valor inicial "))
qf = float(input("valor final "))
y = float(input("anos "))
r = (log(qf) - log(q0)) / y
print(r)