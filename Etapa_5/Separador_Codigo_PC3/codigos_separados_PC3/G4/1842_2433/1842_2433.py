Q = float(input(" valor inicial: "))
Qf = float(input(" valor final: "))
Y = int(input(" número de anos: ")) 

from math import*

A = log(Qf)
B = log(Q)

r = float ((A - B) / Y)

print (r)