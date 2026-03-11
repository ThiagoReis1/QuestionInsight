Q0= float(input("valor inicial: "))
Qf= float(input("valor final: "))
y= int(input("anos: "))

from math import*

r= (log(Qf) - log(Q0))/ y

print(r)


