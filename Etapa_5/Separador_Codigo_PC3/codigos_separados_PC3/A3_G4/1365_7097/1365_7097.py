from math import*
a=float(input("Qual o angulo?"))
d=float(input("Qual a distancia?"))
g=float(9.8)
p1=round(d*g,2)
p2=radians(a)
p3=sin(2*p2)
p4=round(p3,2)
v1=d*g
v2=(v1/(p3))
vo=(v2**(1/2))
print(round(vo,2))