Q0=float(input("valor inicial: "))
Qf=float(input("valor final: "))
y=float(input("numero de anos: "))

from math import*

r=(log(Qf) - log(Q0))/y

print(r)