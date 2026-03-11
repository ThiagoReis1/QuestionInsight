Qi = float(input("valor inicial:"))
Qf = float(input("valor final:"))
Y = int(input("numero de anos:"))

from math import*

A = log(Qf) 
B = log(Qi)

r = (A - B) / Y

print(r)


